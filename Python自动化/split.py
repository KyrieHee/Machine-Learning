# 支持 Excel 读取的扩展库叫做 xlrd 库，支持 Excel 写入的扩展库叫做 xlwt 库
# pip3 install xlrd xlwt

# 读文件
import xlrd

file = '/Users/yun/Desktop/a.xlsx'

data = xlrd.open_workbook(file)
table = data.sheets()[0]
value = table.cell_value(rowx=4, colx=4)



import xlwt

dst_file = '/Users/yum/Desktop/result.xlsx'

workbook = xlwt.Workbook(encoding='utf-8')
xlsheet = workbook.add_sheet("统计结果")

# 写入内容,假设取出的内容是value
xlsheet.write(0, 0, value)

# 保存文件
workbook.save(dst_file)
