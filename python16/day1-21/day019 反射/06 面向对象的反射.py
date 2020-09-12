#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/7 7:23
#@author:wangtongpei
#@email: cn5036520@163.com

from types import FunctionType

class Person:
    # name = 'jack' #类变量
    def __init__(self,name):
        self.name = name
        self.age = None   #推荐

    def eat(self):
        # print('吃东西 %s' % Person.name)
        print('吃东西 %s' % self.name)

p1 = Person('刘伟')
print(p1.name)  #刘伟

# age1 = setattr(p1,'age',18)  #给对象p1 添加一个变量 age，赋值是18
# 注意：setattr的结果不需要变量来接收，和getattr不同
setattr(p1,'name','jack')
print(p1.name)  #修改构造方法中的变量  从刘伟修改成jack  #不建议使用
setattr(p1,'age',18)  #给对象p1 添加一个变量 age，赋值是18
#很少使用，慎用，推荐在构造方法中写 self.age = None  见11行
print(p1.age)  #18

delattr(p1,'age')  #删除变量 age
# print(p1.age)
#AttributeError: 'Person' object has no attribute 'age'

# delattr(p1,'name')  #删除变量 age
# print(p1.name)
#AttributeError: 'Person' object has no attribute 'name'

# delattr(Person,'eat')  #从类中删除eat函数
# delattr(p1,'eat')  #AttributeError: eat   注意点：从对象中删除eat属性 有问题
# p1.eat()  #AttributeError: 'Person' object has no attribute 'eat'

#注意： setattr和delattr都是在内存层面，并没有修改文件
print('-------------------1 setattr delattr')

while 1:
    val = input('请输入你要查找函数名或者变量名:')

    # if hasattr(p1,'eat'):#0 参数1：对象  参数2：要查找的函数名或者变量名  这里的参数2定义死了
    if hasattr(p1,val):#0 参数1：对象  参数2：要查找的函数名或者变量名   这里的参数2可以自定义输入
        # 判断参数1中是否有参数2
        attr1 = getattr(p1,val)  #1 参数1，对象  参数2：要查找的函数名或者变量名
        #从对象p1中查找函数名或者变量名'eat',找到了就获取内存地址
        # if callable(attr1):  #判断获取的是函数内存地址还是变量的内存地址
        if isinstance(attr1,FunctionType): #和上行等效
            attr1()   #吃东西 刘伟  2函数的内存地址加上小括号 就是调用函数
        else:
            print('你获取的是变量，而不是函数')
            print(attr1)  #不是函数，就打印变量的值

        func2 = getattr(Person,val)  #3 参数1，类名  参数2：要查找的函数名或者变量名
        # func2() #
        #TypeError: eat() missing 1 required positional argument: 'self'
        func2(p1)  #这里必须要传入对象才行
    else:
        print('对象中没有找到你要找的函数或者变量')
print('-------------------2 getattr hasattr')



'''
反射小结：
1、重点
getattr(对象名,函数名或者变量名)
    参数列表：参数1是对象或者类，参数2是要查找的函数名或者变量名
    作用：从对象中（对象或者类中）查找指定的内容
    使用：找到后将内存地址存在变量中，变量名后面加上小括号，就是调用函数
        ret1 = getattr(p1,'eat')  #或者函数eat的内存地址
        ret1() #函数的内存地址后面加上小括号

hasattr(对象名,函数名或者变量名)
    参数列表：参数1是对象或者类，参数2是要查找的函数名或者变量名
    作用：判断对象中（对象或者类中）是否有你要查找的指定内容 和if
    使用：有的话，就接着使用getattr
         没有的话，就提示没有你要找的指定内容
         if hasattr(p1,'eat'):  #注意点：函数名加上引号
            ret1 = getattr(p1,'eat')  #或者函数eat的内存地址
            ret1() #函数的内存地址后面加上小括号
         else:
            print('你要查找的内容不存在')

2、次重点 在内存层面修改，文件并没有修改
setattr(对象名,变量名,变量值)
    参数列表：参数1是对象或者类，参数2是变量名，参数3是变量的值
    作用：给对象（对象或者类）的构造方法中，新增一个变量--内存层面，临时增加
    setattr(p1,'age',18)  #注意点：变量名要加上引号

delattr(对象名,变量名)
    参数列表：参数1是对象或者类，参数2是变量名
    作用：删除类中构造方法的一个变量--内存层面，临时删除
    delattr(p1,'age')   #注意点：变量名要加上引号
    delattr(p1,'name')
'''










