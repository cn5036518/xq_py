#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/14 7:07

from collections import deque

d = deque()
d.append('jack')  #向后追加
d.append('tom')
d.append('bob')
print(d)   #deque(['jack', 'tom', 'bob'])
print(type(d))  #<class 'collections.deque'>

d.appendleft('kate')  #从左边添加
print(d)  #deque(['kate', 'jack', 'tom', 'bob'])

d.pop()  #删除右边最后一个
print(d)  #deque(['kate', 'jack', 'tom'])

d.popleft() #删除左边最后一个
print(d)  #deque(['jack', 'tom'])












































