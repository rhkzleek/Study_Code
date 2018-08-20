# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import re

class YunqicrawlPipeline(object):

    def __init__(self):
        try:
            self.conn = pymysql.connect(host='47.105.43.9',
                                      port=3306,
                                      user='root',
                                      passwd='Cgh@1993',
                                      db='MTime_db',
                                      charset='utf8')
        except Exception as e:
            print(e)
        else:
            print('连接成功')
            self.cx = self.conn.cursor()

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(Item,YunqiBookList):
            self._process_booklist_item(item)
        else:
            self._process_bookDetail_item(item)
        return item

    def _process_booklist_item(self,item):
        '''
        处理小说信息
        :param item:
        :return:
        '''
        valDict = dict(item)
        sql = ''
        if(valDict['novelId'] != None):
            sql += "novelId = '"+ valDict['novelId'] + "',"
        if (valDict['novelName'] != None):
            sql += "novelName = '" + valDict['novelName'] + "',"
        if (valDict['novelAuthor'] != None):
            sql += "novelAuthor = '" + valDict['novelAuthor'] + "',"
        if (valDict['novelType'] != None):
            sql += "novelType = '" + valDict['novelType'] + "',"
        if (valDict['novelStatus'] != None):
            sql += "novelStatus = '" + valDict['novelStatus'] + "',"
        if (valDict['novelUpdateTime'] != None):
            sql += "novelUpdateTime = '" + valDict['novelUpdateTime'] + "',"
        if (valDict['novelImageUrl'] != None):
            sql += "novelImageUrl = '" + valDict['novelImageUrl'] + "',"
        if (valDict['novelWords'] != None):
            sql += "novelWords = '" + valDict['novelWords'] + "'"
        else:
            sql += "novelWords = ''"

        print("commit sql:[%s]" % sql)

        self.cx.execute("INSERT INTO MTime_db.BookList SET %s;" % (sql))

    def _deal_item(self,item):
        pattern = re.compile('\d+')
        item['novelLabel'] = item['novelLabel'].strip().replace('\n','')

        match = pattern.search(item['novelAllClick'])
        item['novelAllClick'] = match.group() if match else item['novelAllClick']

        match = pattern.search(item['novelMonethClick'])
        item['novelMonethClick'] = match.group() if match else item['novelMonethClick']

        match = pattern.search(item['novelWeekClick'])
        item['novelWeekClick'] = match.group() if match else item['novelWeekClick']

        match = pattern.search(item['novelAllPopular'])
        item['novelAllPopular'] = match.group() if match else item['novelAllPopular']

        match = pattern.search(item['novelMonthPopular'])
        item['novelMonthPopular'] = match.group() if match else item['novelMonthPopular']

        match = pattern.search(item['novelWeekPopular'])
        item['novelWeekPopular'] = match.group() if match else item['novelWeekPopular']

        match = pattern.search(item['novelAllComm'])
        item['novelAllComm'] = match.group() if match else item['novelAllComm']

        match = pattern.search(item['novelMonethComm'])
        item['novelMonethComm'] = match.group() if match else item['novelMonethComm']

        match = pattern.search(item['novelWeekComm'])
        item['novelWeekComm'] = match.group() if match else item['novelWeekComm']

        return item

    def _process_bookDetail_item(self,item):
        '''
        处理小说热度
        :param item:
        :return:
        '''

        valDict = dict(self._deal_item(item))
        sql = ''
        if(valDict['novelId'] != None):
            sql += "novelId = '"+ valDict['novelId'] + "',"
        if (valDict['novelLabel'] != None):
            sql += "novelLabel = '" + valDict['novelLabel'] + "',"
        if (valDict['novelAllclick'] != None):
            sql += "novelAllclick = '" + valDict['novelAllclick'] + "',"
        if (valDict['novelMonethClick'] != None):
            sql += "novelMonethClick = '" + valDict['novelMonethClick'] + "',"
        if (valDict['novelWeekClick'] != None):
            sql += "novelWeekClick = '" + valDict['novelWeekClick'] + "',"
        if (valDict['novelAllPopular'] != None):
            sql += "novelAllPopular = '" + valDict['novelAllPopular'] + "',"
        if (valDict['novelMonthPopular'] != None):
            sql += "novelMonthPopular = '" + valDict['novelMonthPopular'] + "',"
        if (valDict['novelWeekPopular'] != None):
            sql += "novelWeekPopular = '" + valDict['novelWeekPopular'] + "',"
        if (valDict['novelCommentNum'] != None):
            sql += "novelCommentNum = '" + valDict['novelCommentNum'] + "',"
        if (valDict['novelAllComm'] != None):
            sql += "novelAllComm = '" + valDict['novelAllComm'] + "',"
        if (valDict['novelMonethComm'] != None):
            sql += "novelMonethComm = '" + valDict['novelMonethComm'] + "',"
        if (valDict['novelWeekComm'] != None):
            sql += "novelWeekComm = '" + valDict['novelWeekComm'] + "'"
        else:
            sql += "novelWeekComm = ''"
        print("commit sql:[%s]" % sql)

        self.cx.execute("INSERT INTO MTime_db.BookList SET %s;" % (sql))
