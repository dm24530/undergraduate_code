from pyecharts.charts import Boxplot
import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line

df = pd.read_csv('..//csv//beijing_AQI_2018.csv')
dom = df[['Date', 'AQI']]
data = [[], [], [], []]
dom1, dom2, dom3, dom4 = data
for i, j in zip(dom['Date'], dom['AQI']):
    time = i.split('/')[1]
    if time in ['1', '2', '3']:
        dom1.append(j)
    elif time in ['4', '5', '6']:
        dom2.append(j)
    elif time in ['7', '8', '9']:
        dom3.append(j)
    else:
        dom4.append(j)

boxplot = Boxplot(init_opts=opts.InitOpts(theme=ThemeType.DARK))
boxplot = (
    boxplot.add_xaxis(['第一季度', '第二季度', '第三季度', '第四季度'])
    .add_yaxis("", boxplot.prepare_data([dom1, dom2, dom3, dom4]))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京季度AQI箱型图'))
)
boxplot.render("..//HTML//8.4.2箱型图.html")