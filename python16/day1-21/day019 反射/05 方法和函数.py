#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/3 8:13
#@author:wangtongpei
#@email: cn5036520@163.com

def func1():
    pass

print(func1)  #<function func1 at 0x0000000847B2F048> 注意点：函数名后面没有小括号

class Foo:
    def common_method(self):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

    @property
    def age(self):
        return 10

f = Foo()
print(f.common_method)  #对象.普通方法名   方法    注意点：普通方法名后面没有小括号
#<bound method Foo.common_method of <__main__.Foo object at 0x000000277C5AD7C8>>
print(Foo.common_method)   #类.普通方法名  函数
#<function Foo.common_method at 0x0000001E84AA13A8>
print('----------------------1 普通方法-实例方法')

print(f.static_method)  #对象.静态方法名  函数     注意点：静态方法名后面没有小括号
#<function Foo.static_method at 0x00000034A342F438>
print(Foo.static_method) #类名.静态方法名  函数
#<function Foo.static_method at 0x00000034A342F438>
print('----------------------2 静态方法')

print(f.class_method)   #对象名.类方法名  方法    注意点：类方法名后面没有小括号
#<bound method Foo.class_method of <class '__main__.Foo'>>
print(Foo.class_method)  #类名.类方法名  方法
#<bound method Foo.class_method of <class '__main__.Foo'>>
print('----------------------3 类方法')

'''
小结：
1、类外面的函数一定是函数
2、类里面
    1、普通方法--对象来调用就是方法  类名来调用就是函数
            对象名.普通方法名  方法
              类名.普通方法名  函数
    2、静态方法--都是函数
            对象名.静态方法名  函数
              类名.静态方法名  函数
    3、类方法--都是方法
            对象名.类方法名   方法
              类名.类方法名   方法
    4、属性--是变量
       不是方法，也不是函数
'''

from types import FunctionType,MethodType

def func2(args):
    # print(args)  #<bound method Foo.class_method of <class '__main__.Foo'>>
    print(isinstance(args,FunctionType)) #False
    print(isinstance(args,MethodType))   #True
    #args的类型是方法，就返回True

func2(Foo.class_method) #类方法是方法
print('--------------1 判断类方法是方法还是函数')

def func3(args):
    print(isinstance(args,FunctionType)) #False
    print(isinstance(args,MethodType))   #False
    #args的类型是方法，就返回True

func3(Foo.age) #属性是变量（既不是函数也不是方法）
print('--------------2 判断属性是方法还是函数')

'''
小结：
isinstance(args,MethodType)和isinstance(args,FunctionType)

是用于判断函数的参数是方法还是函数类型
'''















