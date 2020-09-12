#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 13 有如下函数:
# def wrapper():
#     		def inner():
#         		print(666)
# 	wrapper()
#
# 你可以任意添加代码,用两种或以上的方法,执行inner函数.

#方式1
def wrapper():
    def inner():
        print(666)
    inner()
wrapper()
print('-------------------1')

#方式2
def wrapper():
    def inner():
        print(666)
    return inner   #函数名字可以当做变量，返回（return后面可以接内嵌的函数名字）  #装饰器的雏形
ret1 = wrapper()
ret1()


















