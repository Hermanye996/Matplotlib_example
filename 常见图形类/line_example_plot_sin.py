# line_example_plot_sin.py
# 绘制sin函数图像
import matplotlib.pyplot as plt  # 引入matplotlib的pyplot模块
import numpy as np  # 引用numpy数学库

x = np.linspace(0, 2 * np.pi, 200)  # 生成x
y = np.sin(x)

fig, ax = plt.subplots()  # 创建figure同时创建一个axes
ax.plot(x, y)  # 在这个axes上绘图
plt.show()
