import copy
from .data import Data


# 插入排序算法
def insertion_sort(data_set):
    # 初始化一个帧列表，用于存储排序过程中每一步的状态
    frames = [data_set]

    # 深拷贝数据集，确保后续操作不改变原始数据
    ds = copy.deepcopy(data_set)

    # 外层循环，从第二个元素开始
    for i in range(1, Data.data_count):
        # 将当前状态的深拷贝加入帧列表
        frames.append(copy.deepcopy(ds))
        # 标记当前元素为红色
        frames[-1][i].set_color("r")
        # 内层循环，从已排序序列的最后一个元素开始向前比较
        for j in range(i, 0, -1):
            if ds[j].value < ds[j - 1].value:
                # 交换两个元素
                ds[j], ds[j - 1] = ds[j - 1], ds[j]
                frames.append(copy.deepcopy(ds))
                # 标记交换后的元素为红色
                frames[-1][j - 1].set_color("r")
            else:
                break
    # 将最终排序完毕的状态加入帧列表
    frames.append(ds)
    # 返回帧列表，包含排序过程中每一步的状态
    return frames
