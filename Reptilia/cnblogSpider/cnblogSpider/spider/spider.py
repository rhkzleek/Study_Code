# /usr/bin/env python3
#-*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule

class CnblogSpider(scrapy.Spider):
    name='CnblogsSpider' #爬虫的名称
    allowed_domains = ["cnblogs.com"] #可以的域名
    start_urls =  [
        "http://www.cnblogs.com/qiyeboy/default.html?page=1"
    ]

    def parse(self, response):
        #实现网页的解析
        pass


from scrapy import cmdline
cmdline.execute("scrapy crawl CnblogsSpider".split())