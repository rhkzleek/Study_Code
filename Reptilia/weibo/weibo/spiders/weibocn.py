# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
import json
from weibo.items import UserItem,UserRelationItem,WeiboItem
import re,time


class WeibocnSpider(scrapy.Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&value={uid}&containerid=100505{uid}'
    follow_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&page={page}'
    fan_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&page={page}'
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}'
    start_users = ['3217179555', '1742566624', '2282991915', '1288739185', '3952070245', '5878659096']

    #start_urls = ['http://m.weibo.cn/']

    def parse(self, response):
        pass

    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid),callback=self.parse_user)

    def parse_user(self,response):
        self.logger.debug(response)
        result = json.loads(response.text)
        if result.get('data').get('userInfo'):
            user_info = result.get('data').get('userInfo')
            user_item = UserItem()
            field_map = {
                'id':'id',
                'name':'screen_name',
                'avatar':'profile_image_url',
                'cover':'cover_image_phone',
                'gender':'gender',
                'description':'description',
                'fans_count':'followers_count',
                'follows_count':'follow_count',
                'weibos_count':'statuses_count',
                'verified':'verified',
                'verified_reason':'verified_reason',
                'verified_type':'verified_type'
            }
            for field,attr in field_map.items():
                user_item[field] = user_info.get(attr)

            yield user_item

            #关注
            uid = user_info.get('id')
            yield Request(self.follow_url.format(uid=uid,page=1),callback=self.parse_follows,
                          meta={'page':1,'uid':uid})
            #yield Request(self.fan_url.format(uid=uid, page=1), callback=self.parse_fans,meta={'page': 1, 'uid': uid})
            yield Request(self.weibo_url.format(uid=uid, page=1), callback=self.parse_weibos,
                          meta={'page': 1, 'uid': uid})



    def parse_follows(self,response):
        '''
        解析用户关注
        :param self:
        :param response:
        :return:
        '''
        result = json.loads(response.text)
        if result.get('ok') and result.get('data'.get('cards') and len(result.get('data').get('cards'))) and result.get('data').get('cards')[-1].get('card_group'):
            #解析用户
            follows = result.get('data').get('cards')[-1].get('card_group')
            for follow in follows:
                if follow.get('user'):
                    uid = follow.get('user').get('id')
                    yield Request(self.user_url.format(uid=uid),callback=self.parse_user)
            #关注列表
            uid = response.meta.get('uid')
            user_relation_item = UserRelationItem()
            follows = [{
                'id': follow.get('user').get('id'),
                'name':follow.get('user').get('screen_name')
            } for follow in follows]
            user_relation_item['id'] = uid
            user_relation_item['follows'] = follows
            user_relation_item['fans']   = []
            yield user_relation_item

            #下一页关注
            page = response.meta.get('page') + 1
            yield Request(self.follow_url.format(uid=uid,page=page),
                          callback=self.parse_follows,meta={'page':page,'uid':uid})


    def parse_weibos(self,response):
        """
        解析微博列表
        :param response:Response对象
        :return:
        """
        result = json.loads(response.text)
        if result.get('ok') and result.get('data').get('cards'):
            weobos = result.get('data').get('cards')
            for weibo in weobos:
                mblog = weibo.get('mblog')
                if mblog:
                    weibo_item = WeiboItem()
                    field_map = {
                        'id':'id',
                        'attiture_count':'attiture_count',
                        'comments_count':'comments_count',
                        'created_at':'created_at',
                        'reposts_count':'reposts_count',
                        'picture':'original_pic',
                        'pictures':'pics',
                        'source':'source',
                        'text':'text',
                        'raw_text':'raw_text',
                        'thumbnail':'thumbnail_pic'
                    }
                    for field, attr in field_map.items():
                        weibo_item[field] = mblog.get(attr)
                        weibo_item['user'] = response.meta.get('uid')
                        yield weibo_item
                uid = response.meta.get('uid')
                page = response.meta.get('page') + 1
                yield Request(self.weibo_url.format(uid = uid,page = page),callback=self.parse_weibos,
                              meta={'uid':uid,'page':page})
