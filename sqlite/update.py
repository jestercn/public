#! /usr/bin/python
import sqlite3
db_name = 'dbase'
conn = sqlite3.connect(db_name)
print('数据库连接成功')
try:
	curs = conn.cursor()
	sql = '''
			update student set name='张三',carno='13905949999' where carno='350321197809095959'
			'''
	curs.execute(sql)
	conn.commit()
	print('更新数据成功')
except Exception as e:
	print(e)
	conn.rollback()
	print('更新数据失败')
finally:
	conn.close()
