import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#指定折线宽度，颜色，节点用点表示，线型为虚线，在不设置x情况下，x为0-N-1
plt.plot(input_values,squares,linewidth = 5,color = "green",marker = "o",linestyle = "dashed")
#设置图表的字体以及名称
plt.title("Square Numbers",fontsize = 24)
#设置坐标轴的标签
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of values",fontsize = 14)
#形成网格，可选项
plt.grid()
#both指定相应的标签应用在x轴和y轴，刻度的字体大小为14
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()