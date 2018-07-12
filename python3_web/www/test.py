#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import chardet

print(dir(requests))

r = requests.get('http://www.baidu.com')
print('content--> %s' % r.content)
print('text-->%s' % r.text)
print('encoding--> %s' % r.encoding)

print(type(r))

print(dir(requests.models.Response))


#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#headers = {'User-Agent':user_agent}
#r = requests.get('http://www.baidu.com',headers=headers)

for cookie in r.cookies.keys():
    print(cookie,':',r.cookies.get(cookie))


import re
def test001():
    pattern = re.compile(r'\d+')
    #result1 = re.match(pattern,'abc192')
    result1 = re.search(pattern,'abc193edf')
    if result1:
        print(result1.group())
    else:
        print('匹配失败2')

from bs4 import BeautifulSoup

def test002():
    html_str = r.content
    soup = BeautifulSoup(html_str,'lxml',from_encoding='utf-8')
    print(soup.name, soup.attrs)
    print('test:%s' %soup)
    print(soup.a)

import json

def test003():
    user_agent  = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    headers = {'User-Agent':user_agent}
    r = requests.get('http://seputu.com',headers=headers)
    print (r.text)
    soup = BeautifulSoup(r.text, 'html.parser',from_encoding='utf-8')
    content = []
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')
        if h2 != None:
            h2_title = h2.string
            list = []
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.get('title')
                print(href,box_title)
                list.append({'href':href, 'box_title':box_title})
            print('***************************************************')
            content.append({'title':h2_title,'content':list})
    print('******************************')
    print(type(content))
    with open('D:/qiyi.json','wb') as fp:
        fp.write((json.dumps(content)).encode('utf-8'))
        fp.close()
        #json.dump(content,fp=fp,indent=4)
from email.header import Header
from  email.mime.text import MIMEText
from  email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
def test004():
    from_addr = 'caoguanghuaplus@163.com'
    password = 'cao1993'
    to_addr = '978415719@qq.com'
    smtp_server = 'smtp.163.com'
    msg = MIMEText('Python 爬虫运行异常,异常信息为遇到Http 403','plain','utf-8')
    msg['From'] = _format_addr('一号爬虫<%s>' % from_addr)
    msg['To']   = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('一号爬虫运行状态','utf-8').encode()

    server = smtplib.SMTP(smtp_server,25)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
#test001()
#test002()
#test003()
test004()
