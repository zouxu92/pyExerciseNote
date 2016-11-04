# -*- coding: utf-8 -*-
import xlrd
import xlwt

# 打开Excle文件读取数据
data = xlrd.open_workbook('excelFile.xls')

# 获取一个工作表
table = data.sheets()[0]  # 通过索引顺序获取
# data.sheet_by_index(0)
table1 = data.sheet_by_name(u'Sheet1')  # 通过表名获取
print (table)
print (table1)

print (u'检查表单名字')
print (data.sheet_names())

print(u'获取整行和整列的值')
#print (table.row_values(Sheet1))


print(u'获取行数和列数')

nrows = table.nrows
ncols = table.ncols

print(u'行数是：%d， 列数是：%d \n' %(nrows, ncols))

print(u'递归出每行的信息')
for rownum in range(nrows):
	print table.row_values(rownum)

print(u'单元格')
cell_1 = table.cell(0,1).value
cell_2 = table.cell(1,0).value
cell_3  = table.cell(7,3).value
print(u'cell_1 >> %s \ncell_2 >> %s \ncell_3 >> %s \n' % (cell_1, cell_2, cell_3))

print(u'使用行列索引\n')
A1 = table.row(0)[0].value
A2 = table.col(1)[0].value

A3 = table.row(1)[0].value
A4 = table.col(3)[7].value
print (u"A1: %s \nA2: %s \n" %(A1, A2))

print (u"A3: %s \nA4: %s \n" %(A3, A4))
