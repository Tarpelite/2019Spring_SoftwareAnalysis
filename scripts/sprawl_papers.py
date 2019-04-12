# -*- coding: utf-8 -*-
"""
Created on 12 April, 2019

@author: Tarpelite
"""
import requests,re,collections
from bs4 import BeautifulSoup

import json


# choose your demand
Max_page = 2
key = 'sparse+autoencoder'
start = '2000'
final = '2018'
text_title = 'GStitle.txt'
text_keyword = 'GSkw.txt'

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
keywords = ["machine learning", "deep learning"]
# clear existing file
with open(text_title, 'wt', encoding='utf-8') as f:
    f.truncate()

# grab titles
records=[]
cnt = 0
for key in keywords:
    for i in range(Max_page):
        url = 'https://c.beijingbang.top/scholar?start='+str(i*10)+'&q='+key+'&as_ylo='+start+'&as_yhi='+final
        start_html = requests.get(url,  headers=headers)
        Soup = BeautifulSoup(start_html.text, 'lxml')
        papers = Soup.find_all('div', class_='gs_ri')
        for paper in papers:
            record = {}
            title = paper.find_all('h3', class_='gs_rt')
            author = paper.find_all('div', class_='gs_a')
            abstract = paper.find_all('div', class_='gs_rs')
            refs = paper.find_all('div', class_='gs_fl')
            
        
            if paper.previous_sibling:
                urls_soup = BeautifulSoup(str(paper.previous_sibling), 'lxml')
                urls = urls_soup.find_all('a')
                if len(urls) > 0:
                    record['urls'] = urls[0].attrs['href']
                else:
                    record['urls'] = ""

            if len(title) > 0:
                record['title'] = title[0].get_text()
            else:
                record['title'] = ""
            if len(author) > 0:
                record['authors'] = author[0].get_text()
            else:
                record["authors"] = ""
            if len(abstract) > 0:
                record['abstract'] = abstract[0].get_text()
            else:
                record['abstract'] = ""
            if len(refs)> 0:
                record['refs'] = refs[0].get_text()
            else:
                record['refs'] = ""
            records.append(record)
            
            with open("data/"+key+str(cnt)+".json", "w+", encoding='utf-8') as f:
                json.dump(record, f)
                cnt += 1
            
print(records)

