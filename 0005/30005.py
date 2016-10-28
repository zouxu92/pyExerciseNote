#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import os

def change_resolution(path):
	for picname in os.listdir(path):
		picpath = os.path.join(path, picname)
		with Image.open(picpath) as im:
			w, h = im.size
			n = w/1366 if (w/1366) >= (h/600) else h/640
			im.thumbnail((w/n, h/n))
			im.save('finish_' + picname.split('.')[0]+'.jpg', 'jpeg')

if __name__ == '__main__':
	change_resolution("E://python_ex//pyExerciseNote//test")


