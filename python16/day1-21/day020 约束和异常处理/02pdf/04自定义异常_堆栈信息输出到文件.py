#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 8:15

''''''
'''
需求：
1、小明开了一个男澡堂，来了一个女的，让进么，不让进，主动抛出性别异常--raise
2、要求能够看到堆栈的报错信息，并且将堆栈的报错信息接入到文件中

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
    print(e)   #这里是男澡堂哈，女生不能入内
    # val = traceback.format_exc()   #打印堆栈信息，返回字符串保存在val中  黑色字体
    #  format_exception()的缩写是format_exc()
    # print(val)
    # traceback.print_exc()   #直接打印堆栈信息  红色字体   #和上面的2行是等效的
    # print_exc()是print_exception()的缩写
    traceback.print_exc(file=open('traceback.log','a+'))   #把堆栈报错信息追加写入到文件中
    #  a 是追加写，不可读
    #  a+是追加写+读
except Exception as e:
    print(e)

'''
小结：
format_exc()和print_exc()的区别
1、format_exc()是format_exception()的简写
   把堆栈报错信息，作为字符串，保存到变量val，然后打印出val
2、print_exc()是print_exception()的简写
    把堆栈报错信息，直接打印出来
    另外，后者可以把堆栈报错信息，写入到日志文件

文件读写中a 和a+的区别
1、a是追加写，不可读
2、a+是追加写，可读
'''















