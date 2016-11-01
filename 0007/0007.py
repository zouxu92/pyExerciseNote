#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os, re

# 代码所在目录
FILE_PATH = 'E://python_ex//pyExerciseNote//0007'

def analyze_code(codefilesourec):
	'''
	打开一个py文件，统计其中的代码行数，包括空格和注释
	返回含有该文件总行数，注释行数，空行数的列表
	'''
	total_line = 0
	comment_line = 0
	blank_line = 0
	with open(codefilesourec) as f:
		lines = f.readlines()
		total_line = len(lines)
		line_index = 0
		# 遍历每一行
		while line_index < total_line:
			line = lines[line_index]
			# 检查是否为注释
			if line.startswith('#'):
				comment_line += 1
			elif re.match("\s*'''", line) is not None:
				comment_line += 1
				while re.match(".*'''$", line) is None:
					line = lines[line_index]
					comment_line += 1
					line_index += 1
			# 检查是否为空行
			elif line == "\n":
				blank_line += 1
			line_index += 1
		print (u"在%s中：" % codefilesourec)
		print (u"代码行数：%d" % total_line)
		print (u"注释行数：%d " % comment_line + u"占%0.2f%%" % (comment_line*100.0/total_line))
		print (u"空行数：%d " % blank_line + u"占%0.2f%%" % (blank_line*100.0/total_line) + "\n")
		return [total_line, comment_line, blank_line]

def run(FILE_PATH):
	# 切换到code所在目录
	os.chdir(FILE_PATH)
	# 遍历目录下的py文件
	total_lines = 0
	total_comment_lines = 0
	total_blank_lines = 0
	for i in os.listdir(os.getcwd()):
		if os.path.splitext(i)[1] =='.py':
			line = analyze_code(i)
			total_lines, total_comment_lines, total_blank_lines = total_lines + line[0] , total_comment_lines + line[1], total_blank_lines + line[2]

	print (u"\n开始统计总数\n总代码行数：%d " % total_lines)
	if total_lines==0:
		pass
	else:
		print (u"总注释行数：%d " % total_comment_lines + u"占%0.2f%%" % (total_comment_lines*100.0/total_lines))
		print (u"总空行数：%d " % total_blank_lines + u"占%0.2f%%" % (total_blank_lines*100.0/total_lines))
		print ("\n===end=====")

if __name__ == "__main__":
	run(FILE_PATH)