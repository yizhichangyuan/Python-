import json

with open('number.json','r') as f:
    number = json.load(f)
print(number[1])