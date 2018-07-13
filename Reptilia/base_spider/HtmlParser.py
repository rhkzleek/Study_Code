#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
HTML 解析器(HtmlParse.py)用于从HTML下载器中获取已经下载的HTML网页,并且从中解析出新的URL链接交给URL管理器,解析出有效数据交给数据存储器
'''

import  re
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup

class HtmlParse(object):

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容,抽取url和数据
        :param page_url: 下载页面的url
        :param html_cont: 下载页面的网页内容
        :return: 返回url和数据
        '''

        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self.__get_new_urls(page_url,soup)
        new_data = self.__get_new_data(page_url,soup)

        return new_urls,new_data

    def __get_new_urls(self,page_url,soup):
        '''
        抽取url的集合
        :param page_url:下载页面的URL
        :param soup:soup
        :return:返回新的URL集合
        '''
        new_urls = set()
        #抽取符合要求的a标记
        links = soup.find_all('a',href = re.compile(r'/item/\W+'))
        for link in links:
            #提取href属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def __get_new_data(self,page_url,soup):
        '''
        抽取有效数据
        :param page_url:下载页面的URL
        :param soup: soup
        :return: 返回的数据
        '''

        data = {}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')

        data['title'] = title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        #获取tag中包含的所有文本内容,包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary'] = summary.get_text()

        return data