#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/2 6:10
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
类中的方法分类：
1、成员方法-实例方法-最常见
    1、写法
        第一个参数是self，对象本身
    2、调用
        对象来调用成员方法

2、静态方法-函数
    1、写法
        1、参数，不需要传self
        2、方法名字前面加上@staticmethod
    2、调用
        类名来调用静态方法
    3、例子
        字典中的fromkeys 就是一个静态方法
    4、适用场景
        当做函数来看

3、类方法
    1、写法
        1、第一个参数是cls，表示类名
        2、方法名上方加上@classmethod
    2、调用
        类名来调用类方法
    3、适用场景
        可以在类方法中创建对象
'''

class Person:
    def __init__(self): #构造方法，成员变量-实例变量
        pass

    def marry(self): #1 成员方法，第一个参数是self，对象来调用-最常见
        print('我是成员方法')

    @staticmethod   #@表示装饰器  2  静态方法，不传参数self，类名来调用，当做函数来看
    def calculate(a,b):  #这里不需要传self 当做函数
        print('我是静态方法')
        return a+b

    @classmethod  #3 类方法 第一个参数是cls，表示类名，可以用于在类方法中创建对象
    def clsmethod(cls):
        p1 = cls()  #新建对象
        print(p1)  #<__main__.Person object at 0x0000003C9092AC08>
        print('我是类方法')
        c1 = cls()  #类名()  创建对象

p1 = Person()
p1.marry()  #我是成员方法   #成员方法用对象来调

ret1 = Person.calculate(2,3)  #我是静态方法  #静态方法用类名来调，当做函数来看
print(ret1) #5

Person.clsmethod()  #我是类方法  #类方法用类名来调
























