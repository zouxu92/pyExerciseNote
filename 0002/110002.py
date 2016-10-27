#!/usr/bin/python
# -*- coding: UTF-8 -*-
##########################
####    创建数据库    ####
##########################
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("192.168.88.114","root","zx123456","test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据包已经存在使用 execute() 方法删除表
cursor.execute("DROP TABLE IF EXISTS CDKEY")

# 创建数据表SQL语句
sql = """CREATE TABLE `CDKEY` (
`id`  int(5) NOT NULL AUTO_INCREMENT ,
`key`  varchar(12) NULL ,
PRIMARY KEY (`id`)
);"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
