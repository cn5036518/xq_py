#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/11 7:40

''''''
'''
需求：
    通过抽象类和抽象方法，对子类的方法进行约束
'''

from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta): #包含抽象方法的类就是抽象类，抽象类的概念
    @abstractmethod    #包含这个，就是一个抽象方法，抽象方法的概念
    def eat(self):
        pass

class Cat(Animal):  #子类继承抽象类，必须要重写父类中的抽象方法，否则新建子类对象的时候，会报错
    pass

# cat = Cat() #TypeError: Can't instantiate abstract class Cat with abstract methods eat
'''
1、父类是抽象类，抽象类不能新建对象
2、子类如果继承了抽象类，但是没有重写父类的抽象方法的话
   子类也是抽象类，子类也不能新建对象
3、子类继承抽象类后，就必须重写父类的抽象方法，才能新建子类对象

'''
from abc import ABCMeta,abstractmethod

class Base(metaclass=ABCMeta):    #抽象类
    @abstractmethod   #抽象方法
    def login(self):
        pass

class Normal2(Base):   #1 张三编写
    def login(self):   #2 重写父类的抽象方法
        print('普通会员登录')

class Member2(Base):  #2 李四编写
    def denglu(self):  #2 没有重写父类的抽象方法，新建对象的时候会报错
        print('吧务登录')

class Admin2(Base):  #3 王五编写
    def login(self):   #2 重写父类的抽象方法
        print('管理员登录')

def logining(obj):  # 4 架构师编写，参数是上述角色的对象
    obj.login()
    print('请输入验证码')
    print('欢迎登录主页')

#新建3个对象
n2 = Normal2()
# m2 = Member2()    #子类必须重写父类的抽象方法，否则子类无法创建对象--对子类的约束
# #TypeError: Can't instantiate abstract class Member2 with abstract methods login
a2 = Admin2()

#3 调登录入口，传入角色对象
logining(n2)
logining(a2)

'''
关于约束的2种方式：
1、python中推荐使用raise NotImplementedError的方式
   原因是：简单
2、而抽象类、抽象方法、接口主要是java c#使用的

主动抛出异常和抽象类的区别
1、前者，如果子类没有重写父类的方法，子类的对象可以正常创建，只是把子类对象当做参数传入的时候，会报错
2、后者，如果子类没有重写父类的抽象方法，子类的对象创建就会报错
'''















