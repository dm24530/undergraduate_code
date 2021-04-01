import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Line
df = pd.read_csv('..//csv//beijing_AQI_2018.csv')
v1 = df['PM'].values.tolist()
attr = df['Date'].values.tolist()

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(attr)
    .add_yaxis("PM2.5值", v1,
               markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_='average')]),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max'),
                                                      opts.MarkPointItem(type_='min')])
               )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京PM2.5全年走势图'))
)
line.render("..//HTML//8.4.1折线图2.html")