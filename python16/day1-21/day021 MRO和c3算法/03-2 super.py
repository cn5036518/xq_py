#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/25 15:55

''''''
'''
需求：
1、子类在继承父类的时候，子类的成员变量有4个，其中3个是继承父类的成员变量，1个是子类自身的

思路：
通过super()来实现

'''

class Animal:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Cat(Animal):
    def __init__(self,a,b,c,d):  #子类的构造方法会重写父类的构造方法
        self.a = a
        self.b = b
        self.c = c
        self.d = d
print('---------------------------------1')

class Animal:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Cat(Animal):
    def __init__(self,a,b,c,d):  #子类的构造方法会重写父类的构造方法
        super().__init__(a,b,c)  #这里是子类继承父类的这3个成员变量
        # #好处：直接用父类的构造方法帮子类完成一部分代码
        # 父类的成员变量越多，这个好处就越明显
        self.d = d          #子类在继承父类的3个成员变量的基础上，自己定义一个成员变量

a1 = Animal(1,2,3)
print(a1.a)

c1 = Cat(1,2,3,4)
print(c1.a)
print(c1.b)
print(c1.c)
print(c1.d)
print(c1.__dict__)  #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 打印对象中，成员变量的名字作为key，成员变量的值作为value，形成一个字典
print('---------------------------------2')












