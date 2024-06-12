import copy
from .data import Data


# 快速排序算法
def quick_sort(data_set):
    # 初始化一个帧列表，用于存储排序过程中每一步的状态
    frames = [data_set]

    # 深拷贝数据集，确保后续操作不改变原始数据
    ds = copy.deepcopy(data_set)
    # 调用快速排序函数，对数据集进行排序
    qsort(ds, 0, Data.data_count, frames)

    # 将最终排序完毕的状态加入帧列表，返回
    frames.append(ds)
    return frames


def qsort(ds, head, tail, frames):
    # 当待排序的部分长度大于1时，进行快速排序
    if tail - head > 1:
        # 复制当前状态并将范围内的元素标记为黄色
        ds_y = copy.deepcopy(ds)
        for i in range(head, tail):
            ds_y[i].set_color("y")

        # 初始化左右指针和基准值
        i = head
        j = tail - 1
        pivot = ds[j].value

        while i < j:
            # 将当前状态的深拷贝加入帧列表
            frames.append(copy.deepcopy(ds_y))
            frames[-1][i if ds[i].value == pivot else j].set_color("r")
            frames[-1][j if ds[i].value == pivot else i].set_color("k")

            # 比较并交换元素位置
            if ds[i].value > pivot or ds[j].value < pivot:
                ds[i], ds[j] = ds[j], ds[i]
                # 同步更新ds_y并加入帧列表
                ds_y[i], ds_y[j] = ds_y[j], ds_y[i]
                frames.append(copy.deepcopy(ds_y))
                frames[-1][i if ds[i].value == pivot else j].set_color("r")
                frames[-1][j if ds[i].value == pivot else i].set_color("k")

            # 根据基准值移动指针
            if ds[i].value == pivot:
                j -= 1
            else:
                i += 1

        # 递归调用快速排序函数，对分割后的两个子部分进行排序
        qsort(ds, head, i, frames)
        qsort(ds, i + 1, tail, frames)
