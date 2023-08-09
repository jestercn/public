#! /usr/bin/python
import sqlite3
db_name = 'dbase'
conn = sqlite3.connect(db_name)
print('数据库连接成功')
try:
	curs = conn.cursor()
	sql = '''
			select * from student
			'''
	curs.execute(sql)
	for row in curs.fetchall():
				print(row)
				print('查询数据成功')
except Exception as e:
	print(e)
	print('查询数据失败')
finally:
	conn.close()
