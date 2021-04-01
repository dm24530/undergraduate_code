import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line

df = pd.read_csv('..//csv//beijing_AQI_2018.csv')

dom = df[['Date', 'PM']]
list1 = []
for j in dom['Date']:
    time = j.split('/')[1]
    list1.append(time)
df['month'] = list1

month_message = df.groupby(['month'])
month_com = month_message['PM'].agg(['mean'])
month_com.reset_index(inplace=True)
month_com_last = month_com.sort_index()

attr = ['{}'.format(str(i) + '月') for i in range(1, 13)]
v1 = np.array(month_com_last['mean'])
v1 = [int(i) for i in v1]

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(attr)
    .add_yaxis("PM2.5月均值", v1,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max'),
                                                      opts.MarkPointItem(type_='min')])
               )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京月均PM2.5走势图'))
)
line.render("..//HTML//8.4.1走势图4.html")