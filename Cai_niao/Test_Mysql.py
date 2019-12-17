import pymysql.cursors
import numpy as np
import pandas as pd

connect = pymysql.Connect(host='localhost', port=3306, user='root', passwd='68dxqiji', db='mysql', charset='utf8')
coursor = connect.cursor()

coursor.execute("SHOW DATABASES")
print(coursor.execute("SHOW DATABASES"))
