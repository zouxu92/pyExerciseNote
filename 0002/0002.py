#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.88.114","root","zx123456","test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用ececute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取一条数据库
data = cursor.fetchone()

print ("Database version: %s" % data)

# 关闭数据库连接
db.close()


print ("Hello!")