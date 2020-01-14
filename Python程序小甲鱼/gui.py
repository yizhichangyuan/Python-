import easygui as gui
import os
import PIL#处理图形的库，让img显示
import sys

os.chdir('/Users/yizhichangyuan/Desktop/Photo')
# msg = gui.msgbox(msg = "hello",title = "nihao",ok_button = "接下来",image = 'Photo_0.jpg')
msg = gui.integerbox(msg = "请填写喵的尺寸",title = '下载一只喵',default ='35',lowerbound = 30,upperbound = 40)
print("msg",msg)
fieldNames = ["宽:","高:"]
fieldValues = []
msg = gui.multenterbox(msg = "请填写喵的尺寸",title = "下载一只喵",fields = fieldNames)
print(msg)
# if msg
#     gui.ccbox("here is continue")#两个button，分别是continue,cancel
#     gui.ynbox("haha")  # 两个button，分别是yes,no
#     choices = ["一", "二", '三']
#     gui.buttonbox('你想选择的是', "title", choices)
# else:
#     sys.exist(0)
