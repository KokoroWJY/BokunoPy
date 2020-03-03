from pymongo import MongoClient

class TestMongo(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['students']