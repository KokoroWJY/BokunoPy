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


class TestList(object):
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def test_push(self):
        """ lpush/rpush -- 从左/右插入数据 """
        values = ['Amy', 'Jhon']
        rest = self.r.lpush('l_eat', *values)  # lpush(name, *values)
        print(rest)
        rest = self.r.lrange("l_eat", 0, -1)
        print(rest)

    def test_pop(self):
        """ lpop/rpop -- 移除最左/右的元素并返回 """
        rest = self.r.lpop("l_eat2")
        print(rest)


def main():
    obj = TestString()
    #
    # rest = obj.test_set()
    # print(rest)
    #
    # rest = obj.test_get()
    # print(rest)
    #
    # rest = obj.test_mset()
    # print(rest)
    #
    # rest = obj.test_mget()
    # print(rest)
    #
    # rest = obj.test_del()
    # print(rest)

    list_obj = TestList()

    # list_obj.test_push()

    # list_obj.test_pop()


if __name__ == '__main__':
    main()
