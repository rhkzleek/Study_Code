#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
HTML 解析器(HtmlParse.py)用于从HTML下载器中获取已经下载的HTML网页,并且从中解析出新的URL链接交给URL管理器,解析出有效数据交给数据存储器
'''

import  re
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import json

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

    def parser_url(self,page_url,response):
        pattern  = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls != None:
            #将urls去重
            return list(set(urls))
        else:
            return None


    #从动态加载的链接中提取所需的字段
    def parser_json(self,page_url,response):
        '''
        解析响应
        :param page_url:
        :param response:
        :return:
        '''
        #将 "=" 和";"之间的内容提取出来
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result != None:
            # json模块加载字符串
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print(e)
                return None

            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url,value)
                else:
                    return self._parser_no_release(page_url,value,isRelease=2)
            else:
                return self._parser_no_release(page_url,value)


    def _parser_release(self,page_url,value):
        '''
        解析已经上映的影片
        :param self:
        :param page_url:
        :param value:
        :return:
        '''

        try:
            #print('***7***',value)
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal= movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            TotalBoxOffice = boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice =boxOffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')

            ShowDays = boxOffice.get('ShowDays')

            try:
                Rank = boxOffice.get('Rank')
            except Exception as e:
                Rank = 0

            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal,RPictureFinal,RDirectorFinal,
                    RStoryFinal,Usercount,AttitudeCount,
                    TotalBoxOffice + TotalBoxOfficeUnit,
                    TodayBoxOffice + TodayBoxOfficeUnit,
                    Rank,ShowDays,isRelease)

        except Exception as e:
            #print('****5***')
            print(e,page_url,value)
            return None

    def _parser_no_release(self,page_url,value,isRelease = 0):
        '''
        解析未上映的电影信息
        :param page_url:
        :param value:
        :param isRelease:
        :return:
        '''
        try:
            #print('***8***', value)
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')


            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal= movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception as e:
                Rank = 0
            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal,RPictureFinal,RDirectorFinal,
                    RStoryFinal,Usercount,AttitudeCount,
                    u'无',
                    u'无',
                    Rank,0,isRelease)

        except Exception as e:
            #print('****6***')
            print(e,page_url,value)
            return None


