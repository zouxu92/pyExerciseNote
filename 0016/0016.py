# -*- coding: utf-8 -*-
''' 将纯文本文件numbers.txt-->list形式，里面内容写入到numbers.xls中'''

import json
import xlwt

print(u'创建workbook对象')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('numbers') # 创建工作表

# 打开文件并进行读取
data = open('numbers.txt', 'r').read()
# print data

print(u"将字符串反序列化\n")
data2 = json.loads(data)

# 坐标起点
coord_x  = 0 

# 坐标循环，以及对应的数据循环添加到xls表中
while coord_x < len(data2):
	for i in data2:
		coord_y = 0
		while coord_y < len(i):
			for a in i:
				print (coord_x, coord_y, a)
				sheet.write(coord_x, coord_y , a)
				coord_y += 1
		coord_x += 1

# 保存文件
wbk.save('numbers.xls')