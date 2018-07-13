#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
数据存储器(DataOutput.py) 用于将HTML解析器解析出来的数据通过文件或者数据库的形式存储起来
'''

import codecs
import time

class DataOutput(object):

    def __init__(self):
        self.filepath = 'baike_%s.html' %(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_head(self,path):
        '''
        将HTML头写进去
        :return:
        '''
        fout = codecs.open(path,'a',encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_end(self, path):
        '''
        输出HTML结束
        :return:
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()



    def output_html(self):
        fout = codecs.open('baike.html','w',encoding='utf-8')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')
            self.datas.remove(data)
        fout.close()

