# Matplotlib_example
example of Matplolib basic usage and animation function.
# 一、引入
Matplotlib 是一个Python的综合库，用于在 Python 中创建静态、动画和交互式可视化。
本教程包含笔者在使用Matplotlib库过程中遇到的各类完整实例与用法还有遇到的库理论问题，可以根据自己的需要在目录中查询对应的用法、实例以及第四部分关于理论的讨论。
教程参考了Eric Matthes的Python Crash Course中的Matplotlib部分和Matplotlib官方示例。
如果你希望了解更详细的用法和实例，可以查看[Matplotlib官方网站](https://matplotlib.org/)和[Python Crash Course](https://ehmatthes.github.io/pcc/)。
# 二、用法部分
## ①基础类
### 1.安装Matplotlib

```bash
sudo pip install matplotlib  # in Linux
```

### 2.引用Matplotlib常用模块

```python
import matplotlib.pyplot as plt  # 引入matplotlib的pyplot模块
```
### 3.绘制图形

```python
values = [1, 2, 3, 4, 5]  # x值列表
squares = [1, 4, 9, 16, 25]  # y值列表
plt.plot(values, squares)  # 绘图
```
### 4.查看图形

```python
plt.show()  # 打开matplotlib查看器，显示绘制的图形
```

### 5.保存图形

```python
plt.savefig("file_name.png",bbox_inches="tight")#保存文件，bbox_inches可选择是否紧凑裁剪
```

## ②调节设置类
调节设置类对于同一种功能的实现有多种方法，这就需要根据个人的需求来选择，比如复杂的项目或许适合面向对象的方法，一般的画图使用pyplot的方法或许也简单方便。
### 1.设置Figure
**设置Figure标题**
figure标题在整个figure的上部正中。
```python
fig.suptitle("figure_suptitle")  # 为Figure设置标题
```
**设置Figure尺寸大小**
```python
plt.figure(figsize=(10, 6))  # 设置figure尺寸，单位为英寸
```
### 2.设置轴Axes

**设置Axes标题**

```python
ax.set_title("title")  # 为Axes设置标题
```
**设置Axes标签**

```python
ax.set_xlabel("X", fontsize=14)  # 设置x轴标签，字体大小设置为14
ax.set_ylabel("Y")
```
**一次性设置Axes属性**
axes.set()可以同时设置轴的多个属性
```python
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]', title='This is title')
```
**隐藏坐标轴**
若对图像有洁净的追求，希望隐去坐标轴，可以使用
```python
plt.axis("off")  # 隐藏坐标轴
```
### 3.设置轴刻度
轴刻度是Axis来决定的，通过三个参数来确定一个轴的刻度，一般来说轴刻度是自动的，如果需要调节，可以参考以下用法。
#### 尺度the scale of the Axis 
线性尺度、非线性尺度等可以决定数据在y轴上的表达形式，比如log函数
当数据跨越多个数量级时，通常会使用这种办法
详细的尺度可查看[尺度教程](https://matplotlib.org/stable/gallery/scales/scales.html)
```python
ax.set_yscale('linear')
ax.set_yscale('log')
ax.set_yscale('symlog')
# https://matplotlib.org/stable/gallery/scales/scales.html
```
#### 刻度定位或格式化the tick locators & formatters
用于选择沿 Axis 对象放置刻度线的位置以及刻度的内容
详细的刻度定位和格式化可查看[刻度定位和格式化](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#tick-locators-and-formatters)

```python
ax.set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])  # 在x轴上设定0,30,60,90四个刻度并用对应文本覆盖
ax.set_yticks([-1.5, 0, 1.5])  # 在y轴上设定三个刻度
```



### 4.设置图例
图例legend是搭配label使用的，请先为点或者线添加label属性。

```python
ax.plot(x, y, label="This is label for line")  # 为axes中的线添加label
```

详细图例可参考[图例教程](https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html)
```python
ax.legend()  # 将添加过label的artists添加到四角的图例上
```
### 5.设置注释
#### 法1：text
带有markdown格式的数学文本前面需要加r字符，r表示该字符串是 原始字符串，而不是将反斜杠视为 python 转义。
```python
ax.text(x[7], y[7], r'$\theta=0.25,\sigma=15$')  # 在x[7], y[7]点描述文字
```
#### 法2：annotate [推荐]
需要注意的是：
**xy的坐标和xytext的坐标均为元组形式**
```python
ax.annotate('text', xy=(1, 2), xytext=(1.5, 2.5))  
# ax.annotate("文本",xy=(坐标),xytext=(文本坐标))
```

## ③数值处理类
### 1.生成x值和对应y值[规律]
#### 法1：range()
缺陷为生成的是list，关于list和array的讨论可以看第四章理论部分
和法3类似，法3更优
```python
values = list(range(1, 101))  # list搭配range生成多个数的列表
squares = [value ** 2 for value in values]  # 根绝values生成squares
```
#### 法2:numpy.linspace()
注:该方法引用Numpy库
```python
x = np.linspace(0, 2 * np.pi, 200)  # np.linspace(起始点，终止点，采样个数)
y = np.sin(x)
```
#### 法3:np.arange(）[推荐]
和法1类似，优势在于不用再转一次列表并且Matplotlib的输入最好为numpy的array类型
注:该方法引用Numpy库

```python
x = np.arange(0.0, 2.0, 0.01)
```

### 2.生成x值和对应y值[随机]
## ④常见图形类
### 1.生成点

```python
plt.scatter(values, squares, color="red", s=10, label="This is point")  # 绘制散点图,s为点大小,color为颜色
```
为label作格式化输出
```python
label=f'v0 = {v0} m/s'# 需要格式化的标签时，为label添加f
```

### 2.生成线
生成线的本质是生成足够多的点，使之连结，在视觉上呈现线的感觉。

```python
x = np.linspace(0, 2 * np.pi, 200)  # 生成足够多的x
y = np.sin(x)  # 生成足够多对应的y
plt.plot(x, y, color='blue', linewidth=3, linestyle='--', label="This is line")  # 绘图
```


## ⑤美化类
### 1.颜色
#### 更改线或点的颜色
对于颜色方面的美化，可以参考[Matplotlib颜色教程](https://matplotlib.org/stable/tutorials/colors/colors.html)
##### 更改点的颜色
```python
ax.scatter(x, y, s=50, facecolor='red', edgecolor='blue')
# https://matplotlib.org/stable/tutorials/colors/colors.html
```
##### 更改线的颜色
```python
ax.plot(x, y, color="red")  # 红色
```

#### 颜色映射
颜色映射可以将数值大小映射为颜色深浅，从而绘制出数值与颜色相关的图像，比如温度低的位置颜色浅，温度高的地方颜色深。
##### 法1：数值颜色映射
```python
plt.scatter(x, y, c=y, cmap="Reds")  # 颜色映射
# https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
```
如果按照点的先后顺序颜色映射，需要先为规则c生成数值列表
##### 法2：顺序颜色映射
```python
points_number = list(range(101))  # 生成0~100的cmap顺序列表
plt.scatter(x, y, c=points_number, cmap="Blues", s=5)  # 按照顺序颜色映射
```


### 2.线型、线宽、线标记 
#### 常见线型
详细线型可参考[线型教程](https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html)

```python
ax.plot(x, y, linestyle="solid")  # 默认为实线
ax.plot(x, y, linestyle="dotted")  # 点线
ax.plot(x, y, linestyle="dashed")  # 虚线
ax.plot(x, y, linestyle="dashdot")  # 点划线
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
```
#### 常见线宽

```python
ax.plot(x, y, linewidth=3)  # 线宽设置为3
```


#### 常见线标记
详细线标记可参考[线标记教程](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers)

```python
ax.plot(x, y, marker="^")  # 向上三角形
ax.plot(x, y, marker="s")  # 正方形
ax.plot(x, y, marker="o")  # 圆形
# https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
```
### 3.轴的美化
#### 使轴刻度相等[推荐]
当axis参数为both时，x轴、y轴的刻度相同
which默认为major，也就是大刻度，如果需要小刻度也遵循，可在which填入both
```python
plt.tick_params(axis="both", which="both", labelsize=14)  # 设置各轴刻度为等距,标签大小设置为14
```
## ⑥动画类
animation.FuncAnimation()允许我们通过传递一个迭代修改绘图数据的函数来创建动画。
```python
import matplotlib.animation as animation  # 引入动画库
import matplotlib.pyplot as plt
import numpy as np
```
### 创建一个动画
创建一个动画的基本步骤是：

1. 创建x、y数组，并将动画所有状态的点位保存在数组变量里，方便之后调用。

```python
frame=100  #动画总帧数
theta = np.linspace(0, 2 * np.pi, frame)  # 创建x
y = np.sin(theta)  # 创建y
```

2. 绘制t=0状态下的图形，并将关键参数变量声明出来，它们是决定动画迭代的关键参数变量。
以下的scatter_example和line_example分别是点类型和线类型的关键参数变量
**注意：线类型的关键变量为线对象的第[0]内容，所以要在线对象的后面加[0]**

```python
scatter_example = ax.scatter(theta[0], y_scatter[0], color="blue", s=5, label="Cos")
line_example = ax.plot(theta[0], y_line[0], color="red", label="Sin")[0]  # 警告：此处[0]不可省去！
```
3. 写更新函数，在更新函数中处理该帧要画的数据，并通过点的set_offsets()和线的set_xdata()方法将迭代用的关键变量回传

```python
def update(frame):
    # 对于每个帧frame，更新这帧frame要画的数据，存于x、y中
    print(frame)
    x = theta[:frame]
    y = y_scatter[:frame]
    # 更新scatter绘画:
    data_scatter = np.stack([x, y]).T  # 此处将xy拼在一起并转置，形成xy坐标为一组，总共frame组坐标数据的list
    scatter_example.set_offsets(data_scatter)  # 通过set_offsets()更新artist的数据

    # 更新line绘画:
    line_example.set_xdata(theta[:frame])  # 直接设置x
    line_example.set_ydata(y_line[:frame])  # 直接设置y
    return scatter_example, line_example
```

4. 创建FuncAnimation()对象

```python
ani = animation.FuncAnimation(fig=fig, func=更新函数, frames=帧个数, interval=每帧间隔时间ms, blit=是否使用光栅技术加速渲染) 
```

```python
ani = animation.FuncAnimation(fig=fig, func=update, frames=frame, interval=10, blit=True)  # 设置动画，interval单位为ms
# 默认渲染最高帧率为33fps左右，blit=True启用一种光栅技术加快渲染，使之达到200+fps
```
创建动画的完整代码在实例部分，演示了线或者点创建出Sin/Cos完整动画的全过程，你可以参考这个代码来体会动画的创建。

# 三、实例部分
实例部分提供了一些基础的具有详细注释的简单例子，还有有一些有趣的小项目，比如点的随机漫步图、Sin函数动画等，你可以在github或gitee上下载代码：


# 四、理论部分
## 1.Artist、Figure、Axes、Axis的区别
### Artist
基本上，图形上可见的所有内容都是Artist，包括Figure、Axes和Axis对象。
Text对象、Line2D对象、collections对象、Patch 对象等也是Artist。
当 Figure 被渲染时，所有的 Artists 都被绘制到画布上。
大多数Artist和Axes挂钩，不能在Axes间切换也不能被Axes共享。
### Figure
Figure是整个图形，可以看做窗口，一个Figure可以包含多个Axes。
Figure可以用pyplot.figure()单独创建
```python
fig = plt.figure()  # 创建无Axes的空Figure窗口
```

```python
fig, ax = plt.subplots()  # 创建带有一个Axes的Figure
```

Figure也可以用pyplot.subplots()和Axes一起创建。
### Axes
Axes 是附加到 Figure 的 Artist，它包含一个用于绘制数据的区域。
Axes通常用pyplot.subplots()和Figure一起创建。
使用axes_name.plot()来绘制数据
```python
fig, ax = plt.subplots()  # 创建带有一个Axes的Figure
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # 在Axes上绘制数据
```
一个Figure上可以有多个Axes。
```python
fig, axs = plt.subplots(2, 2)  # 创建一个带有2X2个Axes的Figure
axs[1][1].plot(x, y)  # 在第二行第二列的图上绘制
```

```python
fig, (ax1, ax2,ax3,ax4) = plt.subplots(1, 4, figsize=(10, 4))  # 创建带有4个axes的figure
```

### Axis
一个Axes通常包含两个带有刻度和刻度标签Axis，在3D情况下，一个Axes包含3个Axis，这和我们日常生活中的xyz坐标系含有x、y、z轴是相同的概念。
## 2.输入数据的要求
Matplotlib要求输入的数据格式为numpy的array，也就是numpy数组。
### List与Array区别
list是python的内置数据类型，而 array数组需要导入numpy库，不属于内置类型。
 list中的数据类不必相同的，即每个元素可以是不同的数据类型。
 而array则是由numpy封装，存放的元素都是相同的数据类型。
### Matrix的输入
 
矩阵Matrix无法直接作为数据输入，需要先通过numpy.asarray()转化为"类数组"才能输入Matplotlib
```python
a = np.matrix([[1, 2], [3, 4]])  # a为numpy矩阵Matrix
a_asarray = np.asarray(a)  # a转化为类数组a_asarray
```
## 3.内存的占用问题
清理选定的Figure

```python
fig.clf()
```
清理选定的Axes

```python
ax.cla()
```
当制作动画或者大量图形时，需要注意，图形所需的内存在使用plt.close()图形前不会完全释放。
**即使关闭图窗、删除图形也没有用，因为pyplot会维护内部的引用直到plt.close被调用。**
ax和fig没有close用法，只有plt.close()，其针对的关闭对象为最后一个figure

```python
plt.close(figure_number)  # 如果有多个figure，不输入默认关闭最后一个，也可选择关闭某个figure
```
可能良好的习惯是在show之后close所有的figures

```python
plt.show()
plt.close("all")
```

