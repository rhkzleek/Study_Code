# /usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

class DataOutput(object):
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
            self.create_table('MTime_db.MTime')
            print("******1*******")
            self.datas=[]

    def create_table(self,table_name):
        values = '''
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        MovidId INTEGER,
        MovieTitle VARCHAR(40) not NULL,
        RatingFinal REAL NOT NULL DEFAULT 0.0,
        ROtherFinal REAL NOT NULL DEFAULT 0.0,
        RPictureFinal REAL NOT NULL DEFAULT 0.0,
        RDirectorFinal REAL NOT NULL DEFAULT 0.0,
        RStoryFinal REAL NOT NULL DEFAULT 0.0,
        Usercount INTEGER NOT NULL DEFAULT 0,
        AttitudeCount INTEGER NOT NULL DEFAULT 0,
        TotalBoxOffice VARCHAR(20) NOT NULL,
        TodayBoxOffice VARCHAR(20) NOT NULL,
        Rank INTEGER NOT NULL DEFAULT 0,
        ShowDays INTEGER NOT NULL DEFAULT 0,
        isRelease INTEGER NOt NULL
        '''
        res = self.cx.execute('CREATE TABLE IF NOT EXISTs %s(%s)ENGINE=InnoDB DEFAULT CHARSET=utf8' %(table_name,values))
        print(res)


    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_db('MTime_db.MTime')

    def output_db(self,tables):
        '''
        数据存储到mysql
        :param data:
        :return:
        '''
        for data in self.datas:
            print("inser begin ",str(data) ,tables)

            self.cx.execute("INSERT INTO %s (MovidId,MovieTitle,"
                            "RatingFinal,ROtherFinal,RPictureFinal,"
                            "RDirectorFinal,RStoryFinal,Usercount,"
                            "AttitudeCount,TotalBoxOffice,TodayBoxOffice,"
                            "Rank,ShowDays,isRelease) VALUES %s;"
                            "" %(tables,str(data)))
            print("****",data,'*****')
            self.datas.remove(data)
        self.conn.commit()

    def output_end(self):
        '''
        关闭数据库
        :return:
        '''
        if len(self.datas) > 0:
            self.output_db('MTime_db.MTime')
        self.conn.close()

