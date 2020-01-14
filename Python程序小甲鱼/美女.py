import urllib.request
import os
def findPhoto(html):
    listPhoto = []
    start = html.find('a href="//')
    while start != -1:
        end = html.find('.jpg',start)
        if end - start <= 100:
            if end!= -1:
                listPhoto.append("http:" + html[start+8:end+4])
            else:
                end = start + 9
        start = html.find('a href="//',end)
    print(listPhoto)
    return listPhoto

def openUrl(url1):
    req = urllib.request.Request(url1)
    req.add_header(
        "user-agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def download():
    os.chdir("/Users/yizhichangyuan/Desktop")
    os.mkdir("Photo")
    os.chdir("/Users/yizhichangyuan/Desktop/Photo")
    url = "http://jandan.net/ooxx"
    html = openUrl(url)
    html = html.decode("utf-8","ignore")
    listPhoto = findPhoto(html)
    count = 0
    for eachUrl in listPhoto:
        fileName = "Photo_%d.jpg" % count
        count += 1
        html = openUrl(eachUrl)
        with open(fileName,"wb") as f:
            f.write(html)

download()
