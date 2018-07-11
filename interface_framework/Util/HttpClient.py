#encoding=utf-8
import requests
from Util.parse_json import *
import traceback


class HttpClient(object):
    def __init__(self):
        pass

    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        #return res.json()
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        #return json.dumps(res, ensure_ascii=False)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)



if __name__=="__main__":
    httprequest =  HttpClient()
    data = {
        'userid': 'jindutest4@163.com',
        'bookId': '16',
        'knowledgeId': '9194'
    }
    #result = httprequest.run_main("Post","http://m.imooc.com/passport/user/login",data)
    result = httprequest.run_main("get", "http://ke.youdao.com/tiku/pad/questions/next", data)
    print result


















