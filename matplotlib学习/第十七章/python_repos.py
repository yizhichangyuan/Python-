import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
import sys



url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#这个api返回为json格式的信息
response = requests.get(url)
print("Status_code",response.status_code)

#转化为json结构，将api响应存储到一个变量中
response_dict = response.json()
# print(response_dict)
# print(response_dict.keys())
# print('total repositries:',response_dict['total_count'])

#探索仓库相关的信息
repo_dicts = response_dict["items"]
# print('Repositries Return:',len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]
print('\nKeys',len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print('\nSelected Information about each repositry')
# for repo_dict in repo_dicts:
#     print("\nName:",repo_dict['name'])
#     print('Owner:',repo_dict['owner']['login'])
#     print('Stars',repo_dict['stargazers_count'])
#     print('Respositry URL:',repo_dict['html_url'])
#     print('Description:',repo_dict['description'])

names,plot_dicts =[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {'value':repo_dict['stargazers_count'],
                 # 如果不加str，这里会出现错误，因为requests访问对象时
                 #第一个属性访问时，会将相应的字节码存储，但是当访问另一个属性text时
                 #因为Response对象会通过另一个属性encoding来将字节码编码成unicode
                 # 而这个encoding属性居然是responses自己猜出来的
                 #因为源码其中有一个description是空对象null
                 # 所以，在写入字典之前，要检查值，如果为空
                 # 那就填入一个特殊的字符串，这样就可以顺利执行了。
                 'label':str(repo_dict['description']),
                 'xlink':repo_dict['html_url']}
    plot_dicts.append(plot_dict)

my_config = pygal.Config()
#将x轴的每个标签旋转45度
my_config.x_label_rotation = 45
#不显示标签
my_config.show_legend = False
#设置图表标题的大小
my_config.tile_font_size = 24
#设置副标签大小
my_config.label_font_size = 14
#设置主标签大小
my_config.major_label_font_size = 18
#将x轴标签长度限定截断在15个字符以内
my_config.truncate_label = 15
#不显示图表中的水平线
my_config.show_y_guides = False
#自定义宽度，以更好地适应浏览器
my_config.width = 1000
my_style = LS('#333366',base_style=LCS)
#x_label_rotation将横轴的标签顺时针旋转45度，并隐藏了图例
chart = pygal.Bar(my_config,style = my_style)

chart.title = 'Most stared Python in Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repo.svg')

