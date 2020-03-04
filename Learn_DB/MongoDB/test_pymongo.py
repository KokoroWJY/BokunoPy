from pymongo import MongoClient
from datetime import datetime


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


def main():
    obj = TestMongo()
    rest = obj.add_one()
    print(rest.inserted_id)


if __name__ == '__main__':
    main()
