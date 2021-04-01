from pyecharts.charts import Pie
from pyecharts.charts import Boxplot
import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType

df = pd.read_csv('..//csv//beijing_AQI_2018.csv')
# 将数据按照Quality_grade分组
rank_message = df.groupby(['Quality_grade'])
# for i in rank_message:
#     print(i)
#  对Quality_grade这一列进行聚合操作，将数据相同的列放在一起，统计他们的数量
rank_com = rank_message['Quality_grade'].agg(['count'])
# print(rank_com)
# inplace = True：不创建新的对象，直接对原始对象进行修改；
rank_com.reset_index(inplace=True)
# print(rank_com)
#将数据按照count列按照从大到小的顺序进行排序
rank_com_last = rank_com.sort_values('count', ascending=False)
# print(rank_com_last)

# 将数据Quality_grade和count两列分成attr和v1两组数据
attr = rank_com_last['Quality_grade']
v1 = rank_com_last['count']

# 绘制饼图
pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add("空气质量", [list(z) for z in zip(attr, v1)], radius=[130, 180],
         tooltip_opts=opts.TooltipOpts(textstyle_opts=opts.TextStyleOpts(align='center'),
                                       formatter='{a}'+'<br/>'+'{b}: {c} ({d}%)'))
    .set_global_opts(title_opts=opts.TitleOpts(title='2018年北京全年空气质量情况', pos_left='center'),
                     legend_opts=opts.LegendOpts(orient='vertical', pos_top='5%', pos_left='2%')
                    )
)
pie.render("..//HTML//8.4.3饼图.html")