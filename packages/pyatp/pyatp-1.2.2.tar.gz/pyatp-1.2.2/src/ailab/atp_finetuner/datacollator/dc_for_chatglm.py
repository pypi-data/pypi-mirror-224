import torch
from typing import Dict, Optional, Sequence, Union
from transformers import DataCollatorWithPadding,BatchEncoding,PreTrainedTokenizer,PreTrainedModel
from ailab.atp_finetuner.datacollator import AILabDataCollator
from ailab.atp_finetuner import constant
from ailab.atp_finetuner.preprossor import AILabPreprocessor
from ailab.atp_finetuner.model import AILabModel
from ailab.atp_finetuner.build import DataCollatorRg
from ailab.atp_finetuner.constant import Task, Model

class DataCollatorForChatGLM(DataCollatorWithPadding):
        r"""
        Data collator for ChatGLM. It is capable of dynamically padding for batched data.
        """
        def __init__(
                self,
                model: PreTrainedModel,
                tokenizer: PreTrainedTokenizer,
                ignore_pad_token_for_loss: Optional[bool] = True
        ):
            super().__init__(tokenizer, padding=True)
            IGNORE_INDEX = -100
            self.model = model
            self.label_pad_token_id = IGNORE_INDEX if ignore_pad_token_for_loss else tokenizer.pad_token_id
            if tokenizer.eos_token_id == 130005:
                self.get_attention_masks = self.get_attention_masks_v1
                self.get_position_ids = self.get_position_ids_v1
            else:
                self.get_attention_masks = self.get_attention_masks_v2
                self.get_position_ids = self.get_position_ids_v2

        def get_attention_masks_v1(self, input_ids: torch.Tensor, device: torch.device) -> torch.Tensor:
            r"""
            Generates attention masks for left-padded sequences.

            Note that ChatGLM assigns False on token to be attended in attention mask. In general settings, it should be True.

            According to: https://huggingface.co/THUDM/chatglm-6b/blob/v1.1.0/modeling_chatglm.py#L680
            """
            batch_size, seq_length = input_ids.size()
            attention_mask = torch.ones((batch_size, seq_length, seq_length), device=device)
            attention_mask.tril_()

            for i, seq in enumerate(input_ids):
                attention_mask[i, :, :(seq == self.tokenizer.bos_token_id).nonzero()[0].item()] = 1 # context
                attention_mask[i, :, :(seq != self.tokenizer.pad_token_id).nonzero()[0].item()] = 0 # padding

            attention_mask.unsqueeze_(1)
            attention_mask = (attention_mask < 0.5).bool()
            return attention_mask

        def get_position_ids_v1(self, input_ids: torch.Tensor, device: torch.device) -> torch.Tensor:
            r"""
            Generates position ids for left-padded sequenes.

            According to: https://huggingface.co/THUDM/chatglm-6b/blob/v1.1.0/modeling_chatglm.py#L692
            """
            batch_size, seq_length = input_ids.size()
            mask: int = self.model.config.mask_token_id
            gmask: int = self.model.config.gmask_token_id
            position_ids = torch.zeros((batch_size, seq_length), dtype=torch.long, device=device)
            block_position_ids = torch.zeros((batch_size, seq_length), dtype=torch.long, device=device)

            for i, seq in enumerate(input_ids):
                mask_token = gmask if gmask in seq else mask
                context_length = (seq == self.tokenizer.bos_token_id).nonzero()[0].item()
                padding_length = (seq != self.tokenizer.pad_token_id).nonzero()[0].item()
                position_ids[i, padding_length:] = torch.arange(
                    seq_length - padding_length,
                    dtype=torch.long,
                    device=device
                )
                if self.model.position_encoding_2d or (mask_token != gmask): # 2d position encoding or not gMASK
                    position_ids[i, context_length:] = (seq == mask_token).nonzero()[0].item() - padding_length # mask position
                block_position_ids[i, context_length:] = torch.arange(
                    seq_length - context_length,
                    dtype=torch.long,
                    device=device
                ) + 1

            if self.model.position_encoding_2d:
                position_ids = torch.stack((position_ids, block_position_ids), dim=1)

            return position_ids


        def get_attention_masks_v2(self, input_ids: torch.Tensor, device: torch.device) -> torch.Tensor:
            r"""
            Generates attention masks for left-padded sequences.
            """
            batch_size, seq_length = input_ids.size()
            attention_mask = torch.ones((batch_size, seq_length), device=device)

            for i, seq in enumerate(input_ids):
                attention_mask[i, :(seq != self.tokenizer.pad_token_id).nonzero()[0].item()] = 0 # padding

            return attention_mask

        def get_position_ids_v2(self, input_ids: torch.Tensor, device: torch.device) -> torch.Tensor:
            r"""
            Generates position ids for left-padded sequenes.
            """
            batch_size, seq_length = input_ids.size()
            position_ids = torch.zeros((batch_size, seq_length), dtype=torch.long, device=device)

            for i, seq in enumerate(input_ids):
                padding_length = (seq != self.tokenizer.pad_token_id).nonzero()[0].item()
                position_ids[i, padding_length:] = torch.arange(seq_length - padding_length, dtype=torch.long, device=device)

            return position_ids

        def __call__(self, features: Sequence[Dict[str, Union[torch.Tensor, Sequence[int]]]]) -> BatchEncoding:
            r"""
            Pads batched data to the longest sequence in the batch.

            We adopt left-padding in both training and evaluation.
            """
            if isinstance(features[0]["input_ids"], torch.Tensor):
                input_ids = [feature["input_ids"].clone().detach().flip(0) for feature in features]
            else:
                input_ids = [torch.tensor(feature["input_ids"]).flip(0) for feature in features]

            if "labels" in features[0]:
                if isinstance(features[0]["labels"], torch.Tensor):
                    labels = [feature["labels"].clone().detach().flip(0) for feature in features]
                else:
                    labels = [torch.tensor(feature["labels"]).flip(0) for feature in features]
                input_ids = input_ids + labels # pad them to the same length

            input_ids = torch.nn.utils.rnn.pad_sequence(
                input_ids,
                batch_first=True,
                padding_value=self.tokenizer.pad_token_id
            ).flip(-1)

            batch = {}

            if "labels" in features[0]:
                input_ids, labels = input_ids.split(len(features), dim=0)
                labels = torch.where(labels != self.tokenizer.pad_token_id, labels, self.label_pad_token_id)
                batch["labels"] = labels

            batch["input_ids"] = input_ids
            batch["attention_mask"] = self.get_attention_masks(input_ids, device=input_ids.device)
            batch["position_ids"] = self.get_position_ids(input_ids, device=input_ids.device)

            return BatchEncoding(batch)

@DataCollatorRg.register((Task.question_answering, Model.chatglm_6b))
@DataCollatorRg.register((Task.question_answering, Model.chatglm2_6b))
class ChatglmDataCollator(AILabDataCollator) :
    def __init__(self, datacollator, preprocessor):
        super().__init__(datacollator, preprocessor)
    
    def forward(self, **kwargs):
        pass

    @classmethod
    def build_datacollator(cls, framework:constant.Framework, preprocessor:AILabPreprocessor,model:AILabModel) :
        datacollator = DataCollatorForChatGLM(model.model_ins, preprocessor.preprocessor_ins)
        return cls(datacollator, preprocessor)