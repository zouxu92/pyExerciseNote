#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from PIL import Image

def picProcess(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		for f in files:
			print os.path.join(root, f).split('\\')[1]
			'''
			avatar = Image.open(os.path.basename(f))
			
			#print os.path.basename(f)
			w , h = avatar.size
			print w , h
			# 切割大小
			n = w/1366 if (w/1366) >= (h/640) else h/640
			avatar.thumbnail((w/n, h/n))
			avatar.save('new_'+ sourceFileName.split('.')[0]+'.jpg', 'jpeg')
			'''
def Test(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		#for d in dirs:
		#	print os.path.join(root, d)
		for f in files:
			print os.path.join(root, f)
			print os.path.split(f)[1]
			print "============="
			print os.path.basename(f)


if __name__ == "__main__":
	print "beging..."
	picProcess('E://python_ex//pyExerciseNote//test')
	#Test("E:\python_ex\pyExerciseNote\test")

	print "Endding!"
