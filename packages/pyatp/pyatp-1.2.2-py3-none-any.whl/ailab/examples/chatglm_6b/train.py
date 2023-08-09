import os
import sys

from ailab.utils.other import install_requiremet


def install_req():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    install_requiremet(dir_path)


def chatglm_test():
    import subprocess
    # 启动 shell 脚本
    dir_path = os.path.dirname(os.path.realpath(__file__))
    shell_path = os.path.join(dir_path, "train.sh")
    ret = subprocess.call("sh " + shell_path, shell=True)
    if ret != 0:
        print("训练失败: Check")
    return ret


if __name__ == '__main__':
    exit(chatglm_test())
