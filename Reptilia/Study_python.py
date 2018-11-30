#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import math
import decimal
import fractions
'''
    类型和运算
'''
def TypesAndOper():
    # -- 寻求帮助
    print(dir(decimal))
    print(decimal.__doc__)
    print(help(int))

    #测试类型的三种方法,推荐第三种
    L = []
    if type(L) == type([]):
        print('L is list')
    if type(L) == list:
        print('L is list')
    if isinstance(L,list):
        print('L is list')

    #-- Python数据类型:哈希类型,不可哈希类型
        #哈希类型，即在原地不能改变的变量类型,不可变类型,可利用hash函数查看其hash值，也可以作为字典的key
        "数字类型: int,float,decimal.Decimal,fractions.Fraction,complex"
        "字符串类型: str， bytes"
        "元组: tuple"
        "冻结集合, frozenset"
        "布尔类型: True, False"
        "None"
        #不可hash类型: 原地可变类型: list,dict,和set,它们不可以作为字典的key

    #数字常量
        1234,-1234,0,9999999                #整数
        1.23,1,3.14e-10,4E210,4.0e+210      #浮点数
        0o177,0x9ff,0x9FF,0b101010          #八进制,十六进制,二进制数字
        3+4j,3.0+4.0j,0j,3j                 #复数常量也可以用complex（real,image)来创建
        hex(18),oct(18),bin(18)             #将十进制转化为十六进制,八进制,二进制表示
        int('20',base=8)                  #将字符串转化为整数,base为进制数
        #2.x中两种整数类型,一般整数(32位),和长整数(无穷精度).可以用l和L结尾,使一般整数成长为长整数
        print(float('inf'),float('-inf'), float('nan')) #无穷大，无穷小,非数

    #数字的表达式
        x = ['1','2','3']
        y = ['4','5','6']
        #yield x
        #print(x.next)
        print(lambda x,y: x+y)

        x if y else 6



if __name__ == '__main__':
    TypesAndOper()