#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
遍历文件夹中的文件名称，可区分文件或者是文件夹
'''
import os
from PIL import Image
# 方法一，使用的 os.walk:
def Test(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		#for d in dirs:
		#	print os.path.join(root, d)
		for f in files:
			# print os.path.join(root, f)
			print "============="
			print os.path.basename(f)
			
'''
			with Image.open(os.path.join(root, f)) as avatar:
				#  制作缩略图：
				w , h = avatar.size
				print w , h
				n = w/1366 if (w/1366) >= (h/640) else h/640
				avatar.thumbnail((w/n, h/n))
				avatar.save('.//finish//new_'+ sourceFileName.split('.')[0]+'.jpg', 'jpeg')
'''


# 方法二，使用os.listdir:
def Test2(rootDir):
	for lists in os.listdir(rootDir):
		path = os.path.join(rootDir, lists)
		print path
		if os.path.isdir(path):
			Test2(path)

if __name__ == "__main__":
	Test("E://python_ex//pyExerciseNote//test")