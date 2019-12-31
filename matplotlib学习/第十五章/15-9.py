from die import Die
import pygal
"""统计并可视化两个筛子点数相乘的结果"""
#创建一个D6,一个D6
die_1 = Die()
die_2 = Die()

#摇色子，将结果保存在列表里
#使用列表解析代替for循环
results = [die_1.roll() * die_2.roll() for roll_num in range(50000)]
# results = []
# for roll_num in range(50000):
#     result1 = die_1.roll()
#     result2 = die_2.roll()
#     results.append(result1 + result2)

#统计各个点数出现的次数，保存在一个列表里,用到列表count统计次数
max_result = die_1.num_sides * die_2.num_sides

#计算两筛子数相乘的结果，使用set避免重复项
def plus():
    plus_result = set()
    for x in range(1, die_1.num_sides+1):
        for y in range(1, die_2.num_sides+1):
           plus_result.add(x*y)
    return sorted(plus_result)

#使用列表解析代替for循环
frequencies = [results.count(value) for value in plus()]
# frequencies = []
# for value in range(2,max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times"

hist.x_labels = map(str,plus())
#hist.x_labels = [str(x) for x in range(2,max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#第一个参数为标签名，第二个参数为对应x_label的每个值
hist.add("D6 + D6",frequencies)

#此文件用浏览器打开，有一定的交互性
hist.render_to_file("die_visual_点数相乘.svg")