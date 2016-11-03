#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('gbk')
'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

charsList = []
# 读取文件，将文件的词语填入到列表中
def readFilteredWords(file):
	open_file = open(file, "r")
	for chars in open_file.read().split('\n'):
		# 将字符装换成utf-8编码，并添加进入到列表
		charsList.append(chars.decode('utf-8'))
	return charsList

def sensitiveChange():
	# 用户输入
	char = raw_input(u"请输入你需要的文字:")
	print (char)
	



if __name__ == "__main__":
	print (readFilteredWords("E://python_ex//pyExerciseNote//0011//filtered_words.txt"))
	sensitiveChange()