import json
import jsonlines
data_path = "C:\\酋长的工作区\\2019系统分析与设计\\爬虫\\article.json"

fields = []
with open(data_path, encoding="utf-8") as f:
    for item in jsonlines.Reader(f):
        print(type(item))