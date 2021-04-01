# _*_ coding:utf-8 _*_
from pyecharts.charts import Line
from pyecharts import options as opts

# https://zhuanlan.zhihu.com/p/111330795
def draw_postage_line():
	datax = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
	     '2009']
	datay = [0.32, 0.32, 0.32, 0.32, 0.33, 0.33, 0.34, 0.37, 0.37, 0.37, 0.37, 0.39, 0.41, 0.42, 0.44]
	c = (
		Line()
			.add_xaxis(datax)
			.add_yaxis("Price", datay,is_step="False")
			.set_global_opts(title_opts=opts.TitleOpts(title="美国邮费阶梯图"),
							 yaxis_opts=opts.AxisOpts(min_=0.3,max_=0.45,
							 splitline_opts=opts.SplitLineOpts(is_show=True),))
			.render("../HTML/dv_34_postage_line.html")
	)
if __name__ == "__main__":
	draw_postage_line()
