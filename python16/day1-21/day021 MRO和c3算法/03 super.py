#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/25 15:44

''''''
'''
需求：
1、子类在继承父类的时候
   子类方法和父类方法同名的时候，会重写父类的方法
   但是在重写的过程中，还要调用父类这个被重写的方法，怎么办呢？

思路：
在子类的方法中引入super().父类方法名()

'''

class Animal:
    def eat(self):
        print('动物吃')

class Cat(Animal):
    def eat(self):  #将父类的方法重写了
        print('小猫吃鱼')

c1 = Cat()
c1.eat()  #小猫吃鱼
print('---------------------------1 重写')

class Animal2:
    def eat(self):
        print('动物吃')

class Cat2(Animal):
    def eat(self):  #将父类的方法重写了
        super().eat()  #重写父类方法的同时，在这里调用父类的方法  #这里的super()表示父类
        print('小猫吃鱼')

c2 = Cat2()
c2.eat()  #动物吃
          #小猫吃鱼
print('---------------------------2 重写2')



















