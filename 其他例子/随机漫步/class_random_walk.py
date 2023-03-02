from random import choice  # random.choice用于在参数列表中随机选择一个数


class RandomWalk:
    """
    计算随机漫步的点位
    """

    def __init__(self, number_points=5000):
        self.number_points = number_points  # 漫步次数
        self.x = [0]  # 从(0, 0）开始随机漫步
        self.y = [0]

    def walk_calculate(self):
        while len(self.x) < self.number_points:
            # for x
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            # for y
            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # filter
            if x_step == 0 and y_step == 0:
                continue  # 跳出本次循环，不再执行后续步骤
            # for next
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step
            # append
            self.x.append(next_x)
            self.y.append(next_y)
