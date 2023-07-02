import os
"""
用于处理用户输入路径校验的工具
"""


def get_full_path(base_path, input):
    full_path = os.path.abspath(
        os.path.normpath(os.path.join(base_path, input)))
    # 检查生成的路径是否在期望的目录下
    if full_path.startswith(base_path):
        return full_path
    else:
        raise ValueError(f"Non-Supported Path: {input}")
