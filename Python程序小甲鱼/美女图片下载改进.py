import urllib.request
import os
from bs4 import BeautifulSoup
import os.path
import re
import json
def findPhoto(html):
    soup = BeautifulSoup(html.decode("utf-8"),"lxml")
    # print(soup.prettify())
    #第一个参数是标签的名字，第二个href是a标签下的属性值
    listUrl = soup.find_all('a',href=re.compile('.jpg'))
    print(listUrl)
    # print("type",type(listUrl))
    PhotoUrl = []
    for each in listUrl:
        # print("typeeach",type(each))
        # print(each["href"])
        PhotoUrl.append(each['href'])
    # print(PhotoUrl)
    # listUrl = []
    # for each in list1:
    #     for eachChildren in each.children:
    #         print(eachChildren)
    #         listUrl.append(eachChildren[class_])
    #         print(eachChildren[class_])
    return PhotoUrl

# 利用正则表达式匹配
# def findPhoto(html):
#     html = html.decode("utf-8")
#     p = r'"([^"]*\.jpg)"'
#     rp = re.compile(p)
#     imglist = rp.findall(html)
#     # imglist =  re.findall(p,html)
#     imglist = set(imglist)#imglist中会有重复项，用set进行过滤
#     print(imglist)
#     return imglist

def openUrl(url1):
    req = urllib.request.Request(url1)
    req.add_header(
        "user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def download():
    os.chdir("/Users/yizhichangyuan/Desktop")
    if not os.path.exists("/Users/yizhichangyuan/Desktop/Photo"):
        os.mkdir("Photo")
    os.chdir("/Users/yizhichangyuan/Desktop/Photo")
    url = "http://jandan.net/ooxx"
    html = openUrl(url)
    listPhoto = findPhoto(html)
    count = 0
    for eachUrl in listPhoto:
        try:
            fileName = "Photo_%d.jpg" % count
            count += 1
            # print("%",type(eachUrl))
            html = openUrl("http:" + eachUrl)
            with open(fileName,"wb") as f:
                f.write(html)
            # print("^&^")
        except ValueError as reason:
            print(reason)

download()
