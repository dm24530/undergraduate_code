from pyecharts.charts import Pie
from pyecharts.charts import Boxplot
import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType
city_name = ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
v = []
attrs = []
for i in range(4):
    filename = '..//csv//' + city_name[i] + '_AQI' + '_2018.csv'
    df = pd.read_csv(filename)

    Quality_grade_message = df.groupby(['Quality_grade'])
    Quality_grade_com = Quality_grade_message['Quality_grade'].agg(['count'])
    Quality_grade_com.reset_index(inplace=True)
    Quality_grade_com_list = Quality_grade_com.sort_values('count', ascending=False)

    Quality_grade_array = np.array(Quality_grade_com_list['Quality_grade'])
    attrs.append(Quality_grade_array)
    Quality_grade_count = np.array(Quality_grade_com_list['count'])
    v.append(Quality_grade_count)
months = ['{}'.format(str(i) + '月') for i in range(1, 13)]

pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add("北京", [list(z) for z in zip(attrs[0].tolist(), v[0].tolist())], radius=[60, 80], center=['20%', '30%'],
             label_opts=opts.LabelOpts(formatter="北京", position="center", font_size='25')
             )
        .add("上海", [list(z) for z in zip(attrs[1].tolist(), v[1].tolist())], radius=[60, 80], center=['55%', '30%'],
             label_opts=opts.LabelOpts(formatter="上海", position="center", font_size='25')
             )
        .add("广州", [list(z) for z in zip(attrs[2].tolist(), v[2].tolist())], radius=[60, 80], center=['20%', '70%'],
             label_opts=opts.LabelOpts(formatter="广州", position="center", font_size='25')
             )
        .add("深圳", [list(z) for z in zip(attrs[3].tolist(), v[3].tolist())], radius=[60, 80], center=['55%', '70%'],
             label_opts=opts.LabelOpts(formatter="深圳", position="center", font_size='25')
             )
        .set_global_opts(title_opts=opts.TitleOpts(title='2018年北上广深全年空气质量情况'),
                         legend_opts=opts.LegendOpts(type_="scroll", pos_top="20%", pos_left="80%", orient="vertical")
                         )
)
pie.render("..//HTML//8.4.5多个饼图3.html")