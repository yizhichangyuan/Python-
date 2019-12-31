import json
#国别码的字典
from pygal_maps_world.i18n import COUNTRIES
import pygal
from pygal.style import RotateStyle,LightColorizedStyle

fileName = 'population_data.json'
with open(fileName) as f:
    pop_data = json.load(f)

def get_countryCode(countryName):
    """获取国别码"""
    for code,country in COUNTRIES.items():
        if country == countryName:
            return code
        elif countryName == "Yemen, Rep.":
            return 'ye'
    return None

cc_population = {}
def get_pop_country(pop_data):
    """获取国别码，以及人口数量"""
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            countryName = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            countryCode = get_countryCode(countryName)
            if countryCode:
                cc_population[countryCode] = population
            else:
                print('Eroor',countryName)

get_pop_country(pop_data)
print('population',len(cc_population))

cc_pop1,cc_pop2,cc_pop3={},{},{}
def classify(cc_population):
    """依照人口数量分类国家，使得数据展示更加合理"""
    for code,value in cc_population.items():
        if value < 100000000:
            cc_pop1[code] = value
        elif value < 1000000000:
            cc_pop2[code] = value
        else:
            cc_pop3[code] = value

classify(cc_population)

#指定三基色，让图表颜色显得更加好看;并将颜色鲜艳度提升
wm_style = RotateStyle("#336699",base_style= LightColorizedStyle)

wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Population'
wm.add('<1bm',cc_pop1)
wm.add('<10bm',cc_pop2)
wm.add('>10bm',cc_pop3)
wm.render_to_file('world.svg')
