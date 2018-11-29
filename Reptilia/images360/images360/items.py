# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ImageItem(scrapy.Item):
    collection = table = 'image'
    #图片id
    id  = scrapy.Field()
    #链接
    url = scrapy.Field()
    #标题
    title = scrapy.Field()
    #缩小图
    thumb = scrapy.Field()