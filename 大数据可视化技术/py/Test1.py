from pyecharts.charts import Bar,Page
import pyecharts.options as opts
import csv
page = Page()

filename = "..\\csv\\hot-dog-contest-winners.csv"
datax = []
datay = []
def draw_postage_line():
    with open(filename) as f:
        reader = csv.reader(f)
        for datarow in reader:
            if reader.line_num != 1:
                datay.append(datarow[0])
                datax.append(datarow[2])
        bar = {
            Bar()
                .add_xaxis(datay)
                .add_yaxis('Dogs eaten',datax)
                .set_global_opts(title_opts=opts.TitleOpts(title="大胃王"),
                                 yaxis_opts=opts.AxisOpts(min_=0,max_=70,
                                 splitline_opts=opts.SplitLineOpts(is_show=True)))
                .render("..\\HTML\\Test1.html")
        }
if __name__ == "__main__":
	draw_postage_line()