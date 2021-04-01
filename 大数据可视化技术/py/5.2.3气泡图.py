import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime = pd.read_csv('..//csv//crimeRatesByState2005.csv')
print(list(crime.murder))
crime2 = crime[crime.state != 'United States']
crime2 = crime[crime.state != 'District of Columbia']
s = list(crime2.population/10000)
# print(list(crime2.murder))
# print(s[0])
# print(len(list(crime2.murder)))
colors = np.random.rand(len(list(crime2.murder)))
cm = plt.cm.get_cmap('RdYlBu')
# s = s 设置散点图面积大小
# c = color为散点图颜色
# alpha=0.5 设置透明度为0.5
# linewidth=0.5 设置边缘线宽为0.5
plt.scatter(list(crime2.murder),list(crime2.burglary),s=s,c=colors ,
                     cmap=cm,linewidth=0.5,alpha=0.5)
plt.xlabel("murder")
plt.ylabel("burglary")
plt.show()