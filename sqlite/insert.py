#! /usr/bin/python
import sqlite3
db_name = 'dbase'
conn = sqlite3.connect(db_name)
print('数据库连接成功')
try:
		curs = conn.cursor()
		sql = '''
             insert into student values('郑成功','350321197809095959','福建省莆田市荔城区北高镇呈山村')
               '''
		curs.execute(sql)
		conn.commit()
		print('插入数据到表student成功')
except Exception as e:
       print(e)
       conn.rollback()
       print('插入数据到表student失败')
finally:
        conn.close()
