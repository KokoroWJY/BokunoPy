from pymongo import MongoClient

# 链接MongoDB的方法
client = MongoClient()
client2 = MongoClient('localhost', 27017)
client3 = MongoClient('mongodb://localhost:27017')

print(client3.database_names())
