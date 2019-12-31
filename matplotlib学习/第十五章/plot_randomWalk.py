import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    """模拟多次随机漫步，直到用户输入n结束"""
    randomWalk = RandomWalk()
    randomWalk.walk()

    x = randomWalk.x
    y = randomWalk.y
    number_point = list(range(randomWalk.number_point))

    #指定图表的分辨率以及窗口大小尺寸，其中figsize为一个元组，单位为英寸，80像素/英寸；还可以指定背景色facecolor
    plt.figure(dpi = 128,figsize = (10,6))

    #为根据漫步中各点的先后顺序进行着色，我们传递参数c，并将其设置为一个列表，其中包含各点的先后顺序。
    plt.scatter(x,y,c=number_point,cmap=plt.cm.Blues,edgecolors = "none",s = 1)

    #给随机漫步的开始点以及结束点着色,并使得开始点和结束点大小放大，以突出他们
    plt.scatter(x[0],y[0],c="green",edgecolors="none",s=50)
    plt.scatter(x[-1],y[-1],c='red',edgecolors="none",s=50)

    #隐藏横纵坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    #设置图表的标题，横纵坐标轴的标签，以及刻度标记
    plt.title("Random Walk",fontsize = 24)
    plt.xlabel("x_values",fontsize =14)
    plt.ylabel("y_values",fontsize = 14)
    plt.tick_params(axis = "both",labelsize = 14)

    plt.show()

    keep_running = input("make running again？(y/n)")
    if keep_running == "n":
        break
