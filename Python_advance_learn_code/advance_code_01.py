#coding=utf-8

'''
    *argsd和**kwargs的用法
    主要用于函数定义,你可以将不定数量的参数传输给一个函数
'''

def test_var_args(f_arg, *argv):
    print 'first normal arg:', f_arg
    for arg in argv:
        print 'another arg through *argv:',arg


test_var_args('yasoob','python','eggs', 'test')