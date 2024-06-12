import copy
from .data import Data


# 堆排序算法
def heap_sort(data_set):
    # 初始化动画帧列表
    frames = [data_set]
    ds = copy.deepcopy(data_set)
    # 构建最大堆
    for i in range(Data.data_count // 2 - 1, -1, -1):
        heap_adjust(ds, i, Data.data_count, frames)
    # 排序
    for i in range(Data.data_count - 1, 0, -1):
        ds[i], ds[0] = ds[0], ds[i]
        heap_adjust(ds, 0, i, frames)

    frames.append(ds)
    return frames


# 堆调整函数
# ds是堆数据集，head是当前需要调整的节点的索引，tail是堆的尾部索引，frames是用于存储动画帧的列表
def heap_adjust(ds, head, tail, frames):
    # 当前节点head的左孩子的索引
    i = head * 2 + 1
    while i < tail:
        # 如果右孩子存在且比左孩子大，则选择右孩子作为下一次比较的节点
        if i + 1 < tail and ds[i].value < ds[i + 1].value:
            i += 1

        # 进行帧操作，对堆中的元素进行着色，将当前节点和它的孩子节点着色
        ds_c = color(ds, tail)
        frames.append(ds_c)
        ds_c[i].set_color("k")
        ds_c[head].set_color("r")

        # 如果当前节点和它的孩子节点都满足堆的性质，则跳出循环
        if ds[i].value <= ds[head].value:
            break

        # 否则，交换当前节点和较大的孩子节点
        ds[head], ds[i] = ds[i], ds[head]

        # 再次进行帧操作，将交换后的堆状态加入帧列表
        ds_c = copy.deepcopy(ds_c)
        frames.append(ds_c)
        ds_c[head], ds_c[i] = ds_c[i], ds_c[head]
        # 更新当前节点为交换后的节点，并且继续向下调整堆
        head = i
        i = i * 2 + 1


# 着色函数
def color(ds, n):
    # 深拷贝原始数据集，避免修改原始数据
    ds_c = copy.deepcopy(ds)
    head = 0
    tail = 1
    count = 1
    depth = 0
    colors = "bmgcy"
    # 遍历堆中的每个层级
    while head < n:
        # 对当前层级的节点进行着色
        for i in range(head, min(tail, n)):
            # 根据深度选择颜色，并将节点着色
            ds_c[i].set_color(colors[depth % len(colors)])
        # 更新头部索引、计数器和尾部索引，准备着色下一层级的节点
        head = tail
        count *= 2
        tail += count
        depth += 1
    # 返回着色后的数据集
    return ds_c
