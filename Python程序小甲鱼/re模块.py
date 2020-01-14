import re

pattern = re.compile(r"ar{1}")
print(pattern.match("anarge"))#在不指定pos时，默认情况下是匹配整个字符串的开头
print(pattern.search("anarge"))
print(pattern.findall("anargearkml"))
for each in pattern.finditer("anarhfaarjkf"):
    print(each)

print(pattern.sub("13",string = "anarge"))

patterns = re.compile(r"(\w+)\.(\w+)")
o = patterns.match("boy.girl.you")
print(o.start())
print(o.start(2))
print(o.end())
print(o.end(1))
print(o.span())
print("匹配到的整个字符串",o.group()[0:8])
print(o.span(2))
# print(o.group(1,2))

patterns2 = re.compile(r"\.")
o = patterns2.split("boy.girl.you")
print(o)