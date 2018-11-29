#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import time
import os
import logging
import pymysql
'''
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logname = __file__.split('.')[0] + '_' + time.strftime("%Y_%m_%d",time.localtime()) +'.txt'
handler = logging.FileHandler(logname,mode='w',encoding='UTF-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - [%(process)s] - [%(lineno)s] - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
'''
DB_HOST='192.168.0.114'
DB_PORT=3306
DB_USER='depuser'
DB_PWD='depuser'
DB_DB='order_db'
MYSQL='/usr/local/mysql/bin/mysql'

#用字典保存日志级别
format_dict = {
   1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}
# 开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger():
    def __init__(self, logname, loglevel, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname,mode='a',encoding='UTF-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        #ch = logging.StreamHandler()
        #ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(process)s] - [%(lineno)s] - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        #self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
logname = __file__.split('.')[0] + '_' + time.strftime("%Y_%m_%d",time.localtime()) +'.txt'
logger = Logger(logname,'1',__name__).getlog()

def isRunning(process_name):
    try:
        process = len(os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines())
        if process <= 1:
            logger.info("Check can be used")
            return True
        else:
            logger.info("Check can be used")
            return False
    except:
        logger.error("isRunning errer")
        return False


def run():
    flag = isRunning(__file__)
    if(flag):
        logger.info("running.......")
    else:
        logger.info("exit 100 ........")
        exit(100)
    try:
        conn = pymysql.connect(host=DB_HOST,
                                    port=DB_PORT,
                                    user=DB_USER,
                                    passwd=DB_PWD,
                                    db=DB_DB,
                                    charset='utf8')
    except Exception as e:
        logger.info(e)
        exit(101)
    else:
        logger.info('mysql connect success')

        cx = conn.cursor()
    try:
        sql = 'SELECT * FROM order_db.t_qf_channel_order limit 10;'
        cx.execute(sql)
        results = cx.fetchall()
        logger.info(results)
        #遍历结果
        for row in results:
            pass
    except Exception as e:
        logger.info(e)
        cx.close()
        conn.close()
        exit(102)

    try:
        cx.execute(sql)
        conn.commit()
    except Exception as e:
        logger.info(e)
        conn.rollback()
        conn.commit()
        cx.close()
        conn.close()
        exit(103)

    time.sleep(30)


    cx.close()
    conn.close()


class Test(object):
    ID = 1

    def __init__(self):
        pass

    def prtID(self):
        print(self.ID)

    def classplusOne(self):
        Test.ID += 1

    def ObjplusOne(self):
        self.ID += 1

    def testPlusOne(self):
        classplusOne()


if __name__ == '__main__':
    t1 = Test()
    t2 = Test()
    #t1.classplusOne()
    t1.ObjplusOne()
    print(t1.ID)
    print(t2.ID)

    abc = 'abcd'
    for a in abc:
        print(a,'  hhhh')
    print(a)
#if __name__ == '__main__':
    #run()
