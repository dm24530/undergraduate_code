from pyecharts.charts import Line
from pyecharts import options as opts

def draw_stair_line():
    datax = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
             '2008',
             '2009']
    datay = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]
    c = (
        Line()
            .add_xaxis(datax)
            .add_yaxis("price", datay ,is_step=True)
            .set_global_opts(title_opts=opts.TitleOpts("美国邮费阶梯图"),
                            yaxis_opts=opts.AxisOpts(min_=0.3,max_=0.45,splitline_opts=opts.SplitAreaOpts(is_show=True)))
            .render('..//HTML//3.2.1阶梯图.html')
)
if __name__ == "__main__":
    draw_stair_line()