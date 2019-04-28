import json
import jsonlines
data_path = "C:\\酋长的工作区\\2019系统分析与设计\\爬虫\\article.jl"

fields = []
with open(data_path, encoding="utf-8") as f:
    for item in jsonlines.Reader(f):
        url = item.get('url')
        for k in item['data'].keys():
            if k not in fields:
                fields.append(k)
print(fields)