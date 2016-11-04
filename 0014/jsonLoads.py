# -*- coding:utf-8 -*-
'''读取字典数据，将装换成json格式'''

import json


data = open('student.txt', "r").read()# .decode('utf-8')
print (data)

print(u"将字符串反序列化\n")
data2 = json.loads(data)
print(data2)

print(u'循环字典输出值\n')
for k, value in data2.items():
	print (k, value)
	for i in value:
		print (k,i)

