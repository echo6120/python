#coding=utf-8
import requests
import requests
import urllib3
import re
import sys
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl import load_workbook


urllib3.disable_warnings()
UA="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
header = { "User-Agent" : UA,
           "Cookie":"OUTFOX_SEARCH_USER_ID_NCOO=1630482394.4868531; OUTFOX_SEARCH_USER_ID=-966270565@106.2.43.11; UM_distinctid=16339a7bc651cc-0265c2830f600b-444a022e-100200-16339a7bc661a2; __da_ntes_utmz=255406226.1525680684.1.1.; __da_ntes_utmfc=utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none); _9755xjdesxxd_=32; keoutvendor=; _ga=GA1.2.1946758071.1525780890; ke_Pdt=CourseWeb,CourseWeb; gdxidpyhxdE=B9JCJH4OtrmLPvTBrvb3%5CrSGIMUpZ5dTpA3Qu5XEEvWN7XH29XvhRfUMfTRuAjM6reivh%2B8fPJPidaZWKHjWuUsA9HPPPIvTlr%2BDS%2FCyrdwj1VSwgkv4NitelE0AgERiXYcECt37zg4hiWGEwtRBII5%2BjyVTLk6jaOKTgq7iGRSqLS28%3A1526355272041; P_INFO=211703622@fanli.163.com|1526891317|2|kaola|00&99|null#0|null|kaola|211703622@fanli.163.com; JSESSIONID=aaaCdjygJKinM_-kWXjpw; DICT_FORCE=true; Hm_lvt_e46790f6d676f71878ebef1153dda3e2=1528087853,1528210514,1528248664,1528366049; DICT_SESS=v2|Ch9F-7ICXmYWRMJ4OMTz0kEnfQZhf6B0k5n4gynMqS0OlOLzA64TK0U5k4OY6MeK0l50MeFP4P40zlhfYEhf6y0YfRHlW0HPu0; DICT_PERS=v2|urstoken||DICT||web||-1||1528373331562||220.181.102.181||iphoneceshi6@163.com||w4hHzA6Mkl0eyRL6u0LQuRwShLgKhH6z0Tuh4eFkLQB0g4hMPykfl5RwB0MkfnHqL0U5h4wLnHwuRJ4k4lA0Lll0; DICT_LOGIN=3||1528373331567; ke_inLoc=vp_pro_tag430; xuetangvendor=index; ___rl__test__cookies=1528433987808; CNZZDATA1253417976=1882109338-1525679476-null%7C1528433779; __da_ntes_utma=255406226.2229805.1525680684.1528381185.1528433993.36; Hm_lpvt_e46790f6d676f71878ebef1153dda3e2=1528434034; __da_ntes_utmb=255406226.2.10.1528433993"
           }
result3=requests.get("https://ke.youdao.com/user/order/?Pdt=CourseWeb",verify=False,headers=header)
print result3.content


'''
session = requests.Session()
cookies = requests.utils.dict_from_cookiejar(session.cookies)
print 'cookies: ', cookies
cookiejar = result3.cookies    #获取的是cookiejar对象
#将cookiesjar对象转换成字典
dict_cookies = requests.utils.dict_from_cookiejar(cookiejar)
requests.utils.add_dict_to_cookiejar(session.cookies, dict_cookies)
url = "https://ke.youdao.com/user/order/"
result4 = session.get(url,verify=False)
print result4.text
'''
