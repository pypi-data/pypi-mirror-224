# 造个轮子QuQ，文件相关操作

import os
import shutil


def move_file(file_path, target_dir):
    """
    将一个文件移动到指定目录。
    :param file_path: str, 要移动的文件的完整路径。
    :param target_dir: str, 目标目录的完整路径。
    :return: bool, 表示是否成功移动文件。
    """
    # 如果目标目录不存在，则创建它
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    
    # 拼接出目标文件的完整路径
    target_path = os.path.join(target_dir, os.path.basename(file_path))
    
    try:
        # 移动文件
        shutil.move(file_path, target_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False