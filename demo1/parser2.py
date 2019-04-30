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
        article_nums = len(articles)
        h = item.get("h", "")
        g = item.get("i10", "")
        try:
            Author.objects.create(
                name=name,
                domain = domain_text,
                citation_times=citation_times,
                article_numbers = article_nums,
                h_index = h,
                g_index = g,
            )
        except Author.DoesNotExist :
            continue


