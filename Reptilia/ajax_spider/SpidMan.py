# /usr/bin/env python3
# -*- coding: utf-8 -*-
from ajax_spider.DataOutput import DataOutput
from ajax_spider.HtmlDownloader import HtmlDownloader
from ajax_spider.HtmlParser import HtmlParse
import time


class SpidMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser   = HtmlParse()
        self.output   = DataOutput()

    def crawl(self,root_url):
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(root_url,content)
        for url in urls:
            try:
                t = time.strftime("%Y%m%d%H%M%S3282",time.localtime())
                rank_url = 'http://service.library.mtime.com/Movie.api' \
                           '?Ajax_CallBack=tru' \
                           'e&Ajax_CallBackType=Mtime.Library.Services' \
                           '&Ajax_CallBackMethod=GetMovieOverviewRating' \
                           '&Ajax_CrossDomain=1' \
                           '&Ajax_RequestUrl=%s' \
                           '&t=%s' \
                           '&Ajax_CallBackArgument0=%s' % (url[0],t,url[1])

                rank_content = self.downloader.download(rank_url)
                #print('***222****',rank_content)
                data = self.parser.parser_json(rank_url,rank_content)
                print('**333****', data)
                self.output.store_data(data)
                print('**4444****')
            except Exception as e:
                print("Crawl failed")
        self.output.output_end()
        print('Crawl finish')

if __name__ == '__main__':
    spider = SpidMan()

    print()
    spider.crawl('http://theater.mtime.com/China_Beijing/')