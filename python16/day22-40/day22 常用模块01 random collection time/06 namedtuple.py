#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/14 7:23

from collections import namedtuple

po = namedtuple('point',('x','y'))   #创建一个命名元组  相当于定义一个类
p = po(1,2)   #相当于创建一个对象
print(p)  #point(x=1, y=2)
print(type(po))  #<class 'type'>
print(type(p))  #<class '__main__.point'>

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

p1 = Point(2,3)


















