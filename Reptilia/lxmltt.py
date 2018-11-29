#!/usr/bin/env python 
# -*- coding:utf-8 -*-




from lxml import etree

html = etree.parse('http://top.baidu.com/?fr=mhd_card',parser=etree.HTMLParser())
results = html.xpath('//.')
print(results)
print('*******************')
results = html.xpath('//@class')
print(results)
print('*******************')
results = html.xpath('//div[@id="flip-list"]/div/div/div/child::*/@href')
print(results,len(results))
print('*******************')
results = html.xpath('//div[@id="flip-list"]/div/div/div/child::*/attribute::*')
print(results,len(results))
print('*******************')
results = html.xpath('//div[@id="flip-list"]/div/div/div/child::*/ancestor::*')
print(results,len(results))
print('*******************')
results = html.xpath('count(//div[@id="flip-list"]/div/div/div/child::*/ancestor::*)')
print(results)
print('*******************')
