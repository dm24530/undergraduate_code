from pyecharts.charts import Bar
import pyecharts.options as opts
import csv

filename = "..\\csv\\hot-dog-places.csv"
data = []
with open(filename) as f:
    reader = csv.reader(f)
    for datarow in reader:
        data.append(datarow)
datax = data[0]
datay_A = data[1]
datay_B = data[2]
datay_C = data[3]
def draw_postage_line():
    bar = {
        Bar()
        .add_xaxis(datax)
        .add_yaxis("第一名",datay_A,stack=datax)
        .add_yaxis("第二名",datay_B,stack=datax)
        .add_yaxis("第三名",datay_C,stack=datax)
        .set_global_opts(title_opts=opts.TitleOpts(title="柱形图数据堆叠示例"),
                         yaxis_opts=opts.AxisOpts(min_=0,max_=210,
                         splitline_opts=opts.SplitLineOpts(is_show=True)))
        .render('..\\HTML\\Test2.html')
    }
if __name__ == "__main__":
	draw_postage_line()