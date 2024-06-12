# sorting-visualizer

运行如下命令调用所有函数:

```
python output.py arg1 [arg2 [arg3]]  
```

**参数详情：**

参数1

- `play`：在新窗口中播放特定排序算法或所有算法的动画，作为Matplotlib的“图形”。
- `save-html`：将动画保存为一系列图像的HTML页面。
- `save-mp4`：将动画保存为MP4视频。

参数2

- `all` (默认)：在动画中显示所有排序算法的可视化。
- `bubble-sort`：仅在动画中显示冒泡排序算法的可视化。
- `heap-sort`: 仅在动画中显示堆排序算法的可视化。
- `merge-sort`: 仅在动画中显示归并排序算法的可视化。
- `insertion-sort`: 仅在动画中显示直接插入排序算法的可视化。
- `selection-sort`: 仅在动画中显示选择排序算法的可视化。
- `quick-sort`: 仅在动画中显示快速排序算法的可视化。

参数3

- `random` (默认)：对随机序列进行排序。

- `almost-sorted`：对几乎已排序的序列进行排序。
- `few-unique`：对一些部分重复的序列进行排序。
- `reversed`：对降序序列进行排序。

**示例**

要创建一个新窗口播放堆排序算法动画，初始序列为降序排列，可以运行：

```
python output.py play heap-sort reversed
```

## 