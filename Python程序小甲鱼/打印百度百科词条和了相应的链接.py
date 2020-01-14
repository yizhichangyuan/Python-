from bs4 import BeautifulSoup
import re
import urllib.request

url = "http://baike.baidu.com/view/284853.html"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html,"lxml")
pattern = re.compile(r'view')
list1 = soup.find_all(href=pattern)
for each in list1:
    # print(type(each.string))
    # print(str(each.string)
    # print("href",type(each["href"]))
    # 利用join方法比+更高效，前面的；两个引号表示用其中的内容进行连接
    #由于第三个tag的string位于子节点，直接用string只能获取母节点下的string,由于没有只能返回none，这里面利用get_text获取所有子母节点的string，本体只获取到一个
    print(each.get_text(),'>',''.join(["http://baike.baidu.com",each["href"]]))
print(list1[2].string)