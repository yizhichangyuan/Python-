import easygui as gui
import urllib.request

def measurement():
    fieldNames = ["宽","高"]
    size = width, height = 400, 600
    fieldValues = gui.multenterbox(msg="请填写喵的尺寸",title = "下载一只喵",fields = fieldNames)
    while True:
        esmg = ""
        try:
            int(fieldValues[0])
        except:
            esmg += "宽度必须是整数"

        try:
            int(fieldValues[1])
        except:
            esmg += "高都必须是整数"

        if esmg == "":
            break

        fieldValues = gui.multenterbox(esmg,title="下载一只喵",fields = fieldNames)
    root = gui.diropenbox(msg="请选择存放喵的文件夹", title="浏览文件夹", default="/Users/yizhichangyuan/Desktop")
    return fieldValues,root

def download():
    values = measurement()
    url = "http://placekitten.com/%s/%s"%(values[0][0].strip(),values[0][1].strip())
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36')
    html = urllib.request.urlopen(req)
    content = html.read()
    root = values[1] + "/cat.jpg"
    with open(root,"wb") as f:
        f.write(content)

download()