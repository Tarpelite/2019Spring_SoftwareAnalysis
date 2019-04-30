import json
import jsonlines

data_path = "C:\\酋长的工作区\\2019Spring_SoftwareAnalysis\\scripts\\scrap_author\\author.jl"  
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo1.settings")

import django
django.setup()
from hostweb.models import *
fields = ['name', 'citations', 'articles', 'specialties', 'h', 'i10']

with open(data_path, encoding="utf-8") as f:
    for item in jsonlines.Reader(f):
        domain_list = item.get("specialties", " ")
        d_list = []
        for t in domain_list:
            if isinstance(t, list):
                for g in t:
                    d_list.append(g)
        domain_text = ",".join(d_list)
        name = item.get("name", "")[0]
        citation_times = item.get("citations", "")
        articles = item.get("articles", "")
        article_list = []
        for a in articles:
            if isinstance(a, list):
                for a_ in a:
                    try:
                        print(a_)
                        a1 = Resource.objects.get(title=a_)
                        au1 = Author.objects.get(name=name)
                    except Exception as e:
                        continue
                    A2R.objects.create(author_ID=au1, resource_ID=a1)
                    print(a1)

            