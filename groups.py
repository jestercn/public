import pandas as pd
import os
input_file = input('  请输入表格的文件名全称:>')
group_name = input('  请输入要分组的字段名称:>')
output_file = 'new_'+input_file
iris = pd.read_excel(input_file)
class_list = list(iris[group_name].drop_duplicates())
writer = pd.ExcelWriter(output_file)
for i in class_list:
	iris1 = iris[iris[group_name]==i]
	iris1.to_excel(writer,sheet_name=i,index=False)
writer.save()
writer.close()
print('程序运行结束')
os.system('pause')