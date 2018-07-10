#coding:utf-8
from Util.Excel import *
from Config.GlobalData import *
from Util.parse_json import *

class GetData:
	def __init__(self):
		self.opera_excel = ParseExcel(DataFilePath)

	#去获取excel行数,就是我们的case个数	
	def get_case_lines(self):
		return self.opera_excel.get_max_row_no()

	#获取是否执行
	def get_is_run(self,row):
		flag = None
		col = int(testcase_is_excute)
		run_model = self.opera_excel.get_cell_content(row,col)
		if run_model == 'y':
			flag = True
		else:
			flag = False
		return flag


	#是否携带header
	def is_header(self,row):
		col = int(testcase_header)
		header = self.opera_excel.get_cell_content(row,col)
		if header != '':
			return header
		else:
			return None

	#获取请求方式
	def get_request_method(self,row):
		col = int(testcase_requestway)
		request_method = self.opera_excel.get_cell_content(row,col)
		return request_method

	#获取url
	def get_request_url(self,row):
		col = int(testcase_url)
		url = self.opera_excel.get_cell_content(row,col)
		return url


	#获取请求数据
	def get_request_data(self,row):
		col = int(testcase_data)
		data = self.opera_excel.get_cell_content(row,col)
		print data
		if data == '':
			return None
		return data

	#通过获取关键字拿到data数据
	def get_data_for_json(self,row):
		opera_json = OperetionJson(test_data_json_path)
		request_data = opera_json.get_data(self.get_request_data(row))
		#print "debug:",request_data
		return request_data



	#获取预期结果
	def get_expcet_data(self,row):
		col = int(testcase_expectresult)
		expect = self.opera_excel.get_cell(row,col)
		if expect == '':
			return None
		return expect.value

	def write_result(self,row,value):
		col = int(testcase_result)+1
		print col
		self.opera_excel.write_cell_content(row,col,value)

	#获取依赖数据的key
	def get_depend_key(self,row):
		col = int(testcase_case_depend+1)
		depent_key = self.opera_excel.get_cell_content(row,col)
		if depent_key == "":
			return None
		else:
			return depent_key

	#判断是否有case依赖
	def is_depend(self,row):
		col = int(testcase_data_depend-1)
		depend_case_id = self.opera_excel.get_cell_content(row,col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	#获取数据依赖字段
	def get_depend_field(self,row):
		col = int(testcase_test_field_depend)
		data = self.opera_excel.get_cell_content(row,col)
		if data == "":
			return None
		else:
			return data

if __name__=="__main__":
	getdata = GetData()
	#print getdata.get_case_lines()
	#print getdata.get_is_run(2)
	#print getdata.is_header(2)
	#print getdata.get_request_method(2)
	#print getdata.get_request_url(2)
	#print getdata.get_request_data(2)
	print getdata.get_data_for_json(13)
	#print getdata.get_expcet_data(2)
	#print getdata.write_result(2,"哈哈哈哈或或或或或或或或或或或或")
	#for i in range(1,15):
	#	print getdata.get_depend_key(i)
	#print getdata.is_depend(2)
	#print getdata.get_depend_field(2)