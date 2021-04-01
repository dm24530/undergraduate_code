from pyecharts.charts import Line
from pyecharts.charts import Boxplot
import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType

city_name = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
cityes_PM = []
for i in range(4):
    filename = '..//csv//' + city_name[i] + '_AQI' + '_2018.csv'
    pm_data = pd.read_csv(filename)

    get_data = pm_data[['Date', 'PM']]
    month_for_data = []
    for j in get_data['Date']:
        time = j.split('/')[1]
        month_for_data.append(time)
    #   获取每行数据的月份
    pm_data['Month'] = month_for_data
    #   求每个月PM平均值
    month_data = pm_data.groupby(['Month'])
    month_PM = month_data['PM'].agg(['mean'])
    month_PM.reset_index(inplace=True)
    month_PM_average = month_PM.sort_index()
    #   获取每个城市月均PM的数据，转化为int数据类型
    month_PM_data = np.array(month_PM_average['mean'])
    month_PM_data_int = [int(i) for i in month_PM_data]
    cityes_PM.append(month_PM_data_int)
months = ['{}'.format(str(i) + '月') for i in range(1, 13)]

line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(months)
        .add_yaxis("北京", cityes_PM[0])
        .add_yaxis("上海", cityes_PM[1])
        .add_yaxis("广州", cityes_PM[2])
        .add_yaxis("深圳", cityes_PM[3])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title='2018年北上广深PM2.5全年走势图'),
                         legend_opts=opts.LegendOpts(pos_top='8%')
                         )
)
line.render("..//HTML//8.4.5多个数据源2.html")