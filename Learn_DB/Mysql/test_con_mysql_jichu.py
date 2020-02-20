import MySQLdb

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', password='68dxqiji', db='news', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `news`;")
    rest = cursor.fetchall()
    print(rest)
    cursor.close()

except MySQLdb.Error as e:
    print("Error: " + e)
