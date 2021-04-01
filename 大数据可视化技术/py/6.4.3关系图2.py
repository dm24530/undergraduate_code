from pyecharts.charts import Graph
import os
import json

with open(os.path.join("..//json","weibo.json"),"r",encoding="utf-8") as f:
    j = json.load(f)
    # print(j)
    nodes, links, categories, cont, mid, userl = j
    print(mid)
graph = Graph(title="微博转发关系图", width=1200, height=600)
print(graph)
graph.add(
    "",
    nodes,
    links,
    categories,
    label_pos="right",
    graph_repulsion = 50,
    is_legend_show = False,
    line_curve = 0.2,
    label_text_color=None,
)
graph.render()