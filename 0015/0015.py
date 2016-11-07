# -*- coding: utf-8 -*-
'''
将纯文本文件 city.txt为城市信息，写入到city.xls文件中。
同步上一题的进行写入操作，转换为json格式
'''
import json
import xlwt  

print(u'创建workbook对象')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('city') # 创建工作表

# 打开文件并且读取数据
data = open('city.txt' , 'r').read()
# print data

print(u"将字符串反序列化\n")
data2 = json.loads(data)
# print data2

# 将字符循环写人到city.xls 中
for k, value in data2.items():
	print k , value
	# 将值写人到city.xls 中
	sheet.write(int(k)-1, 0, k)
	sheet.write(int(k)-1, 1 , value)


# 保存文件
wbk.save('city.xls')








