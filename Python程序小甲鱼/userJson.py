import json

"""用户首次登陆则访问名字，不是首次登录，则输出起名字，利用存储用户名的文件是否存在来判断"""
fileName = 'userName.json'
try:
    with open(fileName) as f:
        name = json.load(f)
except FileNotFoundError:
    userName = input("What's your name")
    with open(fileName,'w') as f:
        json.dump(userName,f)
    print('I will remenber your name ' + userName)
else:
    print(name + " Welcome back!")

'''重构'''

def getSortedName():
    fileName = "userName.json"
    try:
        with open(fileName) as f:
            name = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return name

def getNewName():
    name = input("what is your name")
    fileName = "userName.json"
    with open(fileName,'w') as f:
        json.dump(name,f)
    return name


def greetUser():
    name = getSortedName()
    if name:
        response = input("it's your name? Y/N")
        if response == "Y":
            print(name + "Welcome back!")
        else:
            name = getNewName()
            print("I will rember your name " + name)
    else:
        name = getNewName()
        print("I will rember your name " + name)

greetUser()
