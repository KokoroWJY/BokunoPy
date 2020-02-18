import MySQLdb


class MysqlSearch(object):

    def __init__(self):
        self.get_coon()

    def get_coon(self):
        try:
            # 获取连接
            self.coon = MySQLdb.connect(host='127.0.0.1', user="root", password='68dxqiji', db='news', port=3306,
                                        charset="utf8")

        except MySQLdb.Error as e:
            print("Error %s" % e)

    def close_coon(self):
        try:
            if self.coon:
                self.coon.close()
        except MySQLdb.Error as e:
            print("Eorr %s" % e)

    def get_one(self):
        # 准备 sql
        sql = 'SELECT * FROM `news` ORDER BY `created_at` DESC;'

        # 找到 cursor
        cursor = self.coon.cursor()

        # 执行 sql
        cursor.execute(sql)

        # 拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))

        # 处理数据
        print(rest)
        print(rest['title'])

        # 关闭cursor/数据
        cursor.close()
        self.close_coon()
        return rest

    def get_more(self):
        # 准备 sql
        sql = 'SELECT * FROM `news` ORDER BY `created_at` DESC;'
        # 找到 cursor
        cursor = self.coon.cursor()
        # 执行 sql
        cursor.execute(sql)
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        # 处理数据
        print(rest)
        # 关闭cursor/数据
        cursor.close()
        self.close_coon()
        return rest


def main():
    obj = MysqlSearch()
    # obj.get_one()
    rest = obj.get_more()
    for item in rest:
        print(item)
        print("----------")


if __name__ == '__main__':
    main()
