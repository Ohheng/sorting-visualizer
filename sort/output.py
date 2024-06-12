import random
import os
import sys
import re
from matplotlib import pyplot as plt
from matplotlib import animation
from sorting.data import Data
from sorting.bubblesort import bubble_sort
from sorting.mergesort import merge_sort
from sorting.heapsort import heap_sort
from sorting.quicksort import quick_sort
from sorting.selectionsort import selection_sort
from sorting.insertionsort import insertion_sort

# 存储排序算法的名称和对应索引.
# 其中键是排序算法的名称，值是排序算法的索引
stype_dic = {
    "all": -1,
    "merge-sort": 0,
    "heap-sort": 1,
    "bubble-sort": 2,
    "quick-sort": 3,
    "selection-sort": 4,
    "insertion-sort": 5,
}

# 存储排序算法的标题及其时间复杂度
titles = [
    r"Merge Sort ($O(n \cdot log_2(n))$)",
    r"Heap Sort ($O(n \cdot log_2(n))$)",
    r"Bubble Sort ($O(n^2)$)",
    r"Quick Sort ($O(n \cdot log_2(n))$)",
    r"Selection Sort ($O(n^2)$)",
    r"Insertion Sort ($O(n^2)$)",
]

# 存储排序算法函数的列表
# 按照 stype_dic 中的索引顺序排列，通过索引快速获取到对应的排序算法函数，方便在代码中调用不同的排序算法
funs = [
    merge_sort,
    heap_sort,
    bubble_sort,
    quick_sort,
    selection_sort,
    insertion_sort,
]


# 创建原始数据，并返回一个列表
def create_original_data(dtype):
    data = []
    if dtype == "random":  # 对随机序列进行排序
        # 生成一个包含从1到Data.data_count的整数的列表
        data = list(range(1, Data.data_count + 1))
        # 随机打乱这个列表
        random.shuffle(data)

    elif dtype == "reversed":  # 按降序排序
        # 从 Data.data_count 到 1 的整数列表，步长为-1。这样生成的列表就是一个降序排列的整数序列
        data = list(range(Data.data_count, 0, -1))

    elif dtype == "few-unique":  # 对一些部分重复的序列进行排序
        d = Data.data_count // 4
        for i in range(0, d):
            data.append(d)
        for i in range(d, d * 2):
            data.append(d * 2)
        for i in range(d * 2, d * 3):
            data.append(d * 3)
        for i in range(d * 3, Data.data_count):
            data.append(Data.data_count)
        random.shuffle(data)

    elif dtype == "almost-sorted":  # 对几乎已排序的序列进行排序
        data = list(range(1, Data.data_count + 1))
        a = random.randint(0, Data.data_count - 1)
        b = random.randint(0, Data.data_count - 1)
        while a == b:
            b = random.randint(0, Data.data_count - 1)
        data[a], data[b] = data[b], data[a]
    return data


# 根据指定的排序算法类型和原始数据生成动态图表
# stype 排序算法的类型
# original_data 原始数据
# frame_interval 动画帧之间的间隔时间
def draw_chart(stype, original_data, frame_interval):
    # 创建一个新的图表，编号为1，尺寸为16:9.
    fig = plt.figure(1, figsize=(16, 9))
    # 原始数据列表转换为 Data 对象的列表，其中每个 Data 对象表示一个数据点
    data_set = [Data(d) for d in original_data]
    # 添加一个子图到图表中，并指定其位置为 1x1 网格中的第 1 个
    axs = fig.add_subplot(111)
    # 设置子图的 x 和 y 轴刻度为空，即不显示坐标轴
    axs.set_xticks([])
    axs.set_yticks([])
    # 调整子图的位置和间距，以便在图表中显示动画
    plt.subplots_adjust(
        left=0.01, bottom=0.02, right=0.99, top=0.95, wspace=0.05, hspace=0.15
    )

    # 调用指定排序算法的函数，对原始数据进行排序，并将排序过程的每一步保存在 frames 列表中
    frames = funs[stype](data_set)

    # 打印排序算法的名称以及动画帧的总数
    print("%s: %d frames." % (re.findall(r"\w+ Sort", titles[stype])[0], len(frames)))

    # 定义动画函数，fi 当前帧的编号.
    def animate(fi):
        # 存储柱状图的图形对象的列表
        bars = []
        if len(frames) > fi:  # 确保当前帧的编号 fi 不超过总帧数，以避免越界访问
            # 清除当前子图的内容，以便绘制新的帧
            axs.cla()
            # 设置子图的标题为排序算法的名称
            axs.set_title(titles[stype])
            # 设置子图的 x 和 y 轴刻度为空，即不显示坐标轴
            axs.set_xticks([])
            axs.set_yticks([])
            # 绘制当前帧的柱状图
            bars += axs.bar(
                list(range(Data.data_count)),  # x 轴数据，即数据点的索引
                [d.value for d in frames[fi]],  # y 轴数据，即当前帧的数据点的值
                1,  # 柱形的宽度
                color=[
                    d.color for d in frames[fi]
                ],  # 柱形的颜色，根据当前帧的数据点的颜色
            ).get_children()

        return bars

    # 创建动画对象，并指定图表、动画函数、帧数和帧之间的间隔时间。
    anim = animation.FuncAnimation(
        fig, animate, frames=len(frames), interval=frame_interval
    )
    # 返回绘图对象 plt 和动画对象 anim
    return plt, anim


