import pandas as pd
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

import pyecharts.options as opts
from pyecharts.globals import ThemeType

from pyecharts.charts import Parallel
# 导入数据
df_final = pd.read_csv('..//csv//beijing_AQI_2018.csv')
df_final = df_final[['AQI', 'AQI_rank', 'PM', 'Quality_grade']].values.tolist()

parallel = (
    Parallel(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_schema(
        [
            opts.ParallelAxisOpts(dim=0, name="AQI"),
            opts.ParallelAxisOpts(dim=1, name="AQI_rank"),
            opts.ParallelAxisOpts(dim=2, name="PM"),
            opts.ParallelAxisOpts(
                dim=3,
                name="Quality_grade",
                type_="category",
                data=["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"],
            ),
        ]
    )
    .add("parallel", df_final[:50])
    .set_global_opts(title_opts=opts.TitleOpts(title="北京空气质量平行折线图"))
)
# 在第一次渲染的时候调用 load_javascript() 会预先加载基本 JavaScript 文件到 Notebook 中
# load_javascript() 和 render_notebook() 方法需要在不同的 cell 中调用，这是 Notebook 的内联机制，
# 其实本质上 pyecharts 返回了带有 _html_, _javascript_ 对象的 class。notebook 会自动去调用这些方法。
parallel.render("..//HTML//8.4.html")