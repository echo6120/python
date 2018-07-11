#coding = utf-8
import requests

data={
    'userid':'jindutest4@163.com',
    'bookId':'16',
    'knowledgeId':'9194'
}
print type(data)
response = requests.get('http://ke.youdao.com/tiku/ai/questions/next',params=data)
print response.text