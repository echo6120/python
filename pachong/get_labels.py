#coding=utf-8
import requests
import urllib3
import re
import sys
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl import load_workbook

#抓取标签,"http://ke.youdao.com"
#定义get_labels函数，需要两个参数，需要抓取的url 以及 将抓取到的内容保存的文档地址
def get_labels(url,label_file):
    #消除关闭证书验证的警告
    urllib3.disable_warnings()
    #将SSL证书取消验证
    resq = requests.get(url,verify=False).text
    #通过正则提取出标签
    labels = re.findall(r"href=\"(/tag/\d+)",resq)
    valid_labellink=[]
    for label in labels:
        valid_labellink.append(url+label)
    with open(label_file,"w") as fp:
        for i in set(valid_labellink):
            fp.writelines(i+"\n")
    print "labes url get done"

url="https://ke.youdao.com"
label_filename="d:\\label.txt"
get_labels(url,label_filename)