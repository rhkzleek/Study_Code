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
        #yield x                        #生成器函数发送协议
        #print(x.next)
        print(lambda x,y: x+y)        #生成匿名函数

        x if y else 6                  #三元选择表达式
        x and y, x or y, not x         #逻辑与，逻辑或，逻辑非
        x in y, x not in y             #成员对象测试
        x is y, x is not y              #实体对象测试
        x < y,x <=y, x>y,x>=y,x==y,x!=y #大小比较,集合子集或者超集值相等性操作符
        1<4<3                           #python中容许连续比较
        3<<2,4>>2                       #位操作，x左移，右移y位
        print (-1,+1,~1)                #一元减法,识别,按位求取(取反)
        x[1],x[1:2:3],x(...)            #索引,分片,调用
        int(3.14),float(3)              #强制类型转换


        #整数可以利用bit_length函数测试所占的位数
        a = 1;  a.bit_length()       #1
        a = 1024; a.bit_length()     #11


        #repr和str显示格式的区别
        '''
        repr 格式: 默认的交互回显,产生的结果看起来他们就像世代码
        str 格式: 打印语句,转化成一种对用户更加友好的格式
        '''
        #数字相关的模块
        #math模块
        #Decimal模块,小数模块
        import decimal
        from decimal import Decimal
        Decimal('0.01') + Decimal('0.02')           #返回Decimal('0.03')
        decimal.getcontext().prec = 4                #设置全局精度为4,即小数点后边4位
        #Fraction模块:分数模块
        from fractions import Fraction
        x = Fraction(4,6)                           #分数类型4/6
        x = Fraction('0.25')                        #分数类型1/4接收字符串类型的参数

if __name__ == '__main__':
    TypesAndOper()