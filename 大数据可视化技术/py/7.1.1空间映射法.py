import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType

import matplotlib.pyplot as plt
import seaborn as sns
# 数据准备
iris = pd.read_csv('..//csv//iris.csv')
# 用Seabron画成对关系
sns.pairplot(iris, hue='species')
plt.show()