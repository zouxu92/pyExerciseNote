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

key_val='86RW3JRF4QD2'
# SQL 插入sql语句
sql = "INSERT INTO CDKEY ( key_val, used) VALUES ( '%s', 0) "  % key_val  

try:
	# 执行sql语句
	cursor.execute(sql)
	# 提交到数据库执行
	db.commit()
except:
	# 发生错误时回滚
	db.rollback()

# 关闭数据库
db.close()	
