# -*- coding: utf-8 -*-

''' 坐标循环'''

x, y = 0,0 

x_max = 3
y_max = 4

while (x < x_max ):
	# print x , y
	y = 0
	while (y < y_max):
		print (x, y)
		y +=1
	x += 1
	
