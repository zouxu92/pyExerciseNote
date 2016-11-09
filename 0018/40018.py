# -*- coding:utf-8 -*-
'''将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中'''
import xlrd
import json
from collections import OrderedDict
import xml.dom.minidom as minidom
#import HTMLParser

# 将系统设置成utf-8的格式
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_xls_data(fileName):
	book = xlrd.open_workbook(fileName)  # 获取对象
	sheet = book.sheet_by_index(0)      # 获取工作目录
	d = OrderedDict()
	for i in range(sheet.nrows):
		# 读一行，存放到dict中
		values = map(lambda x: x.encode('UTF8') if isinstance(x, unicode) else x, sheet.row_values(i))
		d[values[0]] = values[1]
	return d #json.dumps(d, indent=4,ensure_ascii=False, encoding='utf-8').decode('utf-8')

# 将字典里面的数据装换为正确的中文
json_data = json.dumps(get_xls_data('city.xls'), indent=4,ensure_ascii=False, encoding='utf-8')
# print json_data.decode('utf-8')

def writeXml(xlscontent):
	xmlfile = minidom.Document()  # 创建新xml文件
	root = xmlfile.createElement('root') # 创建节点
	citys = xmlfile.createElement ( 'citys' ) # 节点二

	xmlfile.appendChild(root) # 在文件中添加root节点
	root.appendChild(citys) # root下的节点

	# 创建注释
	comment = xmlfile.createComment('城市信息')
	citys.appendChild(comment) # 在students 标签下添加comment

	xmlcontent = xmlfile.createTextNode(json_data.decode('utf-8'))#str(xlscontent).decode('utf-8')) # 创建文本节点
	#print xmlcontent.toxml().replace('&quot;', '"')
	citys.appendChild(xmlcontent) # 在students标签下添加文本内容

	'''
	html_parser = HTMLParser.HTMLParser()
	tranform = html_parser.unescape(xmlcontent.toxml().decode('utf-8'))
	print tranform
	print (root.toxml().decode('utf-8').replace('&quot;', '"'))
	'''

	# 写入文件
	with open('city.xml', 'w') as f:
		#f.write(xmlfile.toxml().decode('utf-8').replace('&quot;', '"'))
		# 这里解决引号的办法，直接用replace('old','new') 替换
		f.write(xmlfile.toprettyxml(newl = '\n', encoding = 'UTF-8').replace('&quot;', '"'))
		f.close # 关闭文件

if __name__ == "__main__":
	writeXml(get_xls_data('city.xls'))


'''  废弃，创建标签，对里面内容进行转换
def makeEasyTag(minidom, tagname, value, type='text'):
	tag = minidom.createElement(tagname)
	if value.find(']]>') > -1:
		type = 'text'
	if type == 'text':
		value = value.replace('&', '&amp;')
		value = value.replace('<', '&lt;')
		text = minidom.createTextNode(value)
	elif type == 'cdata':
		text = minidom.createCDATASection(value)
	tag.appendChild(text)
	return tag

makeEasyTag(minidom, 'test', json_data, json_data)
print (makeEasyTag(minidom, 'test', json_data, json_data))
'''
