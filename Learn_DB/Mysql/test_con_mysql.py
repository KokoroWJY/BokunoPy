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
                coon.close()
        except MySQLdb.Error as e:
            print("Eorr %s" % e)
            
# 获得数据
cursor = coon.cursor()
cursor.execute('SELECT * FROM `news` ORDER BY `created_at` DESC')
rest = cursor.fetchone()
print(rest)