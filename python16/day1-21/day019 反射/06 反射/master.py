#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/6 9:06
#@author:wangtongpei
#@email: cn5036520@163.com

def eat():
    print('吃饭')

def drink():
    print('喝水')

def play():
    print('玩耍')

name = 'jack'

class Person:
    # name = 'jack' #类变量
    def __init__(self,name):
        self.name = name
        self.age = None   #推荐

    def eat(self):
        # print('吃东西')
        print('吃东西 %s' % self.name)












