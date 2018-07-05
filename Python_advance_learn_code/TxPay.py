#-*- coding: utf-8 -*-
#天下支付聚合接口

#生成订单号
import time
import random,string
import platform,socket
import collections
import hashlib
import requests
import json
import sys
#sys.setdefaultencoding('utf8')

#platform 模块的用法
def TestPlatform():
    #获取Python版本
    print(platform.python_version())
    #获取操作系统可执行程序结构(32bit,windowsPE)
    print (platform.architecture())
    #计算机网络名称
    print (platform.node())
    #计算机处理器信息 'Interl 64'
    print (platform.processor())
    #获取操作系统中的python构建日期
    print (platform.python_build())
    #获取系统中python解释器的信息
    print (platform.python_compiler())

    if platform.python_branch()=='':
        print (platform.python_implementation())
        print (platform.python_revision())

    print (platform.release())
    print (platform.system())

    #获取操作系统版本
    print (platform.version())
    #获取上面的所有信息
    print (platform.uname())

#得到本地IP地址
def getCreate_IP():
    sysstr = platform.system()
    if(sysstr=='Windows' or sysstr == 'Linux'):
        localIP= socket.gethostbyname(socket.gethostname())
        print ('local ip:%s' %localIP)
        #的到本机的IP列表，包含内部和外部
        ipList = socket.gethostbyname_ex(socket.gethostname())
        print (ipList)
        for i in ipList:
            if i != localIP:
                print ('external IP:%s' %i)
        return localIP
    else:
        print ('other system')
        return None




#生成length长度的随机数字符串
def createRandomNum(length):
    #numOfNum = random.randint(1,length-1)
    slcNum = [random.choice(string.digits) for i in range(length)]
    random.shuffle(slcNum)
    randomNum = ''.join([i for i in slcNum])
    return randomNum

#生成length长度的订单号,长度至少为16位
def createBillNo(num):
    if (num < 16):
        return  None
    #获取时间戳，并格式化
    curTime = time.strftime('%Y%m%d%H%M%S',time.localtime())
    #print curTime
    #订单号
    billNo = 'test'+ curTime + createRandomNum(num-16)
    return billNo

def creartSign(st):
    m = hashlib.md5()
    m.update(st)
    return m.hexdigest()
#def dict2Kv(signParam):
from xml.etree import ElementTree

def print_node(node):
    #print(node.attrib)
    print(node.tag)
    print(node.text)
#解析xml格式
def analysisXML(path='',text=''):
    root = ''
    if(path == ''and text == ''):
        return None
    elif(path != ''):
        root = ElementTree.parse(path)
    else:

        root = ElementTree.fromstring(text=text)
    #list_node = root.getiterator("root")
    #for node in list_node:
        #print_node(node)
    node_find = root.find('root')
    print_node(node_find)









def requestDataPay(sp_udid = '127',bank_mch_name='txjg',bank_mch_id = '1600212',spid = '1800665296',\
                   out_channel='wxpay',pay_type='800201',tran_amt='1',auto_code='',item_name='AA哈哈AA',input_charset='UTF-8'):
    signParam = {}
    #signParam = collections.OrderedDict()
    signParam['spid']               = spid
    signParam['notify_url']         = 'www.baidu.com'
    signParam['sp_billno']          = createBillNo(26)
    signParam['spbill_create_ip']   = getCreate_IP()
    signParam['out_channel']        = out_channel
    signParam['pay_type']           = pay_type
    signParam['tran_time']          = time.strftime('%Y%m%d%H%M%S',time.localtime())
    signParam['tran_amt']           = tran_amt
    signParam['cur_type']           = 'CNY'
    #signParam['input_charset']     = input_charset
    if(pay_type == '800208'):
        signParam['auth_code']      = auto_code
    signParam['item_name']          = item_name
    if(out_channel == 'wxpay'):
        signParam['bank_mch_name']  = bank_mch_name
        signParam['bank_mch_id']    = bank_mch_id
    elif(out_channel == 'qqpay'):
        signParam['sp_udid']        = sp_udid
    print(signParam.items())
    signParam2 = sorted(signParam.items(), key=lambda d:d[0], reverse=False)
    print (signParam2)
    #转换为KV串
    reqMsg = ''
    for k in signParam2:
        reqMsg += k[0]
        reqMsg += '='
        reqMsg += k[1]
        reqMsg += '&'
    reqMsg += 'key='
    reqMsg += 't-Vn:7LFS4'
    sign = creartSign(reqMsg.encode('utf8')).upper()
    #signParam['item_name']          = item_name.encode('gbk')
    signParam['sign'] = sign

    print ('********************************************')

    r = requests.post('http://api.gcdev.tfb8.com/cgi-bin/v2.0/api_wx_pay_apply.cgi',data=signParam)
    print (r.text)
    print (type(r.text))
    #analysisXML(text=r.text)

