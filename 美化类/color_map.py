# color_map.py
# 颜色映射，温度高的地方颜色深，温度低的地方颜色浅
import matplotlib.pyplot as plt
import numpy as np

places = np.arange(1, 101)
temperature = places ** 2  # 根据places生成temperature，假设关系为平方
plt.scatter(places, temperature, c=temperature, cmap="Reds", s=10)  # 颜色映射
# https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
plt.axis([0, 110, 0, 110 ** 2])  # 设置xy轴的可视范围
plt.title("Temperature of Places", fontsize=20)  # 设置标题
plt.xlabel("Places", fontsize=14)  # 设置x轴标签
plt.ylabel("Temperature", fontsize=14)  # 设置y轴标签
plt.tick_params(axis="both", labelsize=14)  # 设置各轴刻度为等距
plt.show()  # 展示
