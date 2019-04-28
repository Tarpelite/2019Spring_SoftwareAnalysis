import json

data_path = "C:\\酋长的工作区\\2019系统分析与设计\\爬虫\\author.json"

with open(data_path, encoding="utf-8") as f:
    data = json.load(f)
    print(len(data))