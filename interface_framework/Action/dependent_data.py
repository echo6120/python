#coding:utf-8
from Action.get_data import *
#from test_script.runtest import *
from Util.HttpClient import *
from jsonpath_rw import jsonpath,parse
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
class DependdentData:
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = ParseExcel(DataFilePath)
		self.data = GetData()

	#通过case_id去获取该case_id的整行数据
	def get_case_line_data(self):
		rows_data = self.opera_excel.get_row_data(self.case_id)
		return rows_data

	#执行依赖测试，获取结果
	def run_dependent(self):
		httpclient = HttpClient()
		#取行号
		row_num  = self.opera_excel.get_row_num(self.case_id)
		print "row_num",row_num
		#请求数据
		request_data = self.data.get_data_for_json(row_num)
		header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = httpclient.run_main(method,url,request_data,header)
		#print "res",res
		#print "**********"
		#print "request_data",request_data,"header",header,"method,url",method,"url",url,"res",res
		return json.loads(res)

	#根据依赖的key去获取执行依赖测试case的响应,然后返回
	def get_data_for_key(self,row):
		depend_data = self.data.get_depend_key(row)
		print "depend_data",depend_data
		if depend_data !=None:
			response_data = self.run_dependent()
			print "response_data",type(response_data)
			#设置规则，在层级关系中查找需要的数据
			try:
				json_exe = parse(depend_data)
				#查找内容
				madle = json_exe.find(response_data)
				print "madle",madle
				if madle !=None:
					return [math.value for math in madle][0]
				else:
					print "nothing is find"
			except Exception,e:
				raise e

if __name__ == '__main__':

	test = DependdentData("Imooc-11")
	print test.get_case_line_data()
	#print test.run_dependent()
	print test.get_data_for_key(12)


