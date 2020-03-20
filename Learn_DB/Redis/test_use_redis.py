import redis


# 链接数据库的方式
# r = redis.Redis(host='localhost', port=6379, db=0)  # 比较老的一种办法
# r = redis.StrictRedis(host='localhost', port=6379, db=0)  # 最新

class TestString(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)  # 最新

    def test_set(self):
        """ 使用set设置值 """
        return self.r.set('user2', 'Amy')

    def test_get(self):
        """ 使用get获取值 """
        return self.r.get('user3')

    def test_mset(self):
        """mset --设置多个键值对"""
        d = {
            'user3': 'Bob',
            'user4': 'Bobx'
        }
        return self.r.mset(d)

    def test_mget(self):
        """mget --获取多个键值对"""
        l = ['user3', 'user4']
        return self.r.mget(l)

    def test_del(self):
        return self.r.delete('user3')


def main():
    obj = TestString()

    # rest = obj.test_set()
    # print(rest)

    # rest = obj.test_get()
    # print(rest)

    # rest = obj.test_mset()
    # print(rest)

    # rest = obj.test_mget()
    # print(rest)

    # rest = obj.test_del()
    # print(rest)


if __name__ == '__main__':
    main()
