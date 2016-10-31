#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
-->解析：利用循环遍历目录，然后统计每个目录里面对应的每个词的数量
'''
import os
from collections import Counter
# 读取文件名，并循环出文件夹里面的文件
def readFile(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		for f in files:
			# 读取文件名
			print(os.path.join(root, f).split('\\')[1])
			# 读取文件内容，统计对应单词出现的次数
			readContent(os.path.join(root, f))

# 读取文件
def readContent(file):
	file_object = open(file, 'r')
	# 读取全部文件
	# print file_object.read()
	# print (u"=====我叫分割线======")
	'''
	print (u"将文件分行显示")
	while 1:
		file_s = file_object.readline()
		if file_s:
			print (file_s)
		else:
			break
	print ("kakakakakka")
	'''
	# 读取文件，并将文件全部转换成小写的
	fileContent = file_object.read().lower()
	cnt = Counter()
	# 过滤的单词
	stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'are', 'a', 'with', 'as', 'an', 'for', 'or']
	for word in fileContent.split():
		if word in stop_word:
			pass
		else:
			cnt[word] += 1
	# 统计单词出现的次数	显示出前五的数字
	# print (u"文件名为：%s 单词出现前五的如下：\n" % file.split('//')[5])
	
	print (u"文件名称为：%s 单词出现前五的如下： \n" % os.path.basename(file).split('.')[0] )
	print cnt.most_common(5)
	# 关闭文件
	file_object.close()

def test(rootDir):
	list_dirs = os.walk(rootDir)
	for root, dirs, files in list_dirs:
		for f in files:
			# 读取文件名
			# print(os.path.join(root, f).split('//')[5])
			print ("\n")
			# 读取文件内容，统计对应单词出现的次数
			readContent(os.path.join(root, f))
if __name__ == "__main__":
	# readFile("C://Users//admin//Desktop//book")
	# readContent("E://python_ex//pyExerciseNote//0004//mode.txt")
	test("E://python_ex//pyExerciseNote//0004//test//")