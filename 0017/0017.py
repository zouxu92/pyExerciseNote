# -*- coding:utf-8 -*-
'''将student.xls文件中内容，写到student.xml文件中
思路，将信息取出来，变成字典格式，然后写入xml
'''
import xlrd
import xml.dom.minidom as Dom
# 打开excel文件读取数据，并返回工作表
table = xlrd.open_workbook('student.xls').sheet_by_name(u'student') # 通过名字获取
print (table)

# 穿件一个空字典
dict_data = {}
# 获取行数和列数
print (table.nrows, table.ncols)

# 循环，将数据变成字典返回
nrows= 0
while nrows < table.nrows :
	list_data = []
	ncols = 1
	while ncols < table.ncols:
		list_data.append(table.cell(nrows, ncols).value)
		# print list_data
		ncols += 1
	dict_data[table.cell(nrows, 0).value] = list_data
	nrows += 1
print (dict_data)

if __name__ == "__main__":
	# 生成xml文件：
	doc = Dom.Document()
	root_node = doc.createElement('root') # 创建根目录
	doc.appendChild(root_node) # 继承子类

	# 创建root下面的子类
	students_node = doc.createElement("students")  # 标签名字
	data = u"""
	<!-- 
	    学生信息表
	    "id" : [名字, 数学, 语文, 英文]
	-->
	"""
	students_value = doc.createTextNode("%s%s" % (data, dict_data))

	students_node.appendChild(students_value) # 将值赋予students标签下面

	root_node.appendChild(students_node) # 将students标签赋予在root标签下

	f = open('students.xml', 'w')
	f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'UTF-8'))
	f.close




