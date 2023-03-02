from class_random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk(50000)  # 实例化
rw.walk_calculate()  # 计算漫步的坐标列表
points_number = list(range(rw.number_points))  # 生成cmap顺序列表
plt.figure(figsize=(10, 6))  # 设置figure大小，单位为英寸
plt.scatter(rw.x, rw.y, c=points_number, cmap="Blues", s=1)  # 按照顺序颜色映射
plt.scatter(rw.x[0], rw.y[0], color="red", s=50)  # 突出漫步的起点
plt.scatter(rw.x[-1], rw.y[-1], color="green", s=50)  # 突出漫步的终点
plt.axis("off")  # 隐藏坐标轴

plt.show()
