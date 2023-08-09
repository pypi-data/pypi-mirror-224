from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

# 导入输出图片工具
from pyecharts.render import make_snapshot

# 使用snapshot-selenium 渲染图片
from snapshot_phantomjs import snapshot

table = Table()

headers = ["City name", "Area", "Population", "Annual Rainfall"]
rows = [
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Adelaide", 1295, 1158259, 600.5],
    ["Darwin", 112, 120900, 1714.7],
    ["Hobart", 1357, 205556, 619.5],
    ["Sydney", 2058, 4336374, 1214.8],
    ["Melbourne", 1566, 3806092, 646.9],
    ["Perth", 5386, 1554769, 869.4],
]
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="Table-基本示例", subtitle="我是副标题支持换行哦")
)
table.render("table_base.html")

make_snapshot(snapshot, table.render(), "Options配置项_自定义样式_保存图片.png")
