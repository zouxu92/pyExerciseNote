# -*- coding:utf-8 -*-
'''
第 0012 题： 敏感词文本文件 filtered_words.txt，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
-->利用正则匹配
'''
import re
def check(input, filtered_words):
	result=input
	for i in filtered_words:
		if i in result:
			r=re.compile(i) #把正则表达式的模式和标识转化成正则表达式对象
			result=r.sub('*'*len(i.decode('utf-8')), result)
			return result
	return input

file = open('filtered_words.txt','r')
# 将换行替换，返回列表
filtered_words=[line.replace('\n', '') for line in file]

# print filtered_words

if __name__ == "__main__":
	print(check('lovely boy', filtered_words))


