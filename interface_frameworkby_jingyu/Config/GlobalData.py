#coding=utf-8
import os

#获取工程所在的目录的绝对路径
project_path=os.path.dirname(os.path.dirname(__file__))
#测试数据data目录
DataFilePath = project_path.decode("gbk")+u"/TestData/data.xlsx"
#print DataFilePath
#print os.path.exists(DataFilePath)

#json文件的路径
test_data_json_path=project_path.decode("gbk")+u"/TestData/user.json"
#print test_data_json_path

testcase_id =1
testcase_url=3
testcase_is_excute =4
testcase_requestway=5
testcase_header =6
testcase_case_depend =7
testcase_data_depend=8
testcase_test_field_depend=9
testcase_data=10
testcase_expectresult=11
testcase_result =11

