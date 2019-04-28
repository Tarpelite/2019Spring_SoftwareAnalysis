import json
import jsonlines
data_path = "C:\\酋长的工作区\\2019Spring_SoftwareAnalysis\\scripts\\scrap_author\\article.jl"

fields = ['作者', '发表日期', '简介', '出版商', '引用总数', '发明者', '专利局', '专利申请号', '专利号']
with open(data_path, encoding="utf-8") as f:
    for item in jsonlines.Reader(f):
        url = item.get('url', "")
        title = item.get('title',  "")
        data = item.get('data')
        publish_date = data.get('发表日期', "")
        authors = data.get('作者', "")
        intro = data.get('简介', "")
        publisher = data.get('出版商',"")
        citation_numbers = data.get("引用总数", "")
        agency = data.get("专利局", "")
        patent_number = data.get("专利号", "")
        patent_application_number = data.get("专利申请号", "")
        if patent_number != "":
            Type = "P2"
        else:
            Type = "P1"
