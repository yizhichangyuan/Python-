import os
import os.path
import easygui as gui

msg = "请选择要检测代码量的文件夹"
title = "检测代码量"
defaultPath = "/Users/yizhichangyuan/Desktop"
detectPath = gui.diropenbox(msg, title, defaultPath)
print("获取路径：",detectPath)
countLine = 0

def detect(detectPath):
    """检测所在路径的py文件或者cpp文件总共多少行"""
    os.chdir(detectPath)
    listDir = os.listdir()
    # print('listDir',listDir)
    fileType = [".cpp",".c",'.py']
    global countLine

    for each in listDir:
        if os.path.isfile(each):
            if os.path.splitext(each)[-1] in fileType:
                with open(each,'r') as f:
                    # for each in f:
                    #     countLine += 1
                    while f.readline():
                        countLine += 1
            # print("中间值",countLine)
        elif os.path.isdir(each):
            #是文件夹就递归搜索，注意返回条件：返回到上级目录
            detect(each)
            os.chdir(os.pardir)


detect(detectPath)
print('countLine',countLine)
msg = ''.join(["您选择的文件夹下总共",str(countLine) ,"行代码量",",仍需努力啊，少年！"])
try:
    gui.msgbox(msg,title = "代码量统计")
except:
    print(msg)
