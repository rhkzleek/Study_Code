#-*- coding: utf-8 -*-
#天下支付聚合接口

#生成订单号
import time
import random,string
import platform,socket
import collections
import hashlib
import requests
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
#解析xml格式
def analysisXML(path='',text=''):
    root = ''
    if(path == ''and text == ''):
        return None
    elif(path != ''):
        root = ElementTree.parse(path)
    else:

        root = ElementTree.fromstring(text=text.decode('gbk').encode('utf-8'))
    list_node = root.getiterator("root")
    for node in list_node:
        print (node)




def requestDataPay(sp_udid = '127',bank_mch_name='txjg',bank_mch_id = '1600212',spid = '1800665296',\
                   out_channel='wxpay',pay_type='800201',tran_amt='1',auto_code='',item_name='AA哈哈AA'):
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
    if(pay_type == '800208'):
        signParam['auth_code']      = auto_code
    signParam['item_name']          = item_name
    if(out_channel == 'wxpay'):
        signParam['bank_mch_name']  = bank_mch_name
        signParam['bank_mch_id']    = bank_mch_id
    elif(out_channel == 'qqpay'):
        signParam['sp_udid']        = sp_udid

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
    signParam['sign'] = sign

    print ('********************************************')
    r = requests.post('http://api.gcdev.tfb8.com/cgi-bin/v2.0/api_wx_pay_apply.cgi',data=signParam)
    print (r.text)
    print (type(r.text))
    #analysisXML(text=r.text.encode('gbk'))

#requestDataPay()
#TestPlatform()
#getCreate_IP()

requestDataPay(pay_type='800206')