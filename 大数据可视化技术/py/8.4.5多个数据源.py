import datetime
import random
from pyecharts.charts import Calendar
from pyecharts.charts import Line
from pyecharts.charts import Boxplot
import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType
city_name = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
cityes_AQI = []
for i in range(4):
    filename = '..//csv//' + city_name[i] + '_AQI' + '_2018.csv'
    aqi_data = pd.read_csv(filename)

    get_data = aqi_data[['Date', 'AQI']]
    month_for_data = []
    for j in get_data['Date']:
        time = j.split('/')[1]
        month_for_data.append(time)
    #   获取每行数据的月份
    aqi_data['Month'] = month_for_data
    #   求每个月AQI平均值
    month_data = aqi_data.groupby(['Month'])
    month_AQI = month_data['AQI'].agg(['mean'])
    month_AQI.reset_index(inplace=True)
    month_AQI_average = month_AQI.sort_index()
    #   获取每个城市月均AQI的数据，转化为int数据类型
    month_AQI_data = np.array(month_AQI_average['mean'])
    month_AQI_data_int = [int(i) for i in month_AQI_data]
    cityes_AQI.append(month_AQI_data_int)
months = ['{}'.format(str(i) + '月') for i in range(1, 13)]

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(months)
        .add_yaxis("北京", cityes_AQI[0])
        .add_yaxis("上海", cityes_AQI[1])
        .add_yaxis("广州", cityes_AQI[2])
        .add_yaxis("深圳", cityes_AQI[3])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='2018年北上广深AQI全年走势图'),
                         legend_opts=opts.LegendOpts(pos_top='8%')
                         )
)
line.render("..//HTML//8.4.5多个数据源.html")