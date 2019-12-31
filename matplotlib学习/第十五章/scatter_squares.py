import matplotlib.pyplot as plt

#利用python循环生成数据
x = list(range(1,1001))
y = [values ** 2 for values in x]

#degecolor为每个数据点的轮廓，当点数过多时，会造成数据点之间的轮廓粘结在一起
# 指定为none，也就是删除数据点的轮廓，你将看到蓝色实心点
#c为指定数据点的颜色，可以是颜色的规范字符串也可以是RGB，c="red"/c = (0,0,0.8)
# plt.scatter(x,y,c=(0,0,0.8),edgecolor = "none",s= 40)

#cmap为颜色映射，是一系列的颜色；从用户指定的数据中从小到大的渲染颜色的浅深；c=y,就是指定数据，y较小的浅蓝色，y大的深蓝色
plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolors= "none",s=40)
plt.title("Square Number",fontsize = 24)
plt.xlabel("Values",fontsize = 14)
plt.ylabel("Square of Values",fontsize =14)

#设置每个坐标轴的范围，格式为[xmin xmax ymin ymax]
plt.axis([0,1100,0,1100000])

# plt.show()
#savefig可以保存相应的图表数据，第一个参数制定文件名称，将保存在这个脚本的文件夹下，第二个参数将图标的空白区域裁减掉
#若想保留空白，可以将这个参数进行忽略
plt.savefig("square_plot.png",bbox_inches= "tight")