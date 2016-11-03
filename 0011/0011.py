# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
思路：先循环遍历文件内容，然后用户输入时遍历是否有对应的敏感词在里面。
'''
import sys
type = sys.getfilesystemencoding()
#print myname.decode('utf-8').encode(type)

'''
print (u"以读的方式打开文件")
open_file = open("filtered_words.txt", "r")
print (u"将文件内容按照每行输出\n")
for chars in open_file.readlines():
	print (chars.decode('utf-8'))
print(u"\n\n关闭文件")
open_file.close()
'''
listwd = []
def readFilteredWords(file):
	open_file = open(file, "r")
	lines = open_file.readlines()
	for line in lines:
		#listwd = listWords.append(line)
		listwd.append(line.decode('utf-8').encode(type))
		#print listWords.append(line.decode("utf-8"))
		# return (line.decode('utf-8'))
	return listwd
	open_file.close()
	#return listwd

if __name__ == "__main__":
	print readFilteredWords("E://python_ex//pyExerciseNote//0011//filtered_words.txt")
	#print (readFilteredWords("E://python_ex//pyExerciseNote//0011//filtered_words.txt"))
	char = input("Enter your input:")

	if char in readFilteredWords("E://python_ex//pyExerciseNote//0011//filtered_words.txt"):
		print ("Freedom")
	else:
		print ("Human Rights")
	
	print (u"程序结束！")

