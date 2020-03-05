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

    def update_one(self):
        """修改一条数据"""
        return self.db.blog.update_one({'x': 11}, {'$inc': {'x': 10}})  # $inc 增加

    def update_more(self):
        """ 修改多条数据 """
        return self.db.blog.update_many({'x': None}, {'$set': {'x': 1}})  # $set 变成

    def delete_one(self):
        ''' 删除一条数据 '''
        return self.db.blog.delete_one({'title': 'first'})

    def delete_more(self):
        ''' 删除多条数据 '''
        return self.db.blog.delete_many({'x': 1})


def main():
    obj = TestMongo()
    # rest = obj.add_one()
    # print(rest.inserted_id)

    # rest = obj.get_one()
    # print(rest)

    # rest = obj.get_more()
    # for item in rest:
    #     print(item['_id'])

    # rest = obj.get_one_from_oid('5e5ef9ee71d06d8f73481bc2')
    # print(rest)

    # rest = obj.update_one()
    # rest = obj.update_more()
    # print(rest.matched_count)
    # print(rest.modified_count)

    # rest = obj.delete_one()
    # rest = obj.delete_more()
    # print(rest.deleted_count)


if __name__ == '__main__':
    main()
