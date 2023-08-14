# 通过多个RGB最大值分类图片

import imghdr
import glob
import math
import numpy as np
from PIL import Image

# 读取数量排名前 max_colors 的像素颜色
def read_image_RGB(image, max_colors = 5):
    # 打开图片并转换为 RGB 格式
    img = Image.open(image)
    img_rgb = img.convert('RGB')

    # 将图像转换为 numpy 数组以进行处理
    np_img = np.array(img_rgb)

    # 将数组重新形状为一个一维列表，即每个像素都是一个元素
    np_img = np_img.reshape((np_img.shape[0] * np_img.shape[1], 3))

    # 使用 numpy 中的 unique 函数获取所有不同的颜色值，并计算它们在图像中出现的次数
    colors, counts = np.unique(np_img, axis=0, return_counts=True)

    # 按照出现次数从大到小排序，并选择前几个频率最高的颜色
    counts_sort_idx = np.argsort(-counts)
    return colors[counts_sort_idx][:max_colors]

# 读取数量排名前 max_colors 的像素颜色
def read_image_path(path, max_colors = 5, filetype = {'jpg', 'png', 'jpeg'}):
    rgbs_list = {}  # 存储图片信息 和 图片的关键rgb值
    for file_abs in glob.glob(path):
        if imghdr.what(file_abs) in filetype:
            image_name = file_abs.replace(path.rstrip('*'), '')
            image_rgbs = read_image_RGB(image = file_abs, max_colors = max_colors)
            rgbs_list[image_name] = {"rgbs": image_rgbs, "filepath": file_abs}
    return rgbs_list


def rgb_similarity(colors1, colors2):
    """
    比较两个 RGB 颜色数组的相似度
    :param colors1: 包含多个三元组 (R,G,B) 形式表示颜色值的列表或数组。
    :param colors2: 包含多个三元组 (R,G,B) 形式表示颜色值的列表或数组。
    :return: float, 表示颜色数组间的相似度值，范围在 [0, 1]。
    """
    # 将颜色列表或数组转换为 Numpy 数组，以便进行向量化操作
    colors1 = np.array(colors1)
    colors2 = np.array(colors2)
    
    # 计算两个颜色数组之间所有颜色差异的欧几里得距离
    diff = np.sqrt(np.sum((colors1 - colors2) ** 2, axis=1))
    
    # 根据颜色空间的最大距离计算相似度值
    max_distance = math.sqrt(255 ** 2 + 255 ** 2 + 255 ** 2)
    similarity = 1.0 - diff / max_distance
    
    # 对所有相似度值求平均，得到最终的相似度分数
    avg_similarity = np.mean(similarity)
    
    return avg_similarity