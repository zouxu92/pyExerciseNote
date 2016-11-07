# -*- coding:utf-8 -*-
'''生成对应的xml文件练习'''
import xml.dom.minidom as Dom

# 创建对象
doc = Dom.Document()
root_node = doc.createElement('root') # 创建根目录

#root_node.setAttribute('name', 'students')     # 添加相应的属性
#root_node.setAttribute("website", "http://www.126.com")

doc.appendChild(root_node) # 继承子类

# 创建root下面的子类
students_node = doc.createElement("students")  # 标签名字

data = u"""
<!-- 
    学生信息表
    "id" : [名字, 数学, 语文, 英文]
-->
{
    "1" : ["张三", 150, 120, 100],
    "2" : ["李四", 90, 99, 95],
    "3" : ["王五", 60, 66, 68]
}
"""

students_value = doc.createTextNode("%s" % data)


students_node.appendChild(students_value) # 将值赋予students标签下面

root_node.appendChild(students_node) # 将students标签赋予在root标签下

f = open('students.xml', 'w')
f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'UTF-8'))
f.close




