#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/24 16:19

''''''
'''
需求：
1、如何让对象变得可调用，即类的对象后面加上小括号不报错

思路：
类中重写__call__()方法

'''

class Foo:
    pass

f1 = Foo()
# print(f1())  #TypeError: 'Foo' object is not callable
#直接在对象后面加小括号，调用，会报错
print('--------------------1')

class Bar:
    def __call__(self, *args, **kwargs):
        print('可调用的哈')

b1 = Bar()
b1()  #可调用的哈
print('--------------------2')

'''
小结：
类中重写__call__()方法后，对象后就可以加小括号，进行调用了


'''





















