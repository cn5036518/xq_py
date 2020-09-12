#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/30 17:42

#需求1  2个整数的加法，如果不是整数，就主动抛出异常
def add(a,b):
    if type(a) != int or type(b) != int:
        # raise Exception('这里只需要int类型，不需要其他的类型')
        raise TypeError('这里只需要int类型，不需要其他的类型')
    return a+b

result = add(1,2)
print(result)  #

# add(1,2.1)  #Exception: 这里只需要int类型，不需要其他的类型
print('------------------------------1')

'''
#需求2  男澡堂来了一个女的，不让进，抛出性别异常
思路：
1、新建一个自定义的异常类，继承Exception
2、新建一个类，定义人-person
3、新加一个函数，形参是人的对象
'''

class Gender_error(Exception):   #1自定义的异常类
    pass

class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def men_bathroom(person):  #参数是Person的对象
    if person.gender != 'male':
        raise Gender_error('男澡堂，女生不能进入哈')
    else:
        print('欢饮您，先生')

p1 = Person('jack','male')
p2 = Person('lucy','female')

men_bathroom(p1)  #参数是Person的对象
# men_bathroom(p2)  #__main__.Gender_error: 男澡堂，女生不能进入哈
print('------------------------------2')

try:
    men_bathroom(p2)
except Gender_error as e:
    print(e)  #男澡堂，女生不能进入哈    这里把主动抛出的异常信息打印出来了
print('------------------------------3')

#需求3  如何在主动抛出异常信息的同时，打印堆栈的报错信息（知道哪行报错，调用关系）
import traceback

try:
    men_bathroom(p2)
except Gender_error as e:
    print(e)  #男澡堂，女生不能进入哈    这里把主动抛出的异常信息打印出来了
    val = traceback.format_exc()
    print(val)   #这里会把堆栈的报错信息打印出来
print('------------------------------4')
























