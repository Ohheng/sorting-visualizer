import copy
from .data import Data


# 冒泡排序算法
def bubble_sort(data_set):
    # 初始化动画帧列表
    frames = [data_set]
    ds = copy.deepcopy(data_set)
    for i in range(Data.data_count - 1):
        # 记录当前轮次是否发生交换
        flag = False
        for j in range(Data.data_count - i - 1):
            if ds[j].value > ds[j + 1].value:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]
                flag = True
            # 添加动画帧
            frames.append(copy.deepcopy(ds))
            # 将当前交换的元素标红
            frames[-1][j + 1].set_color("r")
        # 如果当前轮次没有发生交换，说明列表已经有序，则提前退出
        if not flag:
            break
    # 将最终排序完成的数据集添加到帧列表
    frames.append(ds)
    return frames
