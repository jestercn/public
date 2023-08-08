import random
import os
names =['A1','A2','A3','A4','A5','A6','A7','A8','B1','B2','B3','B4','B5','B6','B7','B8','C1','C2','C3','C4','C5','C6','C7','C8']
random.shuffle(names)
print("\n")
try:
    with open("out.csv",'w') as f:
        for i in range(24):
            print('   第 {:2s} 号为 {:2s} '.format(str(i+1),names[i]),end="")
            if (i+1)%6==0:
                print("\n   "+"_"*99)
                print("\n")
                
            f.write(names[i]+'\n')
    f.close()
except PermissionError:
    print("    温馨提醒，请关闭表格文件。")
           
while(1):
    if(input(" "*45+"< welcome >")=='exit'):
        break

    

