#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/9 10:30
#@author:wangtongpei
#@email: cn5036520@163.com

class Foo:
    pass

f1 = Foo()
print(type(f1))  #<class '__main__.Foo'>
if type(f1)==Foo:   #写法 type(对象名)==类名
    print('对象f1属于类Foo')

'''
type函数用于判断对象是什么类型的？（对象是哪个类）
写法 type(对象名)==类名 （判断对象名是否属于类）

应用场景：
1、统计男生女生的人数
   男生和女生各定义一个类
2、计算的时候，要求传入的参数是int或者float
    限制传入参数的类型

'''

#需求：统计男生和女生的人数分别是多少？

class Boy:
    pass

class Girl:
    pass

b1 = Boy()  #新建2个男生对象
b2 = Boy()

g1 = Girl()  #新建3个女生对象
g2 = Girl()
g3 = Girl()

li1 = [b1,b2,g1,g2,g3]

def statistifical_quantity(args):  #1函数名字用英语全称
    numbers_of_boys = 0   #2变量名字用英语全称
    numbers_of_girls = 0
    print(args)#[<__main__.Boy object at 0x0000003FD910DE48>,
    # <__main__.Boy object at 0x0000003FD910DE88>,
    # <__main__.Girl object at 0x0000003FD910DEC8>,
    # <__main__.Girl object at 0x0000003FD910DF08>,
    # <__main__.Girl object at 0x0000003FD910DF48>]
    print(type(args))  #<class 'list'>  参数args是列表，列表的元素是2个男生对象和3个女生对象
    for i in args:
        if type(i) == Boy:
            numbers_of_boys += 1
        elif type(i) == Girl:
            numbers_of_girls += 1
    return numbers_of_boys,numbers_of_girls

result1 = statistifical_quantity(li1)  #3变量名字用英语全称
print(result1)  #(2, 3)
print('-----------------------1 type 统计人数')

def statistifical_quantity2(*args):  #1函数的形参的星号(动态参数)，接受的是一个元组
    numbers_of_boys = 0   #2变量名字用英语全称
    numbers_of_girls = 0
    print(args)  #(<__main__.Boy object at 0x000000A8A072DE88>,
    # <__main__.Boy object at 0x000000A8A072DEC8>,
    # <__main__.Girl object at 0x000000A8A072DF08>,
    # <__main__.Girl object at 0x000000A8A072DF48>,
    #  <__main__.Girl object at 0x000000A8A072DF88>)
    print(type(args))  #<class 'tuple'>  参数args是一个元组，元组的元素是2个男生对象和3个女生对象
    for i in args:
        if type(i) == Boy:
            numbers_of_boys += 1
        elif type(i) == Girl:
            numbers_of_girls += 1
    return numbers_of_boys,numbers_of_girls

li1 = [b1,b2,g1,g2,g3]
result1 = statistifical_quantity2(*li1)  #3函数的实参的星号，把列表的而每一个元素打包成元组  注意点
print(result1)  #(2, 3)
print('-----------------------2 type 统计人数')

#需求2 计算的时候，要求传入的参数是int或者float
# 限制传入参数的类型
def add(a,b):
    pass
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        print(a+b)  #注意点：int和str不能直接拼接+
    else:
        print('请输入数字或者小数')

add(-1,1.3)
add('jack',1)  #请输入数字或者小数
print('-----------------------3 type  限制传入参数的类型')












