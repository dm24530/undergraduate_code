import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line

df = pd.read_csv('..//csv//beijing_AQI_2018.csv')
dom = df[['Date', 'AQI']]
# print(dom)
list1 = []
for j in dom['Date']:
    time = j.split('/')[1]
    # print(time)
    list1.append(time)
    # print(dom)
    # print(list1)
df['month'] = list1
# print(df['month'])
month_message = df.groupby(['month'])
# for i in month_message:
    # print(i)
month_com = month_message['AQI'].agg(['mean'])
print(month_com)
#设置了序号
month_com.reset_index(inplace=True)
# print(month_com)
month_com_last = month_com.sort_index()
# print(month_com_last)
attr = ['{}'.format(str(i) + '月') for i in range(1, 13)]
v1 = np.array(month_com_last['mean'])
v1 = [int(i) for i in v1]

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(attr)
    .add_yaxis("AQI月均值", v1,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max'),
                                                      opts.MarkPointItem(type_='min')])
               )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京月均AQI走势图'))
)
# line.render("..//HTML//8.4.1走势图3.html")