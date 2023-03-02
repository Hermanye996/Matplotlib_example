# basic_plot_add_details.py
# 设置线宽和各类标签、标题
import matplotlib.pyplot as plt  # 引入matplotlib的pyplot模块

values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(values, squares, color="blue", linestyle="dotted", marker="^", linewidth=3)  # 设置线宽
plt.title("Square number", fontsize=20)  # 设置标题，字体大小设置为20
plt.xlabel("Value", fontsize=14)  # 设置图标题x轴标签，字体大小设置为14
plt.ylabel("Square of Value", fontsize=14)  # 设置y轴标签，字体大小设置为14
plt.tick_params(axis="both")  # 设置各轴刻度为等距
plt.show()  # 展示
