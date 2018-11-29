#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import sys
from scrapy.utils.project import get_project_settings
from scrapyuniversal.scrapyuniversal.spiders.universal import UniversalSpider
from scrapyuniversal.scrapyuniversal.utils import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    spider = custom_settings.get('spider','universal')
    project_setting = get_project_settings()
    settings = dict(project_setting.copy())

    #合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    #启动爬虫
    process.crawl(spider,**{'name':name})
    process.start()


if __name__ == '__main__':
    run()