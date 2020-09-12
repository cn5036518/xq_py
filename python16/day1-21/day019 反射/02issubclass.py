#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/1/31 9:53
#@author:wangtongpei
#@email: cn5036520@163.com

class Animal:
    pass

class Cat(Animal):
    pass

class Bosicat(Cat):
    pass

print(issubclass(Cat,Animal))  #True
#判断参数1是否是参数2的子类（孙子类）--后代
print(issubclass(Animal,Cat))  #False
print(issubclass(Bosicat,Animal))  #True













