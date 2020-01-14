import urllib.request
import re
import urllib.parse
import string
from bs4 import BeautifulSoup
import easygui as gui
url = "http://baike.baidu.com/item/"
keyword = input("请输入关键词：")
url = ''.join([url,keyword])

#urlopen中的url不能有中文字符，可以通过urllib.parse.quote进行转换，safe表示可以忽略的字符
url = urllib.parse.quote(url,safe=string.printable)

response = urllib.request.urlopen(url)
if response.geturl =="https://baike.baidu.com/error.html":
    print("百度百科未收录此词条")
else:
    html = response.read()

    soup = BeautifulSoup(html,"lxml")
    list1 = soup.find_all('a',href=re.compile('item'))
    print(list1)
    print(len(list1))
    count = 0
    for each in list1:
        # print("each.a",each.a)
        # print(each.a["href"])
        url2 = ''.join(["http://baike.baidu.com",each["href"]])
        url2 = urllib.parse.quote(url2, safe=string.printable)
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2,"lxml")
        print(soup2.h1.next_sibling.name == 'h2')
        if soup2.h1 and soup2.h2:
            print(''.join([soup2.h1.string,'(',soup2.h2.string,')',url2]))
        count += 1
        if count % 10 == 0:
            if gui.ynbox(msg = "您还需要接着往下看嘛",title = "用户提示",choices=["Yes","No"]):
                continue
            else:
                break