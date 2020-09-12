#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
1、什么是异常？what
    异常可以理解成为一个对不正常事情的处理机制
    一般情况下，在python无法正常处理程序时就会发生一个异常。
2、异常处理的好处（为什么要用异常处理？）：why
    可以让错误变得更加人性化。
3、异常处理的写法？how
    1、捕捉异常可以使用try/except语句
    2、try/except语句 用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
4、应用场景
    如果你不想在异常发生时结束你的程序，只需要在try里捕获它。
"""
# f=open("log1.txt","r")

#1 try...except...else
try:
    f=open("log1.txt","r")
except IOError as e:  #固定写法 as e
    print("错误\n",str(e))  #将报错的提示(原来类型是class)转换成字符串
    # print("错误\n",e)  #
    # print(type(e)) #<class 'FileNotFoundError'>
    # print(type(str(e))) #<class 'str'>
else:  #如果没有报错，即文件是存在的，就执行else
    print("success")

#2 try...except...finally
#这个finally后的语句块，是指无论是否发生异常，都会执行的代码块。--what
# 一般用于关闭文件，释放数据库链接等--适用场景
try:
    f=open("log2.txt","r")
except IOError as e:  #固定写法 as e
    print("错误\n",str(e))  #将报错的提示(原来类型是class)转换成字符串
else:  #如果没有报错，即文件是存在的，就执行else
    print("success2")  #success2
finally:
    f.close() #关闭文件

#3 是否允许多个except分钟存在？--可以的
#  try...except...except...else...finally
try:
    f=open("log2.txt","r")
except IOError as e:  #固定写法 as e   读写错误
    print("错误\n",str(e))  #将报错的提示(原来类型是class)转换成字符串
except NameError as e:  #  变量不存在
    print("错误\n",str(e))
else:  #如果没有报错，即文件是存在的，就执行else
    print("success2")  #success2
finally:
    f.close()

"""
常见异常的类型
1 NameError  尝试访问一个没有申明的变量
2 ZeroDivisionError 除数是0
3 SyntaxError 语法错误
4 IndexError   索引超出序列范围
5 KeyError      请求一个不存在的字典key
6 IOError       输入输出错误（比如你要读取的文件不存在）
7 AttributeError 尝试访问未知的对象属性
8 ValueError    传给函数的参数类型不正确（比如给int（）函数传入字符串类型）
9 BaseException 所有异常的基类
10 Exception    常见错误的基类


"""















