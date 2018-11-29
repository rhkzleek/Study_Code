# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.scrapyuniversal.utils import get_config
from scrapyuniversal.scrapyuniversal.configs.rules import rules


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self):
        config = get_config()
        self.config = config
        self.rules = rules.get(config.get('rules'))
        self.start_urls = config.get('start_urls')
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider,self).__init__(*args,**kwargs)
    #allowed_domains = ['universal']
    #start_urls = ['http://universal/']


    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
