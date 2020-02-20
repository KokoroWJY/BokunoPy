import MySQLdb


class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            # 获取连接
            self.conn = MySQLdb.connect(host='127.0.0.1', user="root", password='68dxqiji', db='news', port=3306,
                                        charset="utf8")
        except MySQLdb.Error as e:
            print("Error %s" % e)

    def close_coon(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print("Eorr %s" % e)

    def get_one(self):
        # 准备 sql
        sql = 'SELECT * FROM `news` ORDER BY `created_at` DESC;'

        # 找到 cursor
        cursor = self.conn.cursor()

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
        cursor = self.conn.cursor()
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

    def add_one(self):
        try:
            # 准备SQL
            sql = 'INSERT INTO `news` (`title`, `content`, `types`, `image`) VALUES (%s, %s, %s, %s);'
            # 获取连接和cursor
            cursor = self.conn.cursor()
            # 执行sql
            # 提交数据到数据库
            cursor.execute(sql, ("标题1", "新闻内容1", "推荐", "/static/img/news/01.png"))
            # 提交事务
            self.conn.commit()
            # 关闭cursor连接
            cursor.close()
            self.conn.close()
        except:
            print("Error")
            self.conn.rollback()

def main():
    obj = MysqlSearch()
    # obj.get_one()

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)
    #     print("----------")

    obj.add_one()


if __name__ == '__main__':
    main()
