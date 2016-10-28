#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PIL import Image
'''
读取一个文件夹，然后，读取文件，对文件进行处理操作
并保存到新的文件夹里面
'''
def picProcess(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		for f in files:
			# 这里获取文件的名称对文件进行处理
			#print (os.path.join(root, f).split('\\')[1])
			#print (os.path.join(root, f))
			avatar = Image.open(os.path.join(root, f))
			# 制作缩略图
			w, h = avatar.size
			print(w,h)
			n = w/1366
			# 这里增加一个条件，n>0时进行缩放，否则不改变大小
			if (n>0):
				n  if (w/1366) >= (h/640) else h/640
				avatar.thumbnail((w/n, h/n))
			# 保存图片
			avatar.save('.//finish//new_'+ os.path.join(root, f).split('\\')[1].split('.')[0]+'.jpg', 'jpeg')


''' 可以利用第二种方法，改变os的读取
def picProcess2(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		#for d in dirs:
		#	print os.path.join(root, d)
		for f in files:
			print os.path.join(root, f)
			print os.path.split(f)[1]
			print "============="
			print os.path.basename(f)
'''


if __name__ == "__main__":
	#picProcess2("E://python_ex//pyExerciseNote//0005//test")
    picProcess("E://python_ex//pyExerciseNote//0005//test")