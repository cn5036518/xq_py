#!/usr/bin/env python
#-*- coding:utf-8 -*-

def yue(tools):  #1、形参的概念：在函数定义时候，给出来的参数是形式参数，简称形参。形参用一个变量来表示。
    print('打开手机')
    # print('打开陌陌')  #问题：这里的聊天工具是陌陌，写死了，如果要换成微信或者探探，就需要修改源代码
                       #如何不修改源代码，也能用不同的聊天工具呢？   参数来解决
    print('打开 %s' % tools)  #形参
    print('找到心仪的对象')
    print('出来吃吃饭')
    print('跳跳广场舞')

#3、传参的概念：在调用函数的过程中，把实参的值赋值给形参的过程叫做传参
yue("陌陌") #2、实参的概念：实参是函数调用的过程中给出的具体值，参数是实际参数，简称实参
print('----------------------1 陌陌')
yue("微信")
print('----------------------2 微信')
yue("探探")
print('----------------------3 探探')

'''
问题：聊天工具是陌陌，写死了，如果要换成微信或者谈谈，就需要修改源代码，不够灵活
     如何不修改源代码，也能用不同的聊天工具呢？
解决办法：参数

形参、实参、传参的概念
1、形参：在定义函数的时候，给出来的参数，就是形式参数（简称形参）
         形参用一个变量来表示。
         上述tools就是形参
2、实参：在调用函数的时候，给出来的具体值，就是实际参数（简称实参）
         上述陌陌、微信、探探就是实参
3、传参：在调用函数的时候，把实参的值赋值给形参的过程，就叫传参
         上述把陌陌、微信、探探赋值给tools的过程就是传参
'''










