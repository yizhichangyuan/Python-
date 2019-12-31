import csv
import matplotlib.pyplot as plt
from datetime import datetime

#向csv.reader传递一个文件对象，从而创建一个与该文件相关的reader对象
#csv中包括next()函数，调用他时，传递一个reader对象，总返回文件的下一行，返回的数据格式是以逗号分隔后的数据列表
fileName = 'death_valley_2018_simple.csv'
with open(fileName) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # #enumerate为列表中的每一个数据添加一个index
    # for index,item in enumerate(header_row):
    #     print(index,item)


    #文件指针移动到第二行，从第二行开始提取最高气温,以及日期
    #日期在csv文件中是一个字符串，所以应该转化为一个表示日期的对象
    #第二个参数为设置日期的格式,要与字符串日期格式匹配
    highs,dates,lows = [],[],[]
    for row in reader:
        try:
            date = datetime.strptime(row[2],'%Y-%m-%d')
            high = int(row[5])
            low =int(row[6])
        except ValueError:
            print(date,"missing data")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)


    print(highs)
    print(dates)

#绘制最高气温折线图
#指定窗口大小及分辨率
fig = plt.figure(dpi = 128,figsize=(10,6))

#alpha表示着色深浅程度，1最深，0最浅
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)

#使用fill_between传递一个x系列，两个y系列，fill_between将填充指定的x系列间的两个y系列区域的颜色
plt.fill_between(dates,lows,highs,facecolor="blue",alpha=0.1)


plt.title("Daily High And Low Temperatures-2014",fontsize=24)
plt.xlabel("Date",fontsize=14)

#调用fig.autofmt_xdate使得横坐标的日期标签避免重叠
fig.autofmt_xdate()
plt.ylabel("High Temperature",fontsize = 14)
plt.tick_params(axis="both",which="major",labelsize=16)
#更改y刻度范围
plt.ylim(10,120)

plt.show()




