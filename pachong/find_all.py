#coding=utf-8
import requests
import urllib3
import re
from bs4 import BeautifulSoup

#获取beautifulsoup对象
url ="https://ke.youdao.com/"
urllib3.disable_warnings()
resq = requests.get(url,verify=False).text
soup = BeautifulSoup(resq,'html.parser')

#find_all
#1.name参数
print "打印主页中，标签为h1的标签:",soup.find_all('h1')
#2.正则表达式
for tag in soup.find_all(re.compile("^b")):
    print "打印以b开头的标签：",(tag.name)

#3.传属性参数筛选
print "打印id为link2的标签：",soup.find_all(id='link2')  # 搜索有id属性并且对应值为link2

print soup.find_all(href=re.compile("/tag/\d+"))  # 搜索有href属性并且符合正则表达式值得结果
print soup.find_all("a", class_="sister")  # 对于类似class需要后面加上_
print soup.find_all(attrs={"class": "title"})  # attrs传键值对条件

#4.text参数
print soup.find_all(text="实用英语")  # 搜索一个内容
print soup.find_all(text=["四六级", "考研", "实用英语"])  # 一次搜索三个内容
print soup.find_all(text=re.compile("Dormouse"))  # 根据正则表达式搜索内容
#5.limit参数
soup.find_all("a", limit=2)  # 对筛选结果筛选两个内容