#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
HTML 下载器(HtmlDownloader.py)用于从URL管理器中获取未爬取的URL链接并下载HTML网页
'''

import requests
class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        headers = {'User-Agent':user_agent}
        r = requests.get(url=url, headers= headers)
        if r.status_code == 200:
            r.encoding='utf-8'
            return r.text
        return None