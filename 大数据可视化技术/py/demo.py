from pyecharts.charts import Line,Bar
import pyecharts.options as opts
import csv

filename='..\\csv\\hot-dog-places.csv' #导入csv文件
datax=[]
datay=[]

with open (filename) as f:
    reader=csv.reader(f)
    for datarow in reader:
        datax.append(datarow)

x=datax[0]
y1=datax[1]
y2=datax[2]
y3=datax[3]
bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("A",y1,stack=x)
    .add_yaxis('B',y2,stack=x)
    .add_yaxis('C',y3,stack=x)
    # .reversal_axis()     #翻转 XY 轴    /这里没看懂
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
)
bar.render()