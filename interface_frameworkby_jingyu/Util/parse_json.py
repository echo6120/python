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
            data = json.load(fp)
            return data

#根据关键字获取数据
    def get_data(self,id):
        print type(self.data)
        return self.data[id]

#写json
    def write_data(self,data):
        with open(test_data_json_path,'w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
	opjson = OperetionJson(test_data_json_path)
	print opjson.get_data('shop')
