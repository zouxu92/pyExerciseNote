# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('gbk')

print (u"以读的方式打开文件")
open_file = open("E://python_ex//pyExerciseNote//0011//filtered_words.txt", "r")

charsList = []
print (u"将文件内容按照每行输出\n")
for chars in open_file.read().split('\n'): 
	charsList.append(chars.decode('utf-8'))
print(u"\n关闭文件")
open_file.close()

# 输入内容
char = raw_input("Enter your input:")

if char in charsList:
	print ("Freedom")
else:
	print ("Human Rights")
# print charsList

print(u'程序结束!')
