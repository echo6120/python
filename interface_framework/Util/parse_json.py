#coding:utf-8
import json
from Config.GlobalData import *

#coding:utf-8
import json
class OperetionJson:

    def __init__(self,test_data_json_path):
        self.test_data_json_path = test_data_json_path
        self.data = self.read_data()

#读取json文件
    def read_data(self):
        with open(self.test_data_json_path) as fp:
        #将json格式字符串解码成Python对象
            data = json.load(fp)
            return data

#根据关键字获取数据
    def get_data(self,id):
        #通过键值对找到数据
        print type(self.data)
        return self.data[id]

#写json
    def write_data(self,data):
        #将python对象转换为json格式的字符串
        with open(test_data_json_path,'w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
	opjson = OperetionJson(test_data_json_path)
	print opjson.get_data('shop')
