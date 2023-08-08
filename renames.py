import os
import pandas as pd
list_name = []
find_name =[]
count = 0
print("-"*50)
print('======ptbzjwc利用EXCEL表格，批量自动重命名======')
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
df = pd.read_excel( fname, header = None,index_col=0,sheet_name=0 ).astype(str)
df.index=df.index.astype(str)
for oldname in os.listdir('./'):
    if oldname.lower().endswith(form):
        sname = oldname.split('.')
        sname = sname[:-1]
        sname = '.'.join(sname)
        
        try:
            newname = df.loc[sname,1]
            os.rename(oldname,newname+form)
            find_name.append(newname)
            count +=1
        except KeyError:
            list_name.append(oldname)
            print(oldname+'   找不到')     
        except TypeError:
            list_name.append(oldname)
            print(oldname+'   有同名')
        except FileExistsError:
            list_name.append(oldname)
            print(oldname+'   更名的文件已存在')
print("-"*50)
print("程序运行结束了")
print("-"*50)
if list_name:
    print("请注意，以上重命名失败的文件"+str(len(list_name))+'个')
elif count :
    print("恭喜您，所有文件重命名成功！")
print("-"*50)
print(str(count)+'个文件成功重命名，详细请查看产生的更名结果表格。')
print("-"*50)
writer=pd.ExcelWriter("更名结果.xlsx")
if list_name:
    df1=pd.DataFrame(list_name)
    df1.columns = ["失败名单"]
    df1.to_excel(writer,sheet_name="失败名单",index=False)
if find_name:
    df2=pd.DataFrame(find_name)
    df2.columns =[ "成功名单"]
    df2.to_excel(writer,sheet_name="成功名单",index=False)
writer.save()
os.system('pause')