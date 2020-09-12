#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/11 8:24
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
关于反射，有下面4个函数
1、hasattr(obj,str)
    判断obj（对象、类、模块py文件）中是否有str（方法名、函数名、变量名）
2、getattr(obj,str)
    从obj（对象、类、模块py文件）中获取名字是str的属性(方法名、函数名、变量名)

#只是内存层面，并没有改变文件的内容（没有修改源代码）
3、setattr(obj,str,value)
    在obj（对象、类、模块py文件）中设置属性str（变量名、方法名、函数名）的value值
    比如：给构造方法增加一个成员变量  用的比价少，慎用
    注意点：value既可以是值，也可以是函数(匿名函数)或者方法

4、delattr（obj，str）
    从obj（对象、类、模块py文件）中删除名字是str的属性(方法名、函数名、变量名)
    比如：给构造方法删除一个成员变量（内存层面修改，构造方法的源代码没有修改）
'''

class Foo:
    pass

f = Foo()

print(hasattr(f,'eat'))   #False

setattr(f,'eat','food')  #给对象f，新增一个成员变量eat，它的值是'food'
print(f.eat)  #food

setattr(f,'self_increment',lambda x:x+1)  #给对象f，新增一个匿名函数，函数名字是self_increment
# 匿名函数是lambda x:x+1
print(f.self_increment(3))  #4













