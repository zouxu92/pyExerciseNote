#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
PIL相关练习--》图片处理
'''
from PIL import Image
import os

# 图片名字
sourceFileName = ".//test//test.jpg"
# 打开图片
avatar = Image.open(sourceFileName)
print (sourceFileName)
# 图片的相对属性
'''
Image 类的实例有 5 个属性，分别是：

format: 以 string 返回图片档案的格式（JPG, PNG, BMP, None, etc.）；如果不是从打开文件得到的实例，则返回 None。
mode: 以 string 返回图片的模式（RGB, CMYK, etc.）；完整的列表参见 官方说明·图片模式列表
size: 以二元 tuple 返回图片档案的尺寸 (width, height)
palette: 仅当 mode 为 P 时有效，返回 ImagePalette 示例
info: 以字典形式返回示例的信息
'''
print (avatar.format, avatar.size, avatar.mode, avatar.info)

#  制作缩略图：
w , h = avatar.size

n = w
print('====')
print(n)
aa = w/1366
print (aa)

print ("========")


print w , h
n = w/1366 if (w/1366) >= (h/640) else h/640
avatar.thumbnail((w/n, h/n))
avatar.save('.//finish//new_'+ sourceFileName.split('//')[2].split('.')[0]+'.jpg', 'jpeg')


