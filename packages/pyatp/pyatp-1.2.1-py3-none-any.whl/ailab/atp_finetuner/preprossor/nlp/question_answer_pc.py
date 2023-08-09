import argparse
import json
from tqdm import tqdm
import transformers
import datasets
from ailab.atp_finetuner.preprossor import AILabPreprocessor
from ailab.atp_dataset.dataset import AILabDataset
from transformers import models
from ailab.atp_finetuner.build import PreProcessorRg
from ailab.atp_finetuner.constant import Task, Model

@PreProcessorRg.register((Task.question_answering, Model.distilbert_base_uncased))
class QuestionAnswerPreProcessor(AILabPreprocessor):
    def __init__(self, dataset, preprocessor):
        super().__init__(dataset, preprocessor)

    @classmethod
    def build_preprocessor(cls, model_name:str, dataset: AILabDataset, pc_dir:str, **kwargs):
        pc_name_dir = model_name if pc_dir is None else pc_dir
        hf_preprocessor = models.auto.AutoProcessor.from_pretrained(pc_name_dir, **kwargs)
        return cls(dataset, hf_preprocessor)

    def process_data(self) ->AILabDataset:
        preprocessor = self._preprocessor
        def preprocessor_func(dataset):
                def preprocess(preprocessor, dataset):
                    questions = [q.strip() for q in dataset["question"]]
                    inputs = preprocessor(
                        questions,
                        dataset["context"],
                        max_length=384,
                        truncation="only_second",
                        return_offsets_mapping=True,
                        padding="max_length",
                    )

                    offset_mapping = inputs.pop("offset_mapping")
                    answers = dataset["answers"]
                    start_positions = []
                    end_positions = []

                    for i, offset in enumerate(offset_mapping):
                        answer = answers[i]
                        start_char = answer["answer_start"][0]
                        end_char = answer["answer_start"][0] + len(answer["text"][0])
                        sequence_ids = inputs.sequence_ids(i)

                        # Find the start and end of the context
                        idx = 0
                        while sequence_ids[idx] != 1:
                            idx += 1
                        context_start = idx
                        while sequence_ids[idx] == 1:
                            idx += 1
                        context_end = idx - 1

                        # If the answer is not fully inside the context, label it (0, 0)
                        if offset[context_start][0] > end_char or offset[context_end][1] < start_char:
                            start_positions.append(0)
                            end_positions.append(0)
                        else:
                            # Otherwise it's the start and end token positions
                            idx = context_start
                            while idx <= context_end and offset[idx][0] <= start_char:
                                idx += 1
                            start_positions.append(idx - 1)

                            idx = context_end
                            while idx >= context_start and offset[idx][1] >= end_char:
                                idx -= 1
                            end_positions.append(idx + 1)

                    inputs["start_positions"] = start_positions
                    inputs["end_positions"] = end_positions
                    return inputs
                return preprocess(preprocessor, dataset)
        tokenized_dataset = self._dataset.to_hf_dataset().map(preprocessor_func, batched=True)
        return AILabDataset(tokenized_dataset)