def requestPayQry(spid='1800665296',input_charset='UTF-8',listid=''):
    signParam = {}
    signParam['listid'] = listid
    signParam['input_charset'] = input_charset
    signParam['spid'] = spid

def nbPingAn():
    appid_1 = '20171128222506194087'
    appid = '20171221092135403541'
    app_secret_1= '072f529e542599ff4b18108dedf95b42'
    app_secret='c8a5798dca77b4d83620e81c4b03e8bd'
    store_id = '248714'
    requestUrl = 'http://api.w2wpay.com/gateway'

    signParam = dict()
    signParam['app_id'] = appid
    signParam['method'] = "openapi.merchant.pool.query"
    signParam["format"] = "json"
    signParam["sign_method"] = "md5"
    signParam["nonce"] = createRandomNum(32)
    signParam["biz_content"] = "{}"
    signParam['version'] = '1.0'
    signParam2 = sorted(signParam.items(), key=lambda d: d[0], reverse=False)
    print(signParam2)
    reqMsg = ''
    for k in signParam2:
        reqMsg += k[0]
        reqMsg += '='
        reqMsg += k[1]
        reqMsg += '&'
    print (reqMsg[0:len(reqMsg)-1])
    reqMsg2= reqMsg[0:len(reqMsg)-1]
    reqMsg = reqMsg2 + app_secret
    print(reqMsg)
    print(len(signParam['nonce']))

    sign = creartSign(reqMsg.encode('utf-8')).upper()
    signParam['sign'] = sign

    json_str = json.dumps(signParam)
    print(signParam)
    print(json_str)
    r = requests.post(requestUrl,data=json_str)
    print(r.text)

def test0001():
    signParam=dict()
    contents=''

    headers = {
        'Host': 'oss.gcdev.tfb8.com',
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept - Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept - Encoding': 'gzip, deflate',
        'Referer': 'http://oss.gcdev.tfb8.com/user_infor/user_info_add.shtml',
        'Cookie': "JSESSIONID=AB044B0BBADEBB2718E7791F42305111.gcpaytest081; JSESSIONID=0A12BB1FFFDE5499964B14A5E2F11DC1.gcpaytest081; sid=434467460271e882a93aba6583d8a25f; user_id=10132; verifySession=qooa0qnkbbcegvehjp0wnrfdcp8pf99gfdjczertu0mhi6z3ag",
        'Connection': "keep-alive"
    }
    filename = 'D:/unionpayacp_jigou.pfx'
    filename = 'D:/acp_prod_enc.cer'
    filename = 'D:/acp_prod_verify_sign.cer'
    f = open(filename,"rb")
    contents = f.read()
    signParam["file_content"] = "unionpayacp_jigou.pfx"
    signParam["file_content"] = "acp_prod_enc.cer"
    signParam["file_content"] = "acp_prod_verify_sign.cer"
    print(contents)
    files = {
        "file_content": open(filename, "rb")
    }
    print(signParam["file_content"])
    signParam["pay_channel"] = "UNIONPAY"
    signParam["feature"] = "556555222"
    signParam["file_name"] = signParam["file_content"]
    signParam["bussi_type"] = "1"
    signParam["sub_type"]   = "2"
    if(signParam["sub_type"] == "1"):
        signParam["pfx_pwd"] = "gczf"
    requestUrl = 'http://oss.gcdev.tfb8.com/cgi-bin/v1.0/aggreagtion_binfile_upload.cgi'

    r = requests.post(requestUrl,headers=headers,data=signParam,files=files)
    print(r.text)

import logging;
logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)

    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


#requestDataPay()
#TestPlatform()
#getCreate_IP()

#requestDataPay(pay_type='800206')

#nbPingAn()
#test0002()