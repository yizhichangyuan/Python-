import csv
from pygal_maps_world.i18n import COUNTRIES
fileName = 'world_gdp.csv'
import pygal

def get_countryCode(countryName):
    """获取国别码"""
    for code,name in COUNTRIES.items():
        if name == countryName:
            return code
    return None

f = open(fileName)
reader = csv.reader(f)
for i in range(6):
    head_row = next(reader)
print(head_row)
# for index,content in enumerate(head_row):
#     print(index,content)

country_gdp = {}
def get_countryName_gdp_2018(reader):
    """获取国别码以及对应的gdp"""
    for row in reader:
        try:
            countryName = row[0]
            gdp = float(row[62])
        except ValueError:
            print('Error',row[62])
        else:
            code = get_countryCode(countryName)
            if code:
                print('code_gdp',code,gdp)
                country_gdp[code] = gdp
            else:
                print(countryName,'missing code')

get_countryName_gdp_2018(reader)

gdp1,gdp2,gdp3,gdp4 ={},{},{},{}
def classify(country_gdp):
    for code,gdp in country_gdp.items():
        if gdp < 10000000000:
            gdp1[code] = gdp
        elif gdp < 100000000000:
            gdp2[code] = gdp
        elif gdp < 1000000000000:
            gdp3[code] = gdp
        else:
            gdp4[code] = gdp

classify(country_gdp)
wm = pygal.maps.world.World()
wm.title = "World GDP 2018"
wm.add("<100bm",gdp1)
wm.add('<1000bm',gdp2)
wm.add('<10000bm',gdp3)
wm.add('>10000bm',gdp4)
wm.render_to_file('world_gdp.svg')





