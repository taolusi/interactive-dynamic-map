# coding=utf-8


from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


cities_coor = [("纽约", -77.0, 38.5), ("北京", 116.3, 39.5),
               ("伦敦", 0, 52.0), ("香港", 114.2, 22.3),
               ("巴西利亚", -47.5, -15.4), ("堪培拉", 149.0, -35.1)]
cities_value = [(x[0], int(x[2])) for x in cities_coor]
cities_arrow = []
for city in cities_coor:
    if city[0] != "香港":
        cities_arrow.append((city[0], "香港"))

geo = Geo()

geo.add_schema(maptype="world")

for city in cities_coor:
    geo.add_coordinate(city[0], city[1], city[2])

geo.add(
    "city",
    cities_value,
    type_=ChartType.EFFECT_SCATTER,
    color="green",
    label_opts=opts.LabelOpts(
        is_show=True,
        font_family="Microsoft YaHei",
        position="left",
        formatter="{b}"))
geo.add(
    "impact",
    cities_arrow,
    type_=ChartType.LINES,
    effect_opts=opts.EffectOpts(
        symbol=SymbolType.ARROW,
        symbol_size=6,
        color="blue"),
    linestyle_opts=opts.LineStyleOpts(
        curve=0.2),
    label_opts=opts.LabelOpts(
        is_show=True,
        position="left",
        formatter="{c}")
)

#geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False, position="insideTop", formatter="{b}"))
geo.set_global_opts(title_opts=opts.TitleOpts(title="全球局势影响"))

geo.render("global_situation_impact.html")  # 输出html格式
