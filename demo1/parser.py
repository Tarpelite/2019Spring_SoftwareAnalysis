import json
import jsonlines
data_path = "C:\\酋长的工作区\\SA_Spider\\article.jl"
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo1.settings")

import django
django.setup()
from hostweb.models import *
fields = ['作者', '发表日期', '简介', '出版商', '引用总数', '发明者', '专利局', '专利申请号', '专利号']
with open(data_path, encoding="utf-8") as f:
    for item in jsonlines.Reader(f):
        
        url = item.get('url', "")
        title = item.get('title',  "UnKnown Title")
        if title == "" or title == None:
            continue
        else:
            print(title)
            data = item.get('data')
            publish_date = data.get('发表日期', "")
            authors = data.get('作者', "")
            intro = data.get('简介', "")
            publisher = data.get('出版商',"")
            citation_numbers = data.get("引用总数", "")
            num = citation_numbers.split(":")
            if len(num) > 1:
                citation_numbers = int(num[1])
            else:
                citation_numbers = 0
            agency = data.get("专利局", "")
            patent_number = data.get("专利号", "")
            patent_application_number = data.get("专利申请号", "")
            if patent_number != "":
                Type = "P2"
                authors = data.get("发明者")
            else:
                Type = "P1"
                authors = data.get("发明者")
            try:
                Resource.objects.create(url=url,
                                title=title,
                                publish_date=publish_date,
                                authors=authors,
                                intro=intro,
                                publisher=publisher,
                                citation_numbers=citation_numbers,
                                agency=agency,
                                patent_number=patent_number,
                                patent_applicant_number=patent_application_number,
                                Type=Type)
            except Exception as e:
                continue
        
