import pandas as pd
import numpy as np
import sys


# ! /usr/bin/env python

input_file = sys.argv[1]
nianji = sys.argv[2]
outfile = ((nianji + '课程表生成') + '.xls')
df = pd.read_excel(input_file,header=None,sheet_name=nianji)
num = len(df)
df = np.array(df)
df = np.reshape(df,[5*num,9])
df = df.T
df = np.hsplit(df,num)
df = np.vstack(df)
df = pd.DataFrame(df)
df.columns = ['星期一','星期二','星期三','星期四','星期五']
df.insert( 0, '节数' , [i for i in range(1,10)]*num )
df.insert( 0 ,'班级' , [nianji+'('+str(x)+')班' for x in range(1,num+1) for y in range(9)])
df.rename(columns = {'班级':'', '节数':''},inplace = True)
df.to_excel(outfile,sheet_name = nianji+'级课程表',index=False )
print('执行成功')
