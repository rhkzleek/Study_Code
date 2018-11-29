#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import codecs
from bs4 import  BeautifulSoup
import datetime


class QunaSpider(object):
    def get_hotel(self,driver,to_city,fromdate,todate):

        ele_toCity = driver.find_element_by_name('toCity')
        ele_fromDate = driver.find_element_by_id('fromDate')
        ele_toDate   = driver.find_element_by_id('toDate')
        ele_search   = driver.find_element_by_class_name('search-btn')

        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_toCity.click()
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_search.click()

        page_num = 0
        while True:
            try:
                WebDriverWait(driver,10).until(EC.title_contains(str(to_city)))
            except Exception as e:
                print(e)
                break
            time.sleep(5)

            htm_const = driver.page_source
            soup = BeautifulSoup(htm_const,'html.parser',from_encoding='utf-8')
            infos = soup.find_all(clas_="item_hotel_info")
            f = codecs.open(str(to_city) + str(fromdate) + u'.html','a','utf-8')
            for info in infos:
                f.write(str(page_num) + '--'*50)
                content = info.get_text().replace(" ","").replace("\t","").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
                f.close()
                try:
                    next_page = WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element_by_css_selector(".item.next")))
                    next_page.click()
                    page_num += 1
                    time.sleep(10)
                except Exception as e:
                    print(e)
                    break

    def crawl(self,root_url,to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Firefox(executable_path='F:/phantomjs-2.1.1-windows/bin/geckodriver.exe')
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        driver.maximize_window() #将浏览器最大化显示
        driver.implicitly_wait(10) #控制间隔时间,等待浏览器反应
        self.get_hotel(driver,to_city,today,tomorrow)

import re
import requests

def get_xsrf(session,headers):
    '''_xsrf是动态变化的参数,从网页中提取'''
    index_url = 'http://www.zhihu.com'
    #获取登录时需要用到的_xsrf
    index_page = session.get(index_url,headers=headers)
    html = index_page.text
    print(html)
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern,html)
    print(_xsrf)
    return _xsrf[0]

def login_zhihu():
    agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    headers = {
        'User-Agent':agent
    }
    session = requests.session()
    _xsrf = get_xsrf(session,headers)
    post_url = 'http://www.zhihu.com/login/phone_num'
    postdata = {
        '_xsrf':_xsrf,
        'password':'cao19931011',
        'remember_me':'true',
        'phone_num':'978415719@qq.com'
    }
    login_page = session.post(post_url,data=postdata,headers=headers)
    login_code = login_page.text
    print(login_page.status_code)
    print(login_code)
def tetst001():
    sss = 'ashah tetst jdjaa test iii'
    if 'test' in sss:
        print('success')
    else:
        print('fail')

from lxml import etree
import requests

def  test22002():


    url = 'https://www.zhihu.com/#signin'
    z = requests.get(url)
    sel = etree.HTML(z.content)
    # 这个xsrf怎么获取 我们上面有讲到
    _xsrf = 'f1b05627-15b2-4fd8-ab16-74ee63e088aa'#sel.xpath('//input[@name="_xsrf"]/@value')[0]
    loginurl = 'https://www.zhihu.com/login/email'
    # 这里的_xsrf就是我们刚刚上面得到的
    formdata = {
        'email':'978415719@qq.com',
        'password':'cao19931011',
        '_xsrf':_xsrf
    }
    z2 = requests.post(url=loginurl,data=formdata)
    print (z2.status_code)
     #200
    print (z2.content)
    # '{"r":0,\n "msg": "\\u767b\\u5f55\\u6210\\u529f"\n}'
    #print (z2.json()['msg'])
# 登陆成功
class A(object):
    def foo1(self):
        print('a hello ',self)
    @staticmethod
    def foo2():
        print('b hello')
    @classmethod
    def foo3(cls):
        print('c hello',cls)
        #a = A()
        cls.foo2()


import rsa

pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(512)
    # 明文编码格式
    content = str.encode('utf-8')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con


(a, b) = rsaEncrypt("hello")
print('加密后密文：')
print(a)
content = rsaDecrypt(a, b)
print('解密后明文：')
print(content)

szSqlReq = "";
szSqlReq += "( Fremark,Fspid, FbatchNo,Fregister_no,Fpay_channel,FmerchantId,FpayWay,FmerchantName,";
szSqlReq += " FshortName, FmerchantAddress,FservicePhone, FcontactName, FcontactPhone,";
szSqlReq += " FcontactMobile, FcontactEmail, Fcategory, FidCard, FmerchantCode, Freg_type,"
szSqlReq += " Fsecret, Fappid_flag, Fappid, Fappid_secret, Fcity_no, Fbusiness_no, Fday_limit_amt,"
szSqlReq += " Fextend1, Fpay_channel_name, Ftime_period_start, Ftime_period_end, Fday_deal_count,Fday_deal_success_count";
szSqlReq += " Flimit_amt_low, Flimit_amt_high) ";

szSqlReq2 = "";
szSqlReq2 += "'" + m_inParams["remark"] + "', ";
szSqlReq2 += "'" + m_inParams["spid"] + "', ";
szSqlReq2 += "Fbatch_no, Fregister_no, Fpay_channel, CONCAT(Fregister_no,'_',Fpay_channel,'_',Finformation_no), "
szSqlReq2 += "'" + m_inParams["FpayWay"] + "', ";
szSqlReq2 += "Fmerchant_name, Fshort_name, Faddress, Fcompany_tel, Fcontact_name, Fco" \
             "ntact_mobile, Fcontact_tel, Fmail, Fcatagory, ";
szSqlReq2 += "Fowner_idcard, Fmerchant_code, '1', ";
szSqlReq2 += "'" + m_inParams["secret"] + "', ";
szSqlReq2 += "'1', Fappid, Fappid_secret, Fcity_no, Fbusiness_no, ";
szSqlReq2 += "'" + m_inParams["day_limit_amt"] + "', ";
szSqlReq2 += "Fextend1, Fpay_channel_name, "
szSqlReq2 += "'" + m_inParams["time_avail_start"] + "', ";
szSqlReq2 += "'" + m_inParams["time_avail_end"] + "', ";
szSqlReq2 += "'" + m_inParams["day_deal_count"] + "', ";
szSqlReq2 += "'" + m_inParams["day_deal_success_count"] + "', ";
szSqlReq2 += "'" + m_inParams["limit_amt_low"] + "', ";
szSqlReq2 += "'" + m_inParams["limit_amt_high"] + "' ";


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


t1 = Test()
t2 = Test()
t1.classplusOne()

#test22002()
#if __name__ == '__main__':
    #driver = webdriver.Firefox(executable_path='F:/phantomjs-2.1.1-windows/bin/geckodriver.exe')
    #driver.get('http://www.baidu.com')

    #assert u"百度" in driver.title
    #elem = driver.find_element_by_name("wd")
    #elem.clear()
    #elem.send_keys(u"网络爬虫")
    #elem.send_keys(Keys.RETURN)
    #time.sleep(3)
    #assert u"网络爬虫." not in driver.page_source
    #driver.close()
    #spider = QunaSpider()
    #spider.crawl('http://hotel.qunar.com/',u'上海')
    #login_zhihu()
    #test22002()

