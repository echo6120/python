#coding=utf-8
import requests
import urllib3
import re
import sys
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl import load_workbook

#通过标签抓取课程详情页url
def get_kelink(labellink_file,kelink_file):
    valid_kelink=[]
    with open(labellink_file) as fp:
        for line in fp:
            requests.packages.urllib3.disable_warnings()
            resq1=requests.get(line.strip(),verify=False).text
            ke_urls = re.findall(r"href=\"(https://ke\.youdao\.com/course/detail/\d+)",resq1)
            for kelink in ke_urls:
                valid_kelink.append(kelink.strip())
    with open(kelink_file,"w")as fp1:
        for kelink in set(valid_kelink):
            fp1.writelines(kelink+"\n")
    print "ke url get done"

label_filename="d:\\label.txt"
kelink_file="d:\\kelink.txt"
get_kelink(label_filename,kelink_file)