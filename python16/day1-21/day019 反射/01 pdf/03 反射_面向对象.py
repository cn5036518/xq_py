#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/9 15:56
#@author:wangtongpei
#@email: cn5036520@163.com

from types import FunctionType,MethodType

class Person:
    def __init__(self,name):
        self.name = name
        pass

    def eat(self):
        print('hava a breakfast')

    def play(self):
        print('play basketball')

p1 = Person('jack')
p1.eat()  #对象调方法           写法：  对象名.方法名()
Person.eat(p1) #和上行是等效的   写法：  类名.方法名(对象名)


print(isinstance(p1,Person))  #True  对象p1的类型是Person类
print(isinstance(Person,type)) #True 类Person的类型是type

print(type(p1)) #<class '__main__.Person'>  对象p1的类型是Person类
print(type(Person)) #类Person的类型是type

print('----------------1')

def reflect(scope,args,p=None):  #参数1查找范围（对象、类、py文件）  参数2要查找的内容（方法、函数、变量）
    #参数3--对象名
    if hasattr(scope,args):
        result = getattr(scope,args)
        # print(result)
        if callable(result):
        # if isinstance(result,FunctionType) or isinstance(result,MethodType):
            if isinstance(scope,type): #如果参数1--scope本身是类
                #参数1如果是对象名，参数2是类名，判断对象是否属于类
                #参数1如果是类名，参数2是type，这里的type不能加引号，加引号就是字符串 判断参数1的类型是否是类
                result(p)  #这里的p
                print('----- 类，新建对象后，对象调方法')
            else: #2 如果参数1-obj是对象
                result()#如果是从对象中查找到方法的内存地址，直接加上小括号调用
                print('----- 对象调方法')
        else:
            print(result)
            print('获取的内容不是函数或者方法')
    else:
        print(args)
        print('你也要查找的内容，在指定范围没有查到，请重新输入')

reflect(p1,'name')  #jack
#从对象中查找变量name
reflect(p1,'eat')  #jack
#从对象中查找方法eat
reflect(Person,'play',p1)  #hava a breakfast  参数3是对象名
#从类中查找函数eat

'''
小结：
一、对象调方法的2种写法
写法1：
    对象名.方法名()   #参数不写，默认是self-对象本身
写法2：
    类名.函数名(对象名) #函数的参数，必须是对象名才行
    （函数和方法的不同：方法的参数不写，默认是self-对象本身
                       函数的参数不写，默认是空）

二、如何判断一个变量是类还是对象
   isinstance(args,type)
   如果上述判断成立，那么args就是类（所有的类名，它的类型都是type）

   isinstance(obj，类名)
   判断对象名obj是否属于参数2-类名，如果是的话，上述返回True

'''













