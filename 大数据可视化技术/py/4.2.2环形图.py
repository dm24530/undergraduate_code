from pyecharts import options as opts
from pyecharts.charts import Pie
import csv

filename = '..\\csv\\result.csv'
dataA = []
dataB = []
with open(filename) as f:
    reader = csv.reader((f))
    for datarow in reader:
        if reader.line_num != 1:
            dataA.append(datarow[0])
            dataB.append(datarow[1])
c = (
    Pie()
    .add("",[list(z) for z in zip(dataA, dataB)],radius=["40%", "75%"])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="数据可视化-用户感兴趣领域"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_right="2%"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .render("..\\HTML\\pie_huan.html")
)
