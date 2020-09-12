#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/9 14:17
#@author:wangtongpei
#@email: cn5036520@163.com

class Foo:
    def eat(self):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

f = Foo()
print(f.class_method) #<bound method Foo.class_method of <class '__main__.Foo'>>
print(Foo.class_method) #<bound method Foo.class_method of <class '__main__.Foo'>>
print('------------------1 类方法 都是方法')

print(f.static_method)  #<function Foo.static_method at 0x0000003F0FDC0318>
print(Foo.static_method) #<function Foo.static_method at 0x0000003F0FDC0318>
print('------------------2 静态方法 都是函数')

print(f.eat) #<bound method Foo.eat of <__main__.Foo object at 0x000000435CE4D648>>
print(Foo.eat)  #<function Foo.eat at 0x000000435CE553A8>
print('------------------3 普通方法 对象调是方法，类名调是函数')

'''
小结：
1、类方法都是方法（不管是对象调，还是类名来调）
2、静态方法都是函数（不是是对象调，还是类名来调）
3、普通方法
    对象调是方法，类名调是函数
'''

from types import MethodType,FunctionType
class Foo2:
    def eat(self):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

f2 = Foo2()

print(isinstance(f2.eat,MethodType))  #True
print(isinstance(Foo2.eat,FunctionType))  #True
print('------------------4 普通方法 对象调是方法，类名调是函数')

print(isinstance(f2.class_method,MethodType)) #True
print(isinstance(Foo2.class_method,MethodType)) #True
print('------------------5 类方法 都是方法')

print(isinstance(f2.static_method,FunctionType))
print(isinstance(Foo2.static_method,FunctionType))
print('------------------6 静态方法 都是函数')

#课上练习1
class Foo3:
    @staticmethod
    def func1():
        pass

    @classmethod
    def func2(cls):
        pass

    def func3(self):
        pass

    def func4(self):
        pass

    li = [func1,func2,func3]

f3 = Foo3()
Foo3.li.append(f3.func4)

for i in Foo3.li:
    print(i)
    # print(isinstance(i,MethodType))

# <staticmethod object at 0x0000000CD2407848>
# <classmethod object at 0x0000000CD2407A88>
# <function Foo3.func3 at 0x0000000CD23F0E58>
# <bound method Foo3.func4 of <__main__.Foo3 object at 0x0000000CD2407808>>

#False  类方法，不是方法（因为没有类名调，没有对象调）
        #类方法，都是方法（不管是对象来调，还是类名来调）
#False  静态方法，不是方法（因为没有类名调，没有对象调）
        #静态方法，都是函数（不管是对象来调，还是类名来调）
#False  普通方法，不是方法（因为没有类名调，没有对象调）
        #普通方法，对象来调就是方法，类名来调就是函数
#True  对象调普通方法，是方法
print('----------------------课上练习1')

#课上练习2
#写一个函数，判断传进来的内容是函数还是方法
from types import MethodType,FunctionType
def judge_function_method(args):
    if isinstance(args,MethodType):
        print('传进来的 %s 是方法' % args)
    elif isinstance(args,FunctionType):
        print('传进来的 %s 是函数' % args)

class Foo4:
    def eat(self):
        pass

    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

f4 = Foo4()

judge_function_method(f4.class_method)  #传进来的内容是方法
judge_function_method(f4.static_method)  #传进来的内容是函数
judge_function_method(f4.eat)  #传进来的内容是方法
print('----------------------课上练习2')




