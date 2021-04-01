from pyecharts import options as opts
from pyecharts.charts import Bar
import csv

filename = '..//csv//rate.csv'
data1 = []
data2 = []
data3 = []
data4 = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        if reader.line_num != 1:
            data1.append(datarow[0])
            data2.append(datarow[1])
            data3.append(datarow[2])
            data4.append(datarow[3])
c = {
    Bar()
    .add_xaxis(data1)
    .add_yaxis('支持',data2,stack='stack1')
    .add_yaxis('反对',data3,stack='stack1')
    .add_yaxis('不发表意见',data4,stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="比例堆叠图"),
                     legend_opts=opts.LegendOpts(is_show=True))
    .render('..//HTML//4.2.3.html')
}