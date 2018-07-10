#coding=utf-8
from Action.get_data import *
from Util.HttpClient import *
from Util.common_util import *
from Action.dependent_data import *
from Util.HttpClient import *
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class RunTest:
	def __init__(self):
		#模拟post/get请求
		self.httpclient = HttpClient()
		#获取请求数据
		self.data = GetData()
		#断言请求是否成功
		self.com_util = CommonUtil()

	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		#获取case的行数
		rows_count = self.data.get_case_lines()
		#print "rows_count",rows_count
		#第一行是标题行，不取数据，从1开始，遍历每一行测试接口的数据
		for i in range(1,rows_count):
		#判断是否执行
			is_run = self.data.get_is_run(i)
			if is_run:
			#获取Excel中的url，method，request_data,期望结果，头，依赖数据
				url = self.data.get_request_url(i)
				method = self.data.get_request_method(i)
				request_data = self.data.get_data_for_json(i)

				expect_result = self.data.get_expcet_data(i)
				header = self.data.is_header(i)
				depend_case = self.data.is_depend(i)
				#print "---------------------------"
				#print url,method,request_data,type(request_data),expect_result,header,depend_case
				#print "---------------------------"
				#print "this is depend_case",depend_case
				if depend_case != None:
					#实例化dependdent类
					self.depend_data = DependdentData(depend_case)
					#获取的依赖响应数据
					depend_response_data = self.depend_data.get_data_for_key(i)
					#print "depend_response_data",depend_response_data
					#获取依赖的key
					depend_key = self.data.get_depend_field(i)
					#print "depend_key1111111111111111111",depend_key
					request_data[depend_key] = depend_response_data
				#run_main(self, method, url, data=None, header=None)
				res = self.httpclient.run_main(method, url, request_data, header)

				#if self.com_util.is_equal_dict(expect_result,res) == 0:
				if self.com_util.is_contain(expect_result,res):
					self.data.write_result(i,'pass')
					pass_count.append(i)
				else:
					print res
					self.data.write_result(i,res)
					fail_count.append(i)
				print "pass:",len(pass_count),"fail:",len(fail_count)



if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()