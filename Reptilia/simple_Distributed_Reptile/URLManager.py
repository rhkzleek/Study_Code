#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
URL管理器
'''

import pickle
import hashlib
class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')
        self.old_urls = self.load_progress('old_urls.txt')

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''
        获取一个未爬取的url
        :return:
        '''
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self,url):
        '''
        将新的url添加到未爬取的URL集合中
        :param url: 单个url
        :return:
        '''
        if url is None:
            return
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        将新的url添加到未爬取的URL集合中
        :param urls: url集合
        :return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        获取未爬取的URL集合的大小
        :return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已经爬取的url集合大小
        :return:
        '''
        return len(self.old_urls)

    def save_progress(self,path,data):
        '''
        保存进度
        :param path:文件路径
        :param data: 数据
        :return:
        '''
        with open(path,'wb') as f:
            pickle.dump(data,f)

    def load_progress(self,path):
        '''
        从本地文件加载进度
        :param path: 文件路径
        :return: 返回set集合
        '''
        print('[+] 从文件加载进度: %s' % path)
        try:
            with open(path,'rb') as f:
                tmp = pickle.load(f)
                return tmp
        except Exception as e:
            print('[!] 无进度文件,创建:%s' %path)
        return set()