#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/2 6:40
#@author:wangtongpei

def func(x):  #1普通函数
    return x**2
ret1 = func(5)
print(ret1)  #25
print(func)  #<function func at 0x00000030296B20D8>
# 这里的func是普通函数的函数名
print('-----------------1 普通函数')

func2 = lambda x:x**2  #匿名函数的定义   lambda关键字后面，冒号前面是参数，冒号后面是返回值
print(func2) #<function <lambda> at 0x0000004A32342168>
# 这里的lambda是匿名函数的标识
ret2 = func2(2)  #这里-数字2是匿名函数的参数，ret2是返回值
print(ret2)  #4
print('-----------------2 匿名')

def func31(a,b):  #普通函数写法
    return a+b

func3 = lambda a,b:a+b
ret3 = func3(1,2)
print(ret3)  #3
print('-----------------3 匿名 2个参数')


'''
匿名函数的适用范围：
1、简单的函数可以用匿名函数
2、复杂的函数不适合用匿名函数

匿名函数可以和列表推导式组合使用

'''
















