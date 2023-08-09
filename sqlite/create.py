#! /usr/bin/python
import sqlite3
db_name = 'dbase'
conn = sqlite3.connect(db_name)
print('数据库连接成功')
try:
		curs = conn.cursor()
		sql = ''' create table student 
		(
		   name char(10),
          carno varchar(20),
          adress char(50)
            )
            '''
		curs.execute(sql)
		conn.commit()
		print('创建数据库表成功')
except Exception as e:
     print(e)
     conn.rollback()
     print('创建数据库表失败')
finally:
      conn.close()
