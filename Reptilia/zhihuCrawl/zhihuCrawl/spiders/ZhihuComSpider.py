# /usr/bin/env python3
# -*- coding:utf-8 -*-
import scrapy
from scrapy import Request,Selector,FormRequest,Spider
import json
import os

class ZhihuSpider(Spider):
    name = 'zhihuSpider'
    def start_request(self):
        #首先进入登录界面
        return [Request('https://www.zhihu.com/# signin',
                        callback=self.start_login,
                        meta={'cookiejar':1})]

    def start_login(self, response):
        #开始登录
        self.xsrf = Selector(response).xpath(
            '// input[@name="_xsrf"]/@value'
        ).extract_first()

        return [FormRequest(
            'https://www.zhihu.com/login/phone_num',
            method='POST',
            meta={'cookiejar':response.meta['cookiejar']},
            formdata={
                '_xsrf':self.xsrf,
                'phone_num':'xxxxxx',
                'password':'xxxxxx',
                'captcha_type':'cn'},
            callback=self.after_login
        )]

    def after_login(self,response):
        if json.loads(response.body)['msg'].encode('utf8') == "登录成功":
            self.logger.info(str(response.meta['cookiejar']))
            return [Request(
                self.start_urls[0],
                meta={'cookiejar':response.meta['cookiejar']},
                callback=self.parse_user_info,
                errback=self.parse_err,
            )]
        else:
            self.logger.error('登录失败')
            return

    def parse_user_info(self,response):
        '''
        解析用户信息
        :param response:
        :return:
        '''

        user_id = os.path.split(response.url)[-1]

