import pandas as pd
import os
print('-'*50)
print('*'*5+'实现两个表格的数据全部对齐功能'+'*'*5)
print('-'*50)
while True:
    left_file = input('请输入左表格文件的全名:>')
    left_file = left_file.strip()
    if os.path.exists(left_file):
            break
    else:
            print('输入的文件不存在')
print('-'*50)
while True:
    right_file = input('请输入右表格文件的全名:>')
    right_file = right_file.strip()
    if os.path.exists(right_file):
            break
    else:
        print('输入的文件不存在')
print('-'*50)
key_work = input('请输入关键字段，可以有多个:>')
print('-'*50)
argw = key_work.split()
df_left = pd.read_excel(left_file,sheet_name=0)
df_right = pd.read_excel(right_file,sheet_name=0)
try:
    df_result = pd.merge(df_left,df_right,on=argw,how='outer',suffixes=['_left','_right'], indicator='比较结果')
    df_result.to_excel('左右表格全对齐.xlsx',index=False)
    print('程序执行完毕，表格已经输出')
except KeyError:
    print('输入的关键字段有误')
print('-'*50)
os.system('pause')
