#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
爬虫调度器(SpiderMan.py)主要负责统筹其他四个模块的协调工作
'''

from base_spider.DataOutput import DataOutput
from base_spider.HtmlDownloader import HtmlDownloader
from base_spider.HtmlParser import HtmlParse
from base_spider.URLManager import UrlManager

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParse()
        self.output = DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是否存在新的url,同时抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                #从URL管理器中获取新的url
                new_url = self.manager.get_new_url()

                print(new_url)
                #Html下载网页
                html = self.downloader.download(new_url)
                print(html)
                #Html解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print('new_urls:[%s] data:[%s]'% (new_urls, data))
                print('已经抓取了%s个链接' % self.manager.old_url_size())
            except Exception as e:
                print('crawl failed')
        self.output.output_html()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/网络爬虫")
    #spider_man.crawl("http://www.sina.com.cn/")