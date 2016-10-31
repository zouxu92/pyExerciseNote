# -*- coding:utf-8 -*-

'''
namedtuple()
namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。

'''
from collections import namedtuple

websites = [
	('Sohu', 'http://www.google.com/', u'张朝阳'),
	('Sina', 'http://www.sina.com.cn', u'王志东'),
	('163', 'http://www.163.com', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
	website = Website._make(website)
	print (website)

