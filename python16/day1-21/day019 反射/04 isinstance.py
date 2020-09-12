#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/2 11:25
#@author:wangtongpei
#@email: cn5036520@163.com

class Animal:
    pass

class Cat(Animal):
    pass

class Bosicat(Cat):
    pass

a = Animal()
print(isinstance(a,Animal))  #True  对象a是Animal类型
print(isinstance(a,Cat)) #False    对象a不是Cat类型
print('----------------------1')

b1 = Bosicat()
print(isinstance(b1,Bosicat))  # True   对象b1是Bosicat类型
print(isinstance(b1,Cat))      # True   对象b1是Cat类型--父类
print(isinstance(b1,Animal))   # True   对象b1是Animal类型--祖父类
print('----------------------2')












