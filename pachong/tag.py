#coding=utf-8
import requests
import urllib3
import re
from bs4 import BeautifulSoup

#创建beautifulsoup 对象
url ="https://ke.youdao.com/course/detail/9405"
urllib3.disable_warnings()
resq = requests.get(url,verify=False).text
soup = BeautifulSoup(resq,'html.parser')
print type(soup)
print soup

#输出beautifulsoup对象及解析
print "第一个title标签为：",soup.title#第一个title标签的内容
print "第一个head标签为：",soup.head#第一个head标签的内容
print "第一个p标签为：",soup.p#第一个p标签的内容
print "第一个a标签为：",soup. a #第一个a标签的内容
print "标签对象的类型为: ",type(soup.a)   #<class 'bs4.element.Tag'>
print "第一个a标签本身名称: ",soup.a.name#第一个a标签本身名称
print "第一个a标签的属性: ",soup.a.attrs#打印所有的属性
print "第一个a标签的属性href值: ",soup.a["href"]#获取属性值

#NavigableString（标签内容）
print "第一个title标签为: ",soup.title
print soup.title.string




