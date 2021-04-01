import datetime
import random
from pyecharts.charts import Calendar
from pyecharts.charts import Pie
from pyecharts.charts import Boxplot
import numpy as np
import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType

df = pd.read_csv('../csv/beijing_AQI_2018.csv')
dom = df[['Date', 'PM']]
list1 = []
for i, j in zip(dom['Date'], dom['PM']):
    time_list = i.split('/')
    # print(j)
    time = datetime.date(int(time_list[0]), int(time_list[1]), int(time_list[2]))
    PM = int(j)
    # print(time)
    list1.append([str(time), int(PM)])

calendar=(
    Calendar(init_opts=opts.InitOpts(bg_color='white', height='300px'))
    .add("PM2.5", list1, calendar_opts=opts.CalendarOpts(range_="2018"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2018年北京PM2.5指数日历图"),
        visualmap_opts=opts.VisualMapOpts(
            max_=max(dom['PM']),
            min_=min(dom['PM']),
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        )
    )
)
# calendar.render("..//HTML//8.4.4日历热力图.html")