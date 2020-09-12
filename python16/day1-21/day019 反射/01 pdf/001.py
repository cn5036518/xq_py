#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/9 17:20
#@author:wangtongpei
#@email: cn5036520@163.com

# a =1
# def func():
#     a = 2
#     print(a)
#
# func()  #2  局部作用域   这里全局作用域和局部作用域的a的值是不同的
# print(a) #1   全局作用域
# print('------------------1')

a =1
def func():
    print(a)
a=2

func()  #2  局部作用域  这里全局作用域和局部作用域的a的值是相同的
print(a) #2   全局作用域
print('------------------2')

class Person:
    def eat(self):
        print('hava a breakfast')

    def play(self):
        print('play basketball')

p1 = Person()
p1.eat()  #对象调方法           写法：  对象名.方法名()
# Person.eat(p1) #和上行是等效的   写法：  类名.方法名(对象名)

Person.eat("hahafdas ")












