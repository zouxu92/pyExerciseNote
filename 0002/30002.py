#!/usr/bin/python
# -*- coding: UTF-8 -*-
##########################
####    插入数据库    ####
##########################
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.88.114","root","zx123456","test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 打开文件
file_object = open ("keyData.txt",  "r")

# for 循环将文件的码插入到数据库
for line in file_object.readlines():
	# 利用切割(空格)，截取第三份数据sql插入
	sql = "INSERT INTO CDKEY ( key_val, used) VALUES ( '%s', 0) "  % line.split(' ')[2]  
	try:
		# 执行sql语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
	except:
		# 发生错误时回滚
		db.rollback()
		
# 关闭文件
file_object.close()
# 关闭数据库连接
db.close()

print ("operation complete!")
