import random

class RandomWalk():
    """产生随机漫步点的类"""
    def __init__(self,number_point=5000):
        #初始化随机漫步属性
        self.number_point = number_point

        #所有随机漫步都始于点（0，0）
        self.x = [0]
        self.y = [0]

    def get_step(self):
        """计算产生移动的方向和距离"""
        self.direction = random.choice([-1,1])
        self.distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.step = self.direction * self.distance

        return self.step
    def walk(self):
        """计算随机漫步产生的点"""

        #不断漫步，直到达到指定长度
        while True:
            if len(self.x) < self.number_point:
                #获取x,y移动的方向以及距离
                self.x_step = self.get_step()
                self.y_step = self.get_step()

                #不允许原地踏步
                if self.x_step == 0 and self.y_step ==0:
                    continue

                #计算下一个点的位置
                self.x_walk = self.x[-1] + self.x_step
                self.y_walk = self.y[-1] + self.y_step

                self.x.append(self.x_walk)
                self.y.append(self.y_walk)
            else:
                break

