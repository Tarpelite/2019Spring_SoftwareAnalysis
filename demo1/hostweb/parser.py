import json
import jsonlines
data_path = "C:\\酋长的工作区\\2019Spring_SoftwareAnalysis\\scripts\\scrap_author\\article.jl"

fields = ['作者', '发表日期', '简介', '出版商', '引用总数']
with open(data_path, encoding="utf-8") as f:
    for item in jsonlines.Reader(f):
        url = item.get('url')
        for k in item.keys():
            if k not in fields:
                print(k)
        for k in item['data'].keys():
            if k not in fields:
                fields.append(k)
print(fields)