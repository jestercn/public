#! /usr/bin/python
import sqlite3
db_name = 'dbase'
conn = sqlite3.connect(db_name)
print('数据库连接成功')
try:
		curs = conn.cursor()
		sql = '''
             delete from student where name='郑成功'
               '''
		curs.execute(sql)
		conn.commit()
		print('删除数据成功')
except Exception as e:
       print(e)
       conn.rollback()
       print('删除数据到表student失败')
finally:
        conn.close()
