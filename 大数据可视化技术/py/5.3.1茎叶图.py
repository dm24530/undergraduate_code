import numpy as np
import math
from itertools import groupby
import pandas as pd

birth = pd.read_csv('..//csv//birth-rate.csv')
# print(birth['2008'])
# #Dropna()丢弃缺失数据
birth.dropna(subset=['2008'] , inplace=True)
# print(birth['2008'])
dirt={}
# round(,1) 四舍五入保留一位小数
data = list(round(birth['2008'],1))
# print(round(birth['2008'],1))
# print(data)
rangenum = []
for k,g in groupby(sorted(data),key=lambda x:int(x)):
    lst = map(str,list(map(lambda y:divmod(int(y*10),10)[1],list(g))))
    dirt[k] = ' '.join(lst)
    rangenum.append(k)
    # print(k)
    # print(rangenum)
    # print(dirt[k])
num = list(range(rangenum[0],rangenum[-1],2))
# print(num)
for i in num:
    a = ''
    for k in sorted(dirt.keys()):
        if 0<=k-i<=1:
            a = a + ' ' + dirt[k]
            # print(dirt[k])
        elif k-i > 1:
            break
    print(str(i).rjust(5),'|',a)
