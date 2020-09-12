#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/28 10:36
#@author:wangtongpei
#@email: cn5036520@163.com

#8
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def __call__(self, *args, **kwargs):
        print(self.num)

class RoleConfig(StarkConfig):
    def __call__(self, *args, **kwargs):
        print(self.num)

v1 = StarkConfig(1)
v2 = RoleConfig(11)
v1()  #1   对象名后面的小括号，会调__call__方法
v2() #11
print('----------------------8')

#9
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def run(self):
        self()
    def __call__(self, *args, **kwargs):
        print(self.num)

class RoleConfig(StarkConfig):
    def __call__(self, *args, **kwargs):
        print(345)

v1 = StarkConfig(1)
v2 = RoleConfig(11)
print(v1.run()) #v1()  1  None  #注意点：return默认是返回None
print(v2.run()) #v2()  345 None  对象名后面的小括号，会调__call__方法
print('----------------------9')

#10
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def run(self):
        self()
    def __call__(self, *args, **kwargs):
        print(self.num)

class RoleConfig(StarkConfig):
    def __call__(self, *args, **kwargs):
        print(345)
    def __getitem__(self, item):
        return self.num[item]

v1 = RoleConfig('alex')
v2 = StarkConfig("wupeiqi")
print(v1[1]) #'l'
# print(v2[2]) #报错  TypeError: 'StarkConfig' object is not subscriptable
print('----------------------10')
















