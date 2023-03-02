# basic_plot_line_example.py
# 绘制1~5的平方
import matplotlib.pyplot as plt  # 引入matplotlib的pyplot模块

values = [1, 2, 3, 4, 5]  # x值列表
squares = [1, 4, 9, 16, 25]  # y值列表
plt.plot(values, squares)  # 绘图
plt.show()  # 打开matplotlib查看器，显示绘制的图形
