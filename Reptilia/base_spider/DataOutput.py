#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
数据存储器(DataOutput.py) 用于将HTML解析器解析出来的数据通过文件或者数据库的形式存储起来
'''

import codecs

class DataOutput(object):

    def __init__(self):
        self.data = []

    def store_data(self,data):
        if data is None:
            return
        self