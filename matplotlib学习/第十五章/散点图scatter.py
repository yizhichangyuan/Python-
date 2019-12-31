import matplotlib.pyplot as plt

#绘制散点图，绘制一个点,s代表点的大小
plt.scatter(2,4,s=200)

plt.title("Square Number",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize =14)

#which代表什么
plt.tick_params(axis = "both",which = "major",labelsize = 14)

plt.show()


#scatter绘制一系列点
x = [1,2,3,4]
y = [1,2,3,4]

plt.scatter(x,y,s=200)

plt.title("Square Number",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)

plt.tick_params(axis = "both",which = "major",labelsize = 14)

plt.show()