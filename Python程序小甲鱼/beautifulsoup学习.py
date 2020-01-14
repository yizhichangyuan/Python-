# # import re
# #
# # print(re.search(r"2[0-4]\d|25[0-5]|1\d\d|[1-9]\d|\d","256"))
# from bs4 import BeautifulSoup
# import re
# import urllib.request
# doc = ['<html><head><title>Page title</title></head>',
# '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
# '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
# '</html>']
# # response = urllib.request.urlopen("https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/")
# # html = response.read()
# # print(html)
# soup = BeautifulSoup(doc,'html.parser')
# print(soup.prettify())
# # print(soup.p)
# # print(soup.p.string)
# # print(soup.contents[0].contents[0])
# # print(soup.prettify())

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
print("%")
pattern = re.compile("l")
a = pattern.findall(html_doc)
print(soup.find_all(href=re.compile("l")))
print(soup.find_all('a',href=re.compile("till")))

for link in soup.find_all('a',href=re.compile(r'example')):
    print(link["href"])
# print(soup.p.children.string)
# print(type(soup.get_text()))