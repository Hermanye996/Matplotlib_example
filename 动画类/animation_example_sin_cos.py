# animation_example_sin_cos.py
# 以sin和cos为例制作点和线的动画
import matplotlib.animation as animation  # 引入动画库
import matplotlib.pyplot as plt
import numpy as np


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


plot_delta = 0.1  # 画图修正系数，可忽略
frame = 100  # 一轮总帧数
fig, ax = plt.subplots()  # 创建图形
theta = np.linspace(0, 2 * np.pi, frame)  # 创建x

y_line = np.sin(theta)  # 创建线的y
y_scatter = np.cos(theta)  # 创建点的y

scatter_example = ax.scatter(theta[0], y_scatter[0], color="blue", s=5, label="Cos")
line_example = ax.plot(theta[0], y_line[0], color="red", label="Sin")[0]  # 警告：此处[0]不可省去！

ax.set(xlim=[0 - plot_delta, 2 * np.pi + plot_delta], ylim=[-1 - plot_delta, 1 + plot_delta],
       xlabel='Theta [radian]', ylabel='Value', title="Scatter / Line Animation Plot Test")  # 设置xy限制范围和标签
ax.legend(loc="lower left")  # 设置图例

ani = animation.FuncAnimation(fig=fig, func=update, frames=frame, interval=0, blit=True)  # 设置动画，interval单位为ms
# 默认渲染最高帧率为33fps左右，blit=True启用一种光栅技术加快渲染，使之达到200+fps
plt.show()
