import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
titanic = pd.read_csv('..//csv//birth-rate.csv')
titanic.dropna(subset=['2008'],inplace=True)
plt.style.use('ggplot')
# edgecolor() 边沿颜色
# bins直方图的个数
plt.hist(titanic['2008'],bins=10,color='steelblue',edgecolor='k',label='直方图')
# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off' , right='off')
plt.legend()
plt.show()