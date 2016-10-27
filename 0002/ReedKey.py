#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

# 打开文件
file_object = open ("keyData.txt",  "r")
print file_object.name
i=0
for line in file_object.readlines():
	i+=1
	print (i)
	print (line.split(' ')[2])

file_object.close()

print (file_object.close())
'''
print ("----------我叫分割线------------")
aa = file_object.readline()
print (aa)
m = aa.split(' ')[2]
print(m)
#for item in m:
#	print (item)
'''

print ("----------------")
#file_object.close()