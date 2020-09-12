#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 8:15

''''''
'''
需求：
1、小明开了一个男澡堂，来了一个女的，让进么，不让进，主动抛出性别异常--raise
2、要求能够看到堆栈的报错信息

思路：
0、引入traceback模块
1、自定义一个性别异常的异常类，继承异常的基类
2、定义一个人的类，构造方法，传入参数姓名和性别
3、定义一个函数，参数是人的对象
   如果人的对象的性别不是男，就raise一个性别异常，给出提示语
4、新建2个人的对象
5、调函数，传入2个人的对象，try except捕获和处理异常
    引入traceback来打印堆栈报错信息
'''

import traceback

# 1、自定义一个性别异常的异常类，继承异常的基类
class Gender_error(Exception):
    pass

# 2、定义一个人的类，构造方法，传入参数姓名和性别
class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# 3、定义一个函数，参数是人的对象
#    如果人的对象的性别不是男，就raise一个性别异常，给出提示语
def bashroom_men(person):
    if person.gender != '男':  #对象调成员变量
        raise Gender_error('这里是男澡堂哈，女生不能入内')

# 4、新建2个人的对象
p1 = Person('jack','男')
p2 = Person('lucy','女')

# 5、调函数，传入2个人的对象，try except捕获和处理异常
try:
    bashroom_men(p1)
    bashroom_men(p2)
except Gender_error as e:
    val = traceback.format_exc()   #打印堆栈信息，返回字符串保存在val中
    print(e)   #这里是男澡堂哈，女生不能入内
    print(val)   #把堆栈的报错信息，作为字符串保存在变量val后，打印出来
except Exception as e:
    print(e)

'''


'''















