# scatter_example_plot_square.py
# 画平方点图
import matplotlib.pyplot as plt
import numpy
import numpy as np

values = np.arange(1, 101)
print(values)
squares = values ** 2  # 根据values生成squares
print(squares)
plt.scatter(values, squares, color="red", s=10)  # 绘制散点图,s为点大小,color为颜色
plt.axis([0, 110, 0, 11000])  # 限制x轴和y轴的显示范围
plt.title("Square number", fontsize=20)  # 设置标题，字体大小设置为20
plt.xlabel("Value", fontsize=14)  # 设置x轴标签，字体大小设置为14
plt.ylabel("Square of Value", fontsize=14)  # 设置y轴标签，字体大小设置为14
plt.tick_params(axis="both")  # 设置各轴刻度为等距
plt.show()  # 展示
