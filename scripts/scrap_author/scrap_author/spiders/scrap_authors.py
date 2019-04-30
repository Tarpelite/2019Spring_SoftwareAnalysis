import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re


class author(scrapy.Item):
    name=scrapy.Field()
    articles=scrapy.Field()
    citations=scrapy.Field()
    coworkers=scrapy.Field()
    specialties=scrapy.Field()
    h=scrapy.Field()
    i10=scrapy.Field()
    image_urls=scrapy.Field()
    images=scrapy.Field()

class article(scrapy.Item):
    data=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()

Maxpage=2
Number=100

urls=[]
for i in range(Maxpage):
    urls.append('https://c.glgoo.top/scholar?start=0&q=machine+learning&hl=zh-CN&as_sdt=0,5')

count=0

class AuthorSpider(CrawlSpider):
    name='glgoo'
    start_urls=urls
    allowed_domains=['c.glgoo.top']
    rules=(Rule(LinkExtractor(restrict_css=('div.gs_a')),callback='parse_author',follow=True),)

    def parse_author(self, response):
        au=author()
        au['name']=response.css('#gsc_prf_in::text').extract()
        au['citations']=response.css('.gsc_rsb_std::text').get()
        au['image_urls']=[response.urljoin(response.css('#gsc_prf_pua img::attr(src)').get())]
        if response.css('.gsc_rsb_aa').get() is not None:
            au['coworkers']=[]
            for co in response.css('.gsc_rsb_a_desc'):
                au['coworkers'].append(co.css('a::text').extract())            
            for next_author in co.css('::attr(href)').extract():
                next_author=response.urljoin(next_author)
                yield scrapy.Request(next_author,callback=self.parse_author)
        au['articles']=[]
        for a in response.css('.gsc_a_at'):
            au['articles'].append(a.css('::text').extract())
        au['specialties']=[]
        for s in response.css('.gsc_prf_inta'):
            au['specialties'].append(s.css('::text').extract())
        au['h']=response.css('.gsc_rsb_std::text')[2].extract()
        au['i10']=response.css('.gsc_rsb_std::text')[4].extract()
        for art in response.css('.gsc_a_t'):
            next_art=art.css('::attr(data-href)').get()
            yield scrapy.Request(response.urljoin(next_art),callback=self.parse_article,meta={'dont_redirect':True})
        yield au
    def parse_article(self,response):
        art=article()
        dic={}    
        for a in response.css('.gs_scl'):
            key=a.css('div::text').extract()[0]
            if len(a.css('div::text').extract())>1:                
                value=a.css('div::text').extract()[1]
                dic[key]=value
            else:
                value=response.css('div[style*="margin-bottom:1em"] a::text').get()
                dic[key]=value
                break
        art['data']=dic
        art['url']=response.css('.gsc_vcd_title_link::attr(href)').get()
        art['title']=response.css('.gsc_vcd_title_link::text').get()
        yield art
        