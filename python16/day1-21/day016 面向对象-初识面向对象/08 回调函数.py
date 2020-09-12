#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/30 10:05
#@author:wangtongpei
#@email: cn5036520@163.com

# 回调的英文定义：
#
# A callback is a function that is passed as an argument to another function
# and is executed after its parent function has completed。#
#
# 字面上的理解，回调函数就是一个参数，将这个函数作为参数传到另一个函数里面，
# 当那个函数执行完之后， 再执行传进去的这个函数。这个过程就叫做回调。
#
# 其实也很好理解对吧，回调，回调，就是回头调用的意思。主函数的事先干完，回头再调用传进来的那个函数。

def mainfunc(callback):   #形参是回调函数的函数名字
    callback()  #这里的形参() 就是调用回调函数
    print('我是主函数')

def callb():  #回调函数
    print('我是回调函数')

mainfunc(callb)  #实参是回调函数的名字
# 我是回调函数
# 我是主函数











