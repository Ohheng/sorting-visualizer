# sorting-visualizer

运行如下命令调用所有函数:

```powershell
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

- 冒泡算法对降序序列排序

```powershell
  python output.py play bubble-sort reversed  
```

| 排序前                                           | 排序后                                           |
| ------------------------------------------------ | ------------------------------------------------ |
| ![img](http://cdn.ohheng.cn/202406121809579.jpg) | ![img](http://cdn.ohheng.cn/202406121809596.jpg) |

 

- 堆排序算法对随机序列排序

```powershell
  python output.py play heap-sort  
```

| 排序前                                           | 排序后                                           |
| ------------------------------------------------ | ------------------------------------------------ |
| ![img](http://cdn.ohheng.cn/202406121809589.jpg) | ![img](http://cdn.ohheng.cn/202406121809598.jpg) |

 

-  归并排序算法对一些部分重复的序列排序

```powershell
  python output.py play merge-sort few-unique  
```

| 排序前                                           | 排序后                                           |
| ------------------------------------------------ | ------------------------------------------------ |
| ![img](http://cdn.ohheng.cn/202406121809603.jpg) | ![img](http://cdn.ohheng.cn/202406121809607.jpg) |

 

- 直接插入排序算法对几乎已排序的序列排序

```powershell
  python output.py play insertion-sort  almost-sorted     
```

| 排序前                                                       | 排序后                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![img](C:/Users/12994/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg) | ![img](C:/Users/12994/AppData/Local/Temp/msohtmlclip1/01/clip_image016.jpg) |

 

- 所有排序算法对随机的序列排序

```powershell
  python output.py play     
```

| 排序前                                           | 排序后                                                       |
| ------------------------------------------------ | ------------------------------------------------------------ |
| ![img](http://cdn.ohheng.cn/202406121809141.jpg) | ![img](C:/Users/12994/AppData/Local/Temp/msohtmlclip1/01/clip_image020.jpg) |