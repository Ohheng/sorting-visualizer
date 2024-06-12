import copy
from .data import Data


# 选择排序算法
def selection_sort(data_set):
    # 初始化一个帧列表，用于存储排序过程中每一步的状态
    frames = [data_set]

    # 深拷贝数据集，确保后续操作不改变原始数据
    ds = copy.deepcopy(data_set)

    # 遍历数据集，选择排序算法的外层循环
    for i in range(0, Data.data_count - 1):
        # 遍历数据集，选择排序算法的内层循环
        for j in range(i + 1, Data.data_count):
            # 复制当前状态并标记比较的元素
            ds_r = copy.deepcopy(ds)
            frames.append(ds_r)
            ds_r[i].set_color("r")  # 标记当前选择的元素
            ds_r[j].set_color("k")  # 标记当前比较的元素

            # 如果当前元素小于选择的元素，则交换位置
            if ds[j].value < ds[i].value:
                ds[i], ds[j] = ds[j], ds[i]

    # 将最终排序完毕的状态加入帧列表，返回
    frames.append(ds)
    return frames
