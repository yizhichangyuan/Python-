import chardet
import urllib.request

def openUrl(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def detectCode(html):
    code = chardet.detect(html)
    print(code["encoding"])

html = openUrl("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=Python%E5%AE%98%E6%96%B9%E6%96%87%E6%A1%A3&oq=beautifulsoup&rsv_pq=8517d7c80001c62e&rsv_t=d74eO2iJ100xSagOhVQyZQvTDz%2BsfcykO4vjg1FGjx1jlTHodTR3a2HuShk&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=37&rsv_sug1=30&rsv_sug7=100&rsv_sug2=0&inputT=11699&rsv_sug4=13099")
detectCode(html)