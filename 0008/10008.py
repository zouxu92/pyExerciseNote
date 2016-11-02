#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
这里对SGMLParser类进行简单的学习和实践过程
'''

import urllib,time
# 导入sgmllib中分享网页的SGMLParser模块
from sgmllib import SGMLParser
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class MySGMLParser(SGMLParser):
	# 重写SGMLParser模块中的reset
	def reset(self):
		# 调用原来的函数reset
		SGMLParser.reset(self)
		# 数据存放位置
		self.data = []
		self.lable = False
		self.url = []


	# 查找标签（start_ + 标签）表示查找的那个标签（参数是固定的）
	def start_a(self, attrs):
		# 查找对象的标签里面的属性(此处用到了列表解析)
		href = [v for k,v in attrs if k == 'href']
		# 判断href 是不是存在
		if href:
			self.url.extend(href)
		self.lable = True

	# 查找结束标志
	def end_a(self):
		self.lable = False
	# 处理信息数据的地方
	def handle_data(self, data):
		# 判断标签数不超找完毕
		if self.lable:
			data = data.strip()
			self.data.append(data)


class ParserData():
	def __init__(self, urlpath):
		self.urlpath = urlpath
		self.dealData()
		print ("############")


		print locals()
		print ("###########")

	# 读取url路径的
	def readData(self):
		data = None
		# 访问的地址是不是存在，不存在抛出异常
		try:
			data = urllib.urlopen(self.urlpath)
		except IOError, e:
			print (u'地址不存在')
		return (data)


	# 处理数据
	def dealData(self):
		# 对上述的类实例化
		parser = MySGMLParser()
		# 获取访问url的对象
		data = self.readData()
		if data != None:
			# 调用定义在SGMLParser中的feed方法，将HTML内容放入分析器中(feed传值为字符串) 
			parser.feed(data.read())
			self.closeData(data, parser,)
			# 遍历查找的数据
			for i in parser.url:
				if i.startswith('http'):
					print('url: %s ' %i)

			for i in parser.data:
				print ('data: %s ' % unicode(i,'utf-8'))

	def closeData(self, data, parser):
		parser.close()
		data.close()

if __name__ == "__main__":
	urlpath = 'http://www.baidu.com'
	data = ParserData(urlpath)