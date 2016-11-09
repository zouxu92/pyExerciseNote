# -*- coding: utf-8 -*-
'''将xls中的数字信息，写入到xml中
思路，将xls文件内容读出来转换为json格式,然后通过写入到xml中
'''
import xlrd
import json
import xml.dom.minidom as minidom
# 将系统设置成utf-8的格式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_xls_data(filename):
	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(0)
	content = []
	# 循环获取到数据
	for i in range(sheet.nrows):
		#print sheet.row_values(i)
		content.append(sheet.row_values(i))
	#return content
	# 返回json格式的字符
	return json.dumps(content, indent=4, ensure_ascii=False, encoding="utf-8", separators=(',', ': '))
'''
data = get_xls_data('numbers.xls')
data_json = json.dumps(data, indent=4, ensure_ascii=False, encoding="utf-8", separators=(',', ': '))
print data_json
'''

def write_to_xml(xlscontent):
	xmlfile = minidom.Document()  # 创建新xml文件

	root = xmlfile.createElement('root') # 创建节点
	numbers = xmlfile.createElement ( 'numbers' ) # 节点二s

	xmlfile.appendChild(root) # 在文件中添加root节点
	root.appendChild(numbers) # root下的节点

	# 创建注释
	comment = xmlfile.createComment('数字信息')

	numbers.appendChild(comment) # 在numbers标签下添加comment
	xmlcontent = xmlfile.createTextNode(str(xlscontent).decode('utf-8')) # 创建文本节点
	numbers.appendChild(xmlcontent) # 在numbers标签下添加文本内容

	with open('numbers.xml', 'w') as f:
		f.write(xmlfile.toprettyxml(newl = '\n', encoding = 'UTF-8'))
		f.close # 关闭文件

if __name__ == "__main__":
	write_to_xml(get_xls_data('numbers.xls'))

