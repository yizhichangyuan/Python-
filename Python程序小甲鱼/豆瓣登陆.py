import re
import urllib.request
import http.cookjar

loginUrl = "https://wwww.douban.com/accounts/login"
cookie = http.cookjar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

data ={
    "form-email":"your email",
    "form_password":"your password",
    "source":"index_av"
}
data["form_email"] = ""
data["form_password"] = ""
data["source"] = "index_av"

response = opener.open(loginUrl,urllib.request.urlencode(data).encode("utf-8"))
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read().decode()
    imgurl

