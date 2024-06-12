import copy
from .data import Data


# 归并排序算法
def merge_sort(data_set):
    # 初始化帧列表，将原始数据集作为第一个帧
    frames = [data_set]
    # 深拷贝数据集，确保不修改原始数据
    ds = copy.deepcopy(data_set)
    # 调用递归函数对数据集进行归并排序，并记录动画帧
    split_merge(ds, 0, Data.data_count, frames)
    # 将最终排序完成的数据集加入动画帧列表
    frames.append(ds)
    # 返回所有动画帧，以便可视化展示排序过程
    return frames


""" 
ds：当前数据集。
head：子序列的起始索引。
tail：子序列的结束索引。
frames：动画帧列表。 
"""


def split_merge(ds, head, tail, frames):
    # 计算中间位置
    mid = (head + tail) // 2

    # 如果当前子序列长度大于2，则继续分割并递归调用split_merge函数
    if tail - head > 2:
        split_merge(ds, head, mid, frames)
        split_merge(ds, mid, tail, frames)

    # 创建当前分割区域的副本，并对副本中的元素进行着色
    ds_yb = copy.deepcopy(ds)
    for i in range(head, mid):
        ds_yb[i].set_color("y")  # 设置左半部分元素为黄色
    for i in range(mid, tail):
        ds_yb[i].set_color("b")  # 设置右半部分元素为蓝色

    # 合并操作
    left = head
    right = mid
    tmp_list = []  # 临时列表用于存放合并后的结果
    for i in range(head, tail):
        # 将当前状态加入动画帧列表
        frames.append(copy.deepcopy(ds_yb))
        # 如果右半部分遍历结束或者左半部分的元素小于等于右半部分的元素，则将左半部分的元素加入临时列表
        if right == tail or (left < mid and ds[left].value <= ds[right].value):
            tmp_list.append(ds[left])
            # 设置加入临时列表的元素为红色，表示该元素已经被选取
            frames[-1][left].set_color("r")
            left += 1
        # 否则将右半部分的元素加入临时列表
        else:
            tmp_list.append(ds[right])
            # 设置加入临时列表的元素为红色，表示该元素已经被选取
            frames[-1][right].set_color("r")
            right += 1
    # 将临时列表中的元素复制回原始列表中的相应位置
    for i in range(head, tail):
        ds[i] = tmp_list[i - head]
    # 将合并后的结果加入动画帧列表
    frames.append(copy.deepcopy(ds))
