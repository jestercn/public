import pandas as pd
import os
print('-'*50)
print('*'*5+'  统计成绩的折算总分和平均分  '+'*'*5)
print('-'*50)
zongfen = 0
while True:
    fname = input('请输入成绩表格文件全名:>')
    fname = fname.strip()
    if os.path.exists(fname):
        break
    else:
        print('输入的文件不存在')
df = pd.read_excel(fname)
bili = pd.read_excel('科目及权重.xlsx',header=None,index_col=0)
kemu = list(bili.index)
r = [ i for i in df.columns if i in kemu ]
print('考试科目有 '+str(len(r)) +' 科')
def chfenshu(x):
    percent = bili.at[x,1]
    print(x+'    权重值'+str(percent))
    return df[x]*percent
for x in r:
    zongfen += chfenshu(x)
df['折算总分'] = zongfen
df.loc[len(df),r] = df[r].mean()
df.to_excel('new_'+ fname,index=False)
print('-'*50)
print('程序执行完毕')
print('-'*50)
os.system('pause')
    
    
