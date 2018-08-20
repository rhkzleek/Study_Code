# coding: utf-8
"""
-------------------------------------------------
   File Name：    MysqlClient.py
   Description :  封装mysql操作
   Author :       caogh
   date：          2018/8/16
-------------------------------------------------
   Change Activity:
                   2018/8/16:
                   2018/8/16:完成对mysql的支持
-------------------------------------------------
"""
__author__ = 'caogh'

import pymysql


username = 'root'
password = 'Cgh@1993'

class MysqlClient(object):
    def __init__(self, name, host, port):
        self.name = name
        self.client = pymysql.connect(host=host,user=username,passwd=password,database=name,port=port,charset='utf8')
        self.cursor = self.client.cursor() #创建一个游标对象

    def changeTable(self, name):
        self.name = name

    def get(self, proxy):
        sql = 'SELECT * FROM %s WHERE proxy = %s;' % (self.name,proxy)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row = re
        data = self.db[self.name].find_one({'proxy': proxy})
        return data['num'] if data != None else None

    def put(self, proxy, num=1):
        if self.db[self.name].find_one({'proxy': proxy}):
            return None
        else:
            self.db[self.name].insert({'proxy': proxy, 'num': num})

    def pop(self):
        data = list(self.db[self.name].aggregate([{'$sample': {'size': 1}}]))
        if data:
            data = data[0]
            value = data['proxy']
            self.delete(value)
            return {'proxy': value, 'value': data['num']}
        return None

    def delete(self, value):
        self.db[self.name].remove({'proxy': value})

    def getAll(self):
        return {p['proxy']: p['num'] for p in self.db[self.name].find()}

    def clean(self):
        self.client.drop_database('proxy')

    def delete_all(self):
        self.db[self.name].remove()

    def update(self, key, value):
        self.db[self.name].update({'proxy': key}, {'$inc': {'num': value}})

    def exists(self, key):
        return True if self.db[self.name].find_one({'proxy': key}) != None else False

    def getNumber(self):
        return self.db[self.name].count()


if __name__ == "__main__":
    db = MongodbClient('first', 'localhost', 27017)
    # db.put('127.0.0.1:1')
    # db2 = MongodbClient('second', 'localhost', 27017)
    # db2.put('127.0.0.1:2')
    print(db.pop())
