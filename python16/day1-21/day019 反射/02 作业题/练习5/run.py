#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/15 11:14
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
1、获取handler.py中所有的成员名称：dir（handler）
2、获取handler.py中名字叫Base的成员--反射  getattr()
3、检查其他成员是否是Base的子类（不包含Base），如果是则创建对象并添加到空列表li1中

'''

import handler  #导入py文件

def func():
    li1 = []
    name_li1 = dir(handler)  #1 获取某个文件中所有成员名称（包含py文件有哪些类，哪些内置函数）
    return name_li1

ret1 = func()
print(ret1)
#['Base', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', '__builtins__',
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print('----------------------- dir(handler)  1 获取某个文件中所有成员名称')

# if hasattr(handler,'Base'):
#     attribute1 = getattr(handler,'Base')
#     if callable(attribute1):
#         attribute1()  #我是Base类
# print('----------------------- getattr()  2 获取handler.py中名字叫Base的成员--反射')

#3、检查其他成员是否是Base的子类（不包含Base），如果是则创建对象并添加到空列表li1中
li2 = []
for i in ret1:
    if hasattr(handler,i):
        attribute1 = getattr(handler,i) #1获取handler这个py文件中的全部成员
        attribute_base = getattr(handler,ret1[0]) #2获取py文件中的Base这个类
        if isinstance(attribute1,type) \
                and issubclass(attribute1,attribute_base) \
                and attribute1 != attribute_base:
            #判断条件1： py文件中的成员，过滤成是类的   isinstance(attribute1,type)
            #判断条件2：py文件中的成员，需要是Base类的子类
            #判断条件3：py文件中的成员，不能是Base类本身
            # print(attribute1)
            li2.append(attribute1())  #符合条件的类，创建对象后，追加到空列表
print(li2)



