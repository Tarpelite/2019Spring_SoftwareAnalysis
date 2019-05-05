import json
import jsonlines

data_path = "C:\\酋长的工作区\\SA_Spider\\author.jl"
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo1.settings")

import django
django.setup()
from hostweb.models import *
fields = ['name', 'citations', 'articles', 'specialties', 'h', 'i10']
'''
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
        coworkers = item.get("coworkers")

        
        if coworkers:
            for t in coworkers:
                name2 = t[0]
                try:
                    au1 = Author.objects.get(name = name)
                except:
                    au1 = Author.objects.create(name = name)
                try:
                    au2 = Author.objects.get(name = name2)
                except Author.DoesNotExist:
                    au2 = Author.objects.create(name = name2)

                try:
                    relationship = A2A.objects.get(author1=au1, author2=au2)
                except A2A.DoesNotExist:
                    A2A.objects.create(author1=au1, author2=au2)
        
        
        
        images = item.get("images", "")
        if len(images) > 0:
            path = images[0]['path'][5:]
            path = "author_avator/" + path
            try:
                au1 = Author.objects.get(name=name)
            except Author.DoesNotExist:
                continue
            au1.avator = path
        
            
         
        for a in articles:
            if isinstance(a, list):
                for a_ in a:
                    try:
                        print(a_)
                        a1 = Resource.objects.get(title=a_)
                        au1 = Author.objects.get(name=name)
                    except Exception as e:
                        continue
                    try:
                        A2R.objects.create(author_ID=au1, resource_ID=a1)
                        print(a1)
                    except Exception as e:
                        continue

'''    

with open(data_path, encoding="utf-8") as f:
    base_path = "C:\\酋长的工作区\\SA_Spider\\scrap_author\\Avatar\\full\\"
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
        if articles:
            for t in articles:
                article_list.append(t[0])
    
        h_index = item.get('h', "")
        g_index = item.get('i10', "")
        image = item.get('images')
        if image:
            path = image[0].get("path")
            path = path[5:]
        try:
            au = Author.objects.get(name = name)
        except Author.DoesNotExist:
            au = Author.objects.create(name = name)
        
        au.citation_times = citation_times
        au.domain = domain_text
        au.h_index = h_index
        au.g_index = g_index
        au.save()
        print(name) 
        for a in articles:
            if isinstance(a, list):
                for a_ in a:
                    try:
                        print(a_)
                        a1 = Resource.objects.get(title=a_)
                        au1 = Author.objects.get(name=name)
                    except Exception as e:
                        continue
                    try:
                        A2R.objects.create(author_ID=au1, resource_ID=a1)
                        print(a1)
                    except Exception as e:
                        continue 

        
