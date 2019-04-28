# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from .spiders.scrap_authors import author,article
import json
"""
class ScrapAuthorPipeline(object):
    def process_item(self, item, spider):
        authorset=set()
        if not isinstance(item,author):
            return item
        else:        
            if item['name'] not in authorset:
                authorset.add(item['name'])            
                return item
            else:
                raise DropItem

class ScrapArticlePipeline(object):
    def process_item(self,item,spider):
        articleset=set()
        if not isinstance(item,article):
            return item
        else:
            if item['url'] not in articleset:
                articleset.add(item['url'])            
                return item
            else:
                raise DropItem
"""
class ArticleJsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('article.jl', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item,article):
            return item
        else:
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(line.encode('utf-8'))
            return item

class AuthorJsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('author.jl', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if not isinstance(item,author):
            return item
        else:
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file.write(line.encode('utf-8'))
            return item