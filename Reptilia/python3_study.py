#!/usr/local/env python3
#-*- coding:utf-8 -*-

import requests

def requests_test001():
    r = requests.get('https://www.baidu.com/')
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(r.cookies)


if __name__ == '__main__':
    requests_test001()