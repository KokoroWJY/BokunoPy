from pymongo import MongoClient
from mongoengine import connect  # 使用ODM连接MongoDB

# 链接MongoDB的方法
client = MongoClient()
client2 = MongoClient('localhost', 27017)
client3 = MongoClient('mongodb://localhost:27017')

print(client3.database_names())

# 使用ODM连接MongoDB
con = connect('students')
con2 = connect('students', host='127.0.0.1', port=27017)
con3 = connect('students', host='mongodb://127.0.0.1:27017/students')
