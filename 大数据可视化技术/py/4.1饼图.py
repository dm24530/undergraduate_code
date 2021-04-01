from pyecharts import options as opts
from pyecharts.charts import Pie
import csv

filename = "..\\csv\\result.csv"
data1 = []
data2 = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            data1.append(datarow[0])
            data2.append(datarow[1])
c = (
    Pie()
    .add("", [list(z) for z in zip(data1, data2)])
    .set_global_opts(title_opts=opts.TitleOpts(title="饼图示例"))
    # b数据名  c数据  d百分比
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .render("..\\HTML\\result.html")
)