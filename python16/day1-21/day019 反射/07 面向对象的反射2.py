#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/8 8:12
#@author:wangtongpei
#@email: cn5036520@163.com

class Person:
    # name = 'jack' #类变量
    def __init__(self,name):
        self.name = name
        self.age = None   #推荐

    def eat(self):
        # print('吃东西')
        print('吃东西 %s' % self.name)

p1 = Person('jack')
# delattr(Person,'eat')  #从类中删除函数eat
delattr(p1,'eat')  #从对象中删除eat   AttributeError: eat  注意点：这里有问题
p1.eat()  #AttributeError: 'Person' object has no attribute 'eat'

method1 = getattr(p1,'eat')  #1从对象中找eat，找到了，把eat这个方法（不是函数）的内存地址保存到变量method1
# 普通方法，对象来调用就是方法
method1()  #吃东西 jack
p1.eat()   #和上行等价
# 2method1是方法，所有默认会传入self--对象本身p1
print('------------------------ 对象调方法')

func1 = getattr(Person,'eat')
#1 从类中找eat，找到了，把eat这个函数（不是方法）的内存地址保存到变量func1
#普通方法，类名来调用就是函数（而不是方法）
# func1() #报错 这里的func1是函数，而不是方法（方法的默认参数是self），但是函数没有默认参数
#这里函数的参数是空，所有需要给这个函数传一个对象作为参数
#TypeError: eat() missing 1 required positional argument: 'self
func1(p1)  #吃东西 jack
#2这里把p1这个对象作为参数传递给函数
Person.eat(p1) #和上行等价
print('------------------------ 类名调函数 传入对象作为参数')

'''
1、对象调方法 类名调函数
对象名.方法名()     #对象调方法，参数不写，默认是self-对象本身
类名.函数名(对象名) #类名调函数，参数是对象名

上述2个写法是等效的

2、反射
method1 = getattr(p1,'eat')
    #从对象中查找，获取的是方法
func1 = getattr(Person,'eat')
    #从类中查找，获取的是函数
'''












