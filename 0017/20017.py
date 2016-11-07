# -*- coding: utf-8 -*-

import json
import xlrd
from collections import OrderedDict  # 为了保证位置不会改变
import xml.dom.minidom as minidom
import HTMLParser

# 存放文件的路径
filepath = 'E://python_ex//pyExerciseNote//0017//student.xls'
xmlpath = 'E://python_ex//pyExerciseNote//0017//student.xml'
comment = '''
	<!--
        学生信息表
        "id" : [名字, 数学, 语文, 英文]
    -->
'''

def readDataToJson():
	# 打开表格
	data = xlrd.open_workbook(filepath)
	sheet = data.sheet_by_index(0) # 索引找到工作表
	# 使用orderdict读取，确保元素位置一致
	d = OrderedDict()
	for i in range(sheet.nrows):
		# 读一行，存放到dict中
		values = map(lambda x: x.encode("UTF8") if isinstance(x, unicode) else x, sheet.row_values(i) )
		d[values[0]] = values[1:]
	return d

class MakeXml():
	def __init__(self, xmlpath):
		self.xmlpath = xmlpath
		self.dom = minidom.DOMImplementation().createDocument(None, 'root', None)
		self.root = self.dom.documentElement

	def creat_node(self, node_name, node_text=None, comment=None):
		if None == node_text:
			newNode = self.dom.createElement(node_name)
		else:
			if None != comment:
				newText = self.dom.createTextNode(comment+node_text)
			else:
				newText = self.dom.createTextNode(node_text)
			newNode = self.dom.createElement(node_name)
			newNode.appendChild(newText)
		return newNode

	def add_chile(self, item, comment=None):
		# 注意中文问题
		new_node = self.creat_node('student', json.dumps(item, indent=4, ensure_ascii=False, encoding='utf-8', separators=(',',':')), comment)
		self.root.appendChild(new_node)

	def save(self):
		# 直接writexml 会转义掉字符
		# Node.toxml会返回字符串格式的DOM
		with open(self.xmlpath, 'w') as f:
			html_parser = HTMLParser.HTMLParser()
			tranform = html_parser.unescape(self.dom.toxml().decode('utf-8'))
			f.write(tranform.encode('utf-8'))

if __name__ == "__main__":
	newxml = MakeXml(xmlpath)
	newxml.add_chile(readDataToJson(), comment)
	newxml.save()


