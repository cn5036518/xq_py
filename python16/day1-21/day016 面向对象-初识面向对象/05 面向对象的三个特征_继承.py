#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/25 8:05
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
面向对象的三个特征：
1、封装
    1、狭义：新建对象的时候，自动调构造方法，把参数传递给构造方法，就是封装
        例子：peppa1 = Pig3('小猪佩奇',19,'嘟嘟必杀技','奥特曼')
            把name age skill hero四个参数封装到对象
    2、广义:把一些看似无关紧要的内容组合到一起统一进行存储和使用
        比如：代码块，函数，对象，类，模块-py文件都属于广义的封装
    类比：封装理解成一个黑盒
        黑盒本身接收输入，会有输出；不同的输入，会有不同的输出
            说明黑盒能满足特定功能
        把代码封装到一个黑盒子中

2、继承
3、多态
'''

#2 类的继承
#子类可继承父类的方法
class Foo:
    def func(self):
        print('我是亲爹')
    def paly(self):
        print('亲爹陪你玩')

class Foo2:
    def func2(self):
        print('我是干爹')
    def paly(self):
        print('干爹陪你玩')

class Bar(Foo):  #继承父类
    pass

b1 = Bar()
b1.func()  #我是亲爹   子类对象调父类的方法
print('----------------1 子类对象调父类的方法')

class Bar2(Foo,Foo2):  #子类同时继承2个父类
    pass

b2 = Bar()
b2.paly()  #亲爹陪你玩
#子类同时继承2个父类，子类调用2个父类都有的方法的时候，选择第一个继承的父类的方法执行（找第一个父类）
print('----------------2 子类对象调2个父类的共同方法，选第一个父类的方法执行')

class Pet:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('吃----')
    def sleep(self):
        print('睡觉----')

class cat(Pet):  #继承宠物类
    def catch_mouse(self):
        print('%s 抓老鼠----' % self.name)  #继承了父类的构造方法

class dog(Pet):  #继承宠物类
    def guard_entrance(self):
        print('守门----')

c1 = cat('mimi')
c1.catch_mouse()  #mimi 抓老鼠----















