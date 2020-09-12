#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/25 19:31

from collections import namedtuple

nt1 = namedtuple('point',['x','y'])
print(type(nt1))
p1 = nt1(1,2)
print(p1)  #point(x=1, y=2)
print(type(p1))




