# 生成包含所有排序算法动态图表的图表
def draw_all_charts(original_data, frame_interval):
    # 存储子图对象的列表
    axs = []
    # 存储每种排序算法的所有帧的列表
    frames = []
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    # 循环6次，对于每种排序算法，创建一个子图对象，并设置其属性
    for i in range(6):
        axs.append(fig.add_subplot(331 + i))
        axs[-1].set_xticks([])
        axs[-1].set_yticks([])
    plt.subplots_adjust(
        left=0.01, bottom=0.02, right=0.99, top=0.95, wspace=0.05, hspace=0.15
    )

    # 对于前6种排序算法，获取其所有帧的数据并添加到 frames 列表中
    for i in range(6):
        frames.append(funs[i](data_set))
    # 对于最后一种排序算法（Monkey Sort），其帧数比其他算法的帧数多50，添加到 frames 列表中
    # frames.append(funs[8](data_set, max(len(f) for f in frames) + 50))

    names = []
    max_name_length = 0
    frame_counts = []
    max_frame_length = 0
    for i in range(6):
        names.append(re.findall(r"\w+ Sort", titles[i])[0] + ":")
        if len(names[-1]) > max_name_length:
            max_name_length = len(names[-1])
        frame_counts.append(len(frames[i]))
        if len(str(frame_counts[-1])) > max_frame_length:
            max_frame_length = len(str(frame_counts[-1]))
    for i in range(6):
        print(
            "%-*s %*d frames"
            % (max_name_length, names[i], max_frame_length, frame_counts[i])
        )

    # 定义动画函数，它会在每一帧被调用
    def animate(fi):
        # 存储柱状图的图形对象的列表
        bars = []
        # 遍历每种排序算法对应的子图
        for i in range(6):
            if len(frames[i]) > fi:
                axs[i].cla()
                axs[i].set_title(titles[i])
                axs[i].set_xticks([])
                axs[i].set_yticks([])
                bars += (
                    axs[i]
                    .bar(
                        list(range(Data.data_count)),  # X
                        [d.value for d in frames[i][fi]],  # data
                        1,  # width
                        color=[d.color for d in frames[i][fi]],  # color
                    )
                    .get_children()
                )
        return bars

    # 绘制当前帧的柱状图，并将返回的柱形对象添加到 bars 列表中
    anim = animation.FuncAnimation(
        fig, animate, frames=max(len(f) for f in frames), interval=frame_interval
    )
    return plt, anim


if __name__ == "__main__":
    try:
        Data.data_count = int(
            input("Please set the number of items to be sorted(32): ")
        )
    except:
        Data.data_count = 32  # 默认值为 32
    if len(sys.argv) > 1:  # 检查命令行参数的数量是否大于1
        stype = -1  # 默认值为 -1，表示不使用任何排序算法
        # 检查命令行参数的数量是否大于2，如果是，则表示用户提供了第三个参数，用于指定排序算法类型
        if len(sys.argv) > 2:
            # 此条件检查第三个参数是否在 stype_dic 字典中，即检查用户提供的排序算法类型是否合法
            if sys.argv[2] in stype_dic:
                stype = stype_dic[sys.argv[2]]
            else:
                print("Error: Wrong argument!")
                exit()
        # 将确定的排序算法类型索引值转换为相应的排序算法名称
        stype_str = list(stype_dic.keys())[list(stype_dic.values()).index(stype)]

        # 生成原始数据.
        dtype = "random"  # 默认使用随机序列
        if len(sys.argv) > 3:
            dtype = sys.argv[3]
            if dtype not in ("random", "reversed", "few-unique", "almost-sorted"):
                print("Error: Wrong argument!")
                exit()
        od = create_original_data(dtype)

        # 绘制动画并显示
        if sys.argv[1] == "play":
            try:
                fi = int(input("Please set the frame interval(100): "))
            except:
                fi = 100
                # 如果 stype 的值为 -1，表示用户选择了 "all"，则调用 draw_all_charts 函数，以绘制所有排序算法的动画。
                # 否则，调用 draw_chart 函数，以绘制指定排序算法的动画
            plt, _ = (
                draw_all_charts(od, fi) if stype == -1 else draw_chart(stype, od, fi)
            )
            plt.show()

        # 绘制动画并保存为MP4格式文件
        elif sys.argv[1] == "save-mp4":
            # 创建默认的文件名，包含排序算法和数据类型的信息
            default_fn = stype_str + "-" + dtype + "-animation"
            fn = input("Please input a filename(%s): " % default_fn)
            if fn == "":
                fn = default_fn
            try:
                fps = int(input("Please set the fps(25): "))
            except:
                fps = 25
            _, anim = (
                draw_all_charts(od, 100) if stype == -1 else draw_chart(stype, od, 100)
            )
            print("Please wait...")
            # 将动画保存为 mp4 文件。采用了 FFMpegWriter 类来将动画帧转换为视频文件
            anim.save(
                fn + ".mp4",
                writer=animation.FFMpegWriter(
                    fps=fps, extra_args=["-vcodec", "libx264"]
                ),
            )
            # 提示用户文件保存成功的消息，并显示保存的文件路径
            print(
                "The file has been successfully saved in %s"
                % os.path.abspath(fn + ".mp4")
            )

        # 绘制动画并保存为HTML文件
        elif sys.argv[1] == "save-html":
            default_fn = stype_str + "-" + dtype + "-animation"
            fn = input("Please input a filename(%s): " % default_fn)
            if fn == "":
                fn = default_fn
            try:
                fps = int(input("Please set the fps(25): "))
            except:
                fps = 25
            _, anim = (
                draw_all_charts(od, 100) if stype == -1 else draw_chart(stype, od, 100)
            )
            print("Please wait...")
            anim.save(fn + ".html", writer=animation.HTMLWriter(fps=fps))
            print(
                "The file has been successfully saved in %s"
                % os.path.abspath(fn + ".html")
            )
