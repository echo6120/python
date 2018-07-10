#coding:utf-8
import json

class CommonUtil:
	#str_one 查找到字符串，str_two 被查找的字符串
	def is_contain(self,str_one,str_two):
		flag = None
		if isinstance(str_one,unicode):
			str_one = str_one.encode("unicode-escape").decode('string_escape')
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag
