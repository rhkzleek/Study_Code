#-*- coding: utf-8 -*-
'''python爬虫抓站的一些技巧总结'''
import urllib.request
import http.cookiejar
import urllib.parse
import json

def baseSpid(url):
    content = urllib.request.urlopen(url).read()
    print('数据:%s' %content)

def proxySpid(url):
    proxy_support = urllib.request.ProxyHandler({'http':url})
    opener        = urllib.request.build_opener(proxy_support,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    content       = urllib.request.urlopen(url).read()
    print(content)

def cookieSpid(url):
    cookie_support=urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
    print(cookie_support)
    opener = urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    content=urllib.request.urlopen(url).read()
    print (content)
#baseSpid('http://www.baidu.com')
#proxySpid('http://www.baidu.com')

def zhihuSpid(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Host':'static.zhihu.com',
        'Accept':'text/css,*/*;q=0.1',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'https://www.zhihu.com/',
        'Cookie':'q_c1=3e1a7a5088134075afee7f19abc53dad|1514422839000|1500858744000; d_c0="AEBCwWudHAyPTkeDm_eqIl-NcllhKccuMD0=|1500858745"; _zap=dc88aa13-5383-4fce-8ad2-b6c2ba917f69; __utma=51854390.323148352.1508319839.1512550601.1513932403.15; __utmz=51854390.1512550601.14.11.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=51854390.000--|2=registration_date=20150316=1^3=entry_date=20170724=1; r_cap_id="YjhkM2E4YWE3ZTA0NDJiMzk3YWUzOGE3MzcwYzIzNGQ=|1513931875|cb4ff6d45e1371e9a412177659002742f7af587f"; cap_id="OThiMzk4YTJiZDZjNDYxMWEzOTIzYmM3OGQxNzM1NTA=|1513931874|af000821e708e8531634203f64848324ea60d6b9"; capsion_ticket="2|1:0|10:1515395752|14:capsion_ticket|44:NDI0ZGNkOWQ3MDkyNGM1NDlhNTlmMTY5NzE0MDRlY2U=|188c4b820ec781569974def8ae45b99ff7c809f8e04489a7ac3fa288bf5a9942"; _xsrf=f9e4b533-3fb3-4c24-a625-8e61edeb44de; z_c0="2|1:0|10:1515395758|4:z_c0|92:Mi4xMG5NS0FRQUFBQUFBUUVMQmE1MGNEQ1lBQUFCZ0FsVk5ybWhBV3dEaE9VQ2E1c29uaHlodTFPYnBkcXNnLXlPYmt3|750749a549f4c6e03efaa8daf467d6a0bfaeedff35b68b3295fa81eea293f042"'
    }
    postdata = urllib.parse.urlencode({
        'client_id':'c3cef7c66a1843f8b3a9e6a1e3160e20',
        'grant_type':'password',
        'timestamp':'1515395758796',
        'source':'com.zhihu.web',
        'signature':'4aef0a69cf524f05fca4a74e72d2412a6810120d',
        'username':'978415719@qq.com',
        'password':'cao19931011',
        'lang':'cn',
        'ref_source':'homepage',
    }).encode(encoding='UTF-8')
    print(postdata)
    req = urllib.request.Request(url=url,data=postdata,headers=headers)
    print (req.headers)
    result = urllib.request.urlopen(req).read()
    print(result)
#cookieSpid('http://www.baidu.com')

zhihuSpid('https://www.zhihu.com/api/v3/oauth/sign_in')