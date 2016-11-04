# -*- coding:utf-8 -*-
import xlwt

print(u'创建workbook对象')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('studay')

# 写入数据
sheet.write(0,1, 'test test')


# 这里如果修改数据，将会报错，利用cell_overwrite_ok=True来进行修改数据解决这个问题
#sheet.write(0,1, 'opps')

sheet2 = wbk.add_sheet('sheet2', cell_overwrite_ok=True)

sheet2.write(0,1, 'some text')
sheet2.write(0,1, "aaaa")

print(u'保存文件')
wbk.save('test.xls')
