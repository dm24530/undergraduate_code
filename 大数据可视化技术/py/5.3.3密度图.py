import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#用来正常显示中文标签 字体微软雅黑
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
titanic = pd.read_csv('..//csv//birth-rate.csv')
titanic.dropna(subset=['2008'],inplace=True)
# 生成核密度曲线的数据
kde = mlab.GaussianKDE(titanic['2008'])
x2 = np.linspace(titanic['2008'].min(),titanic['2008'].max(),1000)
line2 = plt.plot(x2,kde(x2),'g-',linewidth=2)
plt.show()