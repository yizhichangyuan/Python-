import re
import urllib.request
from bs4 import BeautifulSoup
import string
import urllib.parse
#此方法来查看是否有副标题，有太多干扰，实际有副标题是每个网页打开后有h1,h2

def search(html):
    soup = BeautifulSoup(html,"lxml")
    #re.compile(r'"[^"]*"')此为错误，因为title=形如字典，默认了后面的元素有""
    list1 = soup.find_all('a',title=re.compile(r'[^"]+'))
    # print(list1)
    for each in list1:
        if each.string:
            print(''.join([each["title"],'(',each.string,')',each["href"]]))
    print(list1[2].string)

url = "http://baike.baidu.com/item/"
keyword = input("请输入关键词：")
url = ''.join([url,keyword])
#urlopen中的url不能有中文字符，可以通过urllib.parse.quote进行转换，safe表示可以忽略的字符。
#string.printable表示ASCII码第33～126号可打印字符，其中第48～57号为0～9十个阿拉伯数字；65～90号为26个大写英文字母，97～122号为26个小写英文字母，其余的是一些标点符号、运算符号等。
#如果去掉safe参数的内容将会出错。
url = urllib.parse.quote(url,safe=string.printable)
response = urllib.request.urlopen(url)
if response.geturl() == "https://baike.baidu.com/error.html":
    print("百度百科尚未收录该词条")
else:
    html = response.read()
    search(html)

