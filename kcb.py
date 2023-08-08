#! /usr/bin/env python
import pandas as pd
import numpy as np
import os
for fname in os.listdir('./'):
    if fname.endswith('.xls') || fname.endswith('.xlsx'):
        dic = pd.read_excel(fname,header=None,sheet_name=None)
        for key,value in dic.items():
            if not value.empty:
                num = len(value)
                df = np.array(value)
                try:
                    df = np.reshape(df,[5*num,9])
                    df = df.T
                    df = np.hsplit(df,num)
                    df = np.vstack(df)
                    df = pd.DataFrame(df)
                    df.columns = ['星期一','星期二','星期三','星期四','星期五']
                    df.insert( 0, '节数' , [i for i in range(1,10)]*num )
                    df.insert( 0 ,'班级' , [key+'('+str(x)+')班' for x in range(1,num+1) for y in range(9)])
                    df.rename(columns = {'班级':'', '节数':''},inplace = True)
                    df.to_excel(key+'生成.xlsx',sheet_name = key+'级课程表',index=False )
                except:
                    print(fname+'   '+key+'   '+'表的格式不正确')
            else:
                print(fname+'   '+key+'   '+'是空表')
print('执行成功')
os.system('pause')