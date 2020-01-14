import json

numbers = [1,23,4]
fileName = "number.json"
with open(fileName,'w') as f:
    json.dump(numbers,f)