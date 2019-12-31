import pygal
from random_walk import RandomWalk

randomWalk = RandomWalk()
randomWalk.walk()
x = randomWalk.x
y = randomWalk.y
length = len(x)
#实例化一个Bar类
hist = pygal.XY(stroke = False)

point = [(x[index],y[index]) for index in range(length)]
hist.add("point",point)
hist.title ="Random Walk"
hist.render_to_file("walk.svg")

# 初学者可能会使用如下方法使用字典，这样做忽视了字典中key值唯一不重复的特性，丢失了很多点
#
# # 创建坐标点字典
# point = {}
# for i in range(rw.num_points):
#     point[rw.x_values[i]] = rw.y_values[i]
#     # 列表解析 key,value迭代
# xy_chart.add('A', [(x, y) for x, y in point.items()])
# 以下代码同一key值对应多个value值，不存在丢失点的情况
#
# from collections import OrderedDict
#
# # 创建坐标点字典
# point = OrderedDict()
# for i in range(rw.num_points):
#     point[i] = (rw.x_values[i], rw.y_values[i])
#
# # 列表解析 key,value迭代
# xy_chart.add('A', [(x, y) for x, y in point.values()])
#
# 这里使用OrederedDict类仅表示我们不仅重视键值对的对应关系，还重视键值对的添加（生成）顺序，对随机漫步点图的生成无影响
# 如果要生成路径图，必须使用OrederedDict类
