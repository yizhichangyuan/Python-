doc = '<h1>猪八戒</h1><h2>（小说《西游记》中的角色）</h2>'
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(doc,"lxml")
print(soup.h1)
print(soup.h1.next_sibling.name == "h2")
print(soup.h1.next_sibling == soup.h2)
print(soup.h2)
print(soup.h1.next_sibling == soup.h2)
while True:
    try:
        number1 = int(input("Please input first number"))
        number2 = int(input("Please input second number"))
    except ValueError:
        print("你输入的不是数字")
    else:
        print('两数除为：',number1/number2)
