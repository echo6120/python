#coding=utf-8
import requests
import urllib3
import re
from bs4 import BeautifulSoup


#获取beautifulsoup对象
url ="https://ke.youdao.com/course/detail/9405"
urllib3.disable_warnings()
resq = requests.get(url,verify=False).text
soup = BeautifulSoup(resq,'html.parser')

#css选择器
#a.过标签名查找,打印标签名为div
print soup.select('div')#直接原值表示标签名
print"==============================================================================================================="
#b.通过类名查找，打印class=.g-w body
print soup.select('.g-w body')#.加值代表类名
print"==============================================================================================================="
#c.通过id查找
print soup.select('#mod-course-head')##字符代表id
print"==============================================================================================================="
#d.组合查找
#定位课程标题
print soup.select("div.g-w.body > div > h1")[0]
print"==============================================================================================================="
#定位课程状态
print soup.select("div.g-w.body > div > p.course-status")[0]
print"==============================================================================================================="
