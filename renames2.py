import os
import pandas as pd
list_name = []
count = 0
print("-"*50)
print('======利用EXCEL表格，批量自动重命名======')
print("-"*50)
while True:
    fname = input('请输入表格文件的全名:>')
    if os.path.exists(fname):
        break
    else:
        print('输入的文件不存在')
        print("-"*50)
form = '.'+input('请输入要重命名的文件类型:>')
print("-"*50)
df = pd.read_excel( fname, header = 0,sheet_name=0 ).astype(str)
df.set_index("原文件名",inplace=True)
for oldname in os.listdir('./'):
    if oldname.endswith(form):
        sname = oldname.split('.')
        sname = sname[:-1]
        sname = '.'.join(sname)
        
        try:
            newname = df.loc[sname,"新文件名"]
            os.rename(oldname,newname+form)
            print(sname,'======>',newname)
            count +=1
        except KeyError:
            list_name.append(oldname+'   找不到')     
        except TypeError:
            list_name.append(oldname+'   有同名')
        except FileExistsError:
            list_name.append(oldname+'   更名的文件已存在')
print("-"*50)
print("程序运行结束了")
print("-"*50)
if list_name:
    print("请注意，以下为重命名失败的文件"+str(len(list_name))+'个')
    for name in list_name:
        print(name)
elif count :
    print("恭喜您，所有文件重命名成功！")
print("-"*50)
print(str(count)+'个文件成功重命名')
print("-"*50)
os.system('pause')