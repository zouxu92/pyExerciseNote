# -*- coding:utf-8 -*-
'''读取txt文件(字典)用json格式装换成字典,将文件内容写入到xls里面0014'''

import json
import xlwt  


print(u'创建workbook对象')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('student') # 创建工作表

# 打开文件并读取内容
data = open('student.txt', "r").read()

print(u"将字符串反序列化\n")
data2 = json.loads(data)


print(u'循环字典输出值\n')
for k, value in data2.items():
	#print (k, value)
	sheet.write(int(k)-1, 0, k)
	num = 1
	for i in value:
		if num <= len(value):
			# 将k的值强转成int型，num的值从1开始，因为k值的0已经在前面添加
			sheet.write(int(k)-1, num , i)
			num += 1

# 保存文件
wbk.save('student.xls')


