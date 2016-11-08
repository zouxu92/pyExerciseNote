# -*- coding: utf-8 -*-

import xlrd
import xml.dom.minidom as md

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_xls_data(filename):
	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(0)
	content = {}
	for i in range(sheet.nrows):
		content[i+1] = sheet.row_values(i)[1:]
	return content


def write_to_xml(xlscontent):
	xmlfile = md.Document()  # 创建新xml文件

	root = xmlfile.createElement('root') # 创建节点
	students = xmlfile.createElement ( 'students' ) # 节点二

	xmlfile.appendChild(root) # 在文件中添加root节点
	root.appendChild(students) # root下的节点

	# 创建注释
	comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')

	students.appendChild(comment) # 在students 标签下添加comment

	xmlcontent = xmlfile.createTextNode(str(xlscontent).decode('utf-8')) # 创建文本节点
	students.appendChild(xmlcontent) # 在students标签下添加文本内容


	# 写入文件
	with open('students3.xml', 'w') as f:
		f.write(xmlfile.toprettyxml(newl = '\n', encoding = 'UTF-8'))
		f.close # 关闭文件

if __name__ == "__main__":
	write_to_xml(get_xls_data('student.xls'))