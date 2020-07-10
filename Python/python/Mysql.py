import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","unix","test" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# SQL 查询语句
# sql = "SELECT * FROM emp"
sql = """CREATE TABLE `user8`  (
        `id` int(10) NOT NULL
        )"""
#sql = """CREATE TABLE `user3`  (
#  `id` int(10) NOT NULL
#) """
try:
   # 执行SQL语句
   cursor.execute("DROP TABLE IF EXISTS user8")
   # 获取所有记录列表
   sql = """CREATE TABLE `user8`  (
            `id` int(10) NOT NULL
            )"""
   cursor.execute(sql)
except:
   print ("Error: unable to fetch data")
 
# 关闭数据库连接
db.close()
