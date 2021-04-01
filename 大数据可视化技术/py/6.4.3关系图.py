from pyecharts.charts import Graph
import pyecharts.options as opts
from pyecharts.globals import ThemeType
# from pyecharts_snapshot.main import make_a_snapshot
import os
import json

with open(os.path.join("..//json//weibo.json"), "r", encoding="utf-8") as f:
    j = json.load(f)
    # print(j)
    nodes, links, categories, cont, mid, userl = j
    # print(mid)
graph = (
    Graph(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    .add("", nodes, links, categories, repulsion=50)
    .set_series_opts(label_opts=opts.LabelOpts(position='right'),
                     linestyle_opts=opts.LineStyleOpts(curve=0.2))
    .set_global_opts(title_opts=opts.TitleOpts(title='微博转发关系图',
                                               title_textstyle_opts=opts.TextStyleOpts(color='white')),
                     legend_opts=opts.LegendOpts(is_show=False))
)
graph.render('..//HTML//6.4.3关系图.html')
# make_a_snapshot('test.png')