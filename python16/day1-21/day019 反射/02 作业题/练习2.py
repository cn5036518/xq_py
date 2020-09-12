#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/12 7:40
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
第4题
判断函数的参数是否可以被调用，是的话，打印调用后的返回值
不是的话，直接打印参数
2个办法
callable  isinstance
'''
import master
from types import FunctionType,MethodType

#方法1 callable()
def func1(args):
    if hasattr(master, args):
        attribute1 = getattr(master,args)  #参数1是模块py文件（还可以是类、对象）
        if callable(attribute1):
            attribute1()   #吃饭
        else:
            print(attribute1) #jack

func1('eat')
func1('name')
print('-------------1 callable 判断对象是否可以被调用')

#方法2 isinstance()
def func2(args):
    if hasattr(master,args): #1 参数2-属性在指定范围（参数1-对象、类、模块py文件）是否能找到
        attribute1 = getattr(master,args)
        #1 从指定范围（参数1-对象、类、模块py文件）获取参数1（属性-函数、方法、变量等）
        if isinstance(attribute1,FunctionType):
            #判断参数1是否是函数（对象调方法，类调函数）
            attribute1()
        else:
            print(attribute1)
func2('eat')
func2('name')
print('-------------2 isinstance 判断对象是否可以被调用')


'''
小结：
目前可以被调用的对象有哪些？
1、函数    函数名()           执行函数
2、方法    对象名.方法()      通过对象调用方法
3、类      类名()            新建对象  初始化对象   __new__   __init__
4、对象    对象名()          执行__call__    py特有的


'''


'''
第5题
动态参数 *args
计算动态参数中函数、方法、类对象的个数，并返回给调用者
'''

def func_dynamic_parameters(*args):
    print(len(args))  #3
    print(args)  #('eat', 'drink', 'play')
    for i in args:#遍历循环
        if hasattr(master,i):
            attribute1 = getattr(master,i)
            if callable(attribute1):
                attribute1()  #是函数，就调用
            else: #不是函数，是变量，就打印变量
                print(attribute1)  #jack
                # <master.Person object at 0x000000FF50112488>  打印p1对象
        else:
            print('你输入的字符串-函数名、方法名、变量名，'
                  '在指定范围-对象、类、py文件，没有找到，请重新输入')
    # print(*args)  #eat drink play  #这个一般不用

li1 = ['eat','drink','play','name','p1']   #3个函数名 和1个变量名 一个对象名
func_dynamic_parameters(*li1)
#实参*li1 实参的星号* 是把列表['eat','drink','play']转换成元组('eat','drink','play')
# 传递参数给形参 *args  次数形参args就是元组('eat', 'drink', 'play')










