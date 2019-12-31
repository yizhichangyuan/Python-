import json
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
submission_ids = response.json()

plot_dicts,names = [],[]
for submission_id in submission_ids[:30]:
    url = ''.join(['https://hacker-news.firebaseio.com/v0/item/',str(submission_id),'.json'])
    response = requests.get(url)
    r = response.json()
    plot_dict = {'value':r['descendants'],'xlink':r['url']}
    plot_dicts.append(plot_dict)
    names.append(r['title'])

# #将plot_dicts依照每个字典的Value值排序，相应的name也应该改变顺序,此方法不行，name的顺序没有改变
# plot_dicts = sorted(plot_dicts,key=lambda x:int(x['value']，reverse=False))

#利用zip函数将两个列表关联，再解压
z = zip(names,plot_dicts)
z = sorted(z,key=lambda x:x[1]['value'],reverse=True)
names,plot_dicts = zip(*z)

my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.title = "Hack Pop Article"
my_config.truncate = 15
my_config.x_label_rotation = 45
chart = pygal.Bar(my_config,style=my_style)
chart.add('',plot_dicts)
chart.x_labels = names
chart.render_to_file("Hack_pop_article.svg")



