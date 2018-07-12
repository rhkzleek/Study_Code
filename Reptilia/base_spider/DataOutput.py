#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
数据存储器(DataOutput.py) 用于将HTML解析器解析出来的数据通过文件或者数据库的形式存储起来
'''

import codecs

class DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('baike.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.write('</html>')
        fout.write('</body>')
        fout.write('</table>')
        fout.close()