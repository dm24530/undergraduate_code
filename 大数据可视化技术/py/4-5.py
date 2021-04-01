from pyecharts import options as opts
from pyecharts.charts import Pie
import csv

filename = "..\\csv\\result.csv"
datax = []
datay = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            datay.append(datarow[0])
            datax.append(datarow[1])
c = (
    Pie()
    .add("", [list(z) for z in zip(datay, datax)])
    .set_global_opts(title_opts=opts.TitleOpts(title="饼图示例"),
                     legend_opts=opts.LegendOpts(is_show=False))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    .render("..\\HTML\\4-5.html")
)