key = '75e9661b08891456fc4b44ae18660077'
ip_url = 'http://restapi.amap.com/v3/ip?parameters'
url = 'http://api.gcdev.tfb8.com/cgi-bin/v2.0/api_china_unionpay_upay_notify.cgi'
#curl '&signature=HeaABbNutxgxmNaeAILBDg%2b3lz21kgUdljSXNmXEmyrYzi1pfh9ox%2bdx9JBCfjsY7t0ZY2aV9K1ngwnIrD3RJKbtf9T7Jq5Us79JXrmyX1ST6Pe%2fVn1Xlf70vpGX85PuqtRoIGMArWGiA%2fvaU%2bQp8k%2bJdGpRD2GoNlPiZbEkJMdhKohQi1Uyr3MhQKg75O6P%2bup04%2fDEK9Q0ex1alw0FPL%2b%2fwgGfPruzXC%2f2kL7D4bkGjrQW30Hodd%2fFRaOAPlC5Av%2bHvZHFtGJLuzC%2fVz5635HLesAzOz3v6fFjdd3IqoptpV9ydwru42FC6R73%2bhPa%2f8TLUtn4SvUpd4L6sqjs7g%3d%3d"
import requests

postData = {'certId':'69597475696',
            'comInfo':'e0YwPTAyMDAmRjM9MDAwMDAwJkYyNT0wMCZGMzc9MjA5MjExODEyMzY4JkY2MD0wMzAwMDAwMDAwMDA3MDAxMDAwMDAwMDAwMjUwMDExMDB9',
            'currencyCode':'156',
            'encryptCertId':'70155121924',
            'orderNo':'8021800372106180209211812368',
            'orderTime':'20180209164037',
            'payInfo':'bJ11EVSebTO3KmrBUIAtIHQjg%2bjx0sJzb8Sc4t2%2fQfbkW%2bNM9nMk58rSPaEdmqVa5mZQcTEmrM9nOQ2NmLUplRt%2fI30%2f3wHja7KaVIMycL%2fnHNRsE3BeNVJkOdDRZzbQfW9HQ7oc3C1%2foZisQIyAPaKBTceUwpkfM%2bRf9nGhDYXCdiJlxS%2fKCWdNmy%2bVCn1RD3U6KSuyTfUJITDSwNa8TQYf94lHqjBEDWzZj0%2bwlLxS0xqPCXC1HMm4Fx83HMZ35pqam2gfEDWnfuMKrKOec1%2ftFQwTxveoFDjW8SFDTHRI5NXkzZdj3TddcPZGHthFClydThnbIJTnuFEBlvIU9A%3d%3d',
            'reqType':'0530000903',
            'settleDate':'0209',
            'settleKey':'49403320   00049992   4726720209164100',
            'txnAmt':'5100',
            'version':'1.0.0',
            'voucherNum':'20180209367227035408',
            'signature':'HeaABbNutxgxmNaeAILBDg%2b3lz21kgUdljSXNmXEmyrYzi1pfh9ox%2bdx9JBCfjsY7t0ZY2aV9K1ngwnIrD3RJKbtf9T7Jq5Us79JXrmyX1ST6Pe%2fVn1Xlf70vpGX85PuqtRoIGMArWGiA%2fvaU%2bQp8k%2bJdGpRD2GoNlPiZbEkJMdhKohQi1Uyr3MhQKg75O6P%2bup04%2fDEK9Q0ex1alw0FPL%2b%2fwgGfPruzXC%2f2kL7D4bkGjrQW30Hodd%2fFRaOAPlC5Av%2bHvZHFtGJLuzC%2fVz5635HLesAzOz3v6fFjdd3IqoptpV9ydwru42FC6R73%2bhPa%2f8TLUtn4SvUpd4L6sqjs7g%3d%3d'
            }

postData_1 = {'certId':'69597475696',
            'comInfo':'e0YwPTAyMDAmRjM9MDAwMDAwJkYyNT0wMCZGMzc9MjA5MjExODEyMzY4JkY2MD0wMzAwMDAwMDAwMDA3MDAxMDAwMDAwMDAwMjUwMDExMDB9',
            'currencyCode':'156',
            'encryptCertId':'70155121924',
            'orderNo':'8021800372106180209211812368',
            'orderTime':'20180209164037',
            'payInfo':'bJ11EVSebTO3KmrBUIAtIHQjg+jx0sJzb8Sc4t2/QfbkW+NM9nMk58rSPaEdmqVa5mZQcTEmrM9nOQ2NmLUplRt/I30/3wHja7KaVIMycL/nHNRsE3BeNVJkOdDRZzbQfW9HQ7oc3C1/oZisQIyAPaKBTceUwpkfM+Rf9nGhDYXCdiJlxS/KCWdNmy+VCn1RD3U6KSuyTfUJITDSwNa8TQYf94lHqjBEDWzZj0+wlLxS0xqPCXC1HMm4Fx83HMZ35pqam2gfEDWnfuMKrKOec1/tFQwTxveoFDjW8SFDTHRI5NXkzZdj3TddcPZGHthFClydThnbIJTnuFEBlvIU9A==',
            'reqType':'0530000903',
            'settleDate':'0209',
            'settleKey':'49403320   00049992   4726720209164100',
            'txnAmt':'5100',
            'version':'1.0.0',
            'voucherNum':'20180209367227035408',
            'signature':'HeaABbNutxgxmNaeAILBDg+3lz21kgUdljSXNmXEmyrYzi1pfh9ox+dx9JBCfjsY7t0ZY2aV9K1ngwnIrD3RJKbtf9T7Jq5Us79JXrmyX1ST6Pe/Vn1Xlf70vpGX85PuqtRoIGMArWGiA/vaU+Qp8k+JdGpRD2GoNlPiZbEkJMdhKohQi1Uyr3MhQKg75O6P+up04/DEK9Q0ex1alw0FPL+/wgGfPruzXC/2kL7D4bkGjrQW30Hodd/FRaOAPlC5Av+HvZHFtGJLuzC/Vz5635HLesAzOz3v6fFjdd3IqoptpV9ydwru42FC6R73+hPa/8TLUtn4SvUpd4L6sqjs7g=='
            }


#r = requests.post(url=url,data=postData_1)

import json

with open("D:\GitHub\Study_Code\Python_advance_learn_code\.idea\inspectionProfiles\data_json.txt", "rb+") as fp:                        # open with 'read and write' mode
    data = fp.read()
    data = json.loads(data)

