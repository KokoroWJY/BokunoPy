from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


class TestMongo(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['blog']

    def add_one(self):
        """ 新增一条数据 """
        post = {
            'title': '新的标题',
            'content': '博客内容, ....',
            'created_at': datetime.now()
        }
        return self.db.blog.insert_one(post)

    def get_one(self):
        ''' 查询一条数据 '''
        return self.db.blog.find_one()

    def get_more(self):
        ''' 查询多条数据 '''
        return self.db.blog.find({'x': None})  # 查询blog里面x没有值的数据

    def get_one_from_oid(self, oid):
        ''' 查询指定id的数据 '''
        return self.db.blog.find_one({'_id': ObjectId(oid)})


def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest.inserted_id)

    # rest = obj.get_one()
    # print(rest)

    # rest = obj.get_more()
    # for item in rest:
    #     print(item['_id'])

    rest = obj.get_one_from_oid('5e5ef9ee71d06d8f73481bc2')
    print(rest)


if __name__ == '__main__':
    main()
