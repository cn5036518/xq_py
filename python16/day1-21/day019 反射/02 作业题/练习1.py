#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/11 8:42
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
1、类变量和实例变量的区别
    一、类变量
        1、位置
            在类中，方法外
        2、全局属性
            类变量是类中的全局属性，类似一个共享内存，比如：统计学生人数
            类中的方法都可以对类变量进行修改
        3、写法
            类变量一遍是类名来调用
        4、归属
            类变量归属-类

    二、实例变量（普通变量）
        1、位置
            在类中，方法内
        2、实例变量在构造方法中定义，可以在不同的方法中使用
        3、写法
            实例变量前面一般是对象self
        4、归属
            实例变量归属-对象

2、super的作用--nok

3、isinstance和type的区别并用代码举例说明
    一、type
        1、可以判断一个变量的数据类型
           比如：str int  list tuple dict set等
        2、可以判断一个对象-实例属于哪个自定义的类
            比如：p1是自定义类Person的对象，可以通过type(p1)输出p1所属的自定义类
        3、适用场景
            计算2个整数的和的函数，要求参数是整数
            就用type(a)==int来判断

    二、isinstance
        1、可以判断一个对象-实例是否属于一个类（包括父类）
            参数1是对象，参数2是类，如果对象是类创建的，就返回True
        2、可以判断参数1的数据类型是否是一个自定义类
            参数1是自定义类名，参数2是type（不带引号）
            如果返回True，说明参数1的数据类型是自定义类名
            如果返回False，说明参数1的数据类型不是自定义类名
            原因：所有的类名（不管是自定义类，还是list等系统自带的类）
                  它的类型都是type
        3、适用场景
            函数或者方法的参数，要求是老师这个类及其子类的对象，就用isinstance来判断
            如果返回是false，就不然传入，raise异常

    举例：
    1、cat对象就是animal这个父类，可以用isinstance
        只要是animal这个家族的成员，都可以用isinstnce来判断，并且返回true
        --家族概念
    2、type只能判断cat对象的精确类型是cat类，cat对象的精确类型不能是animal类
       --精确类型

'''

#1 类变量和实例变量的区别的例子
class Foo:
    number_of_students = 0  #类变量
    def __init__(self,name):
        self.name = name  #self.name是实例变量

    def register(self):
        Foo.number_of_students += 1  #类名调类变量--全局
        # self.number_of_students += 1
        print('学生的人数是',Foo.number_of_students)
        # print('学生的人数是',self.number_of_students)

f1 = Foo('jack')
f1.register()  #学生的人数是 1
f2 = Foo('tom')
f2.register()  #学生的人数是 2
print('--------------1 类变量和实例变量的区别的例子')

#2 type和isinstance的区别的例子
# 一、type
# 1、可以判断一个变量的数据类型
# 比如：str# int# list# tuple# dict# set等
s1 = 'jack'
print(type(s1))  #<class 'str'>

li1 = [1,2]
print(type(li1))  #<class 'list'>
print('--------------2-1 type 判断变量的数据类型')

# 2、可以判断一个对象 - 实例属于哪个自定义的类
# 比如：p1是自定义类Person的对象，可以通过type(p1)
# 输出p1所属的自定义类
class Person:
    pass
p1 = Person()
print(type(p1)) #<class '__main__.Person'>
print('--------------2-2 type 判断实例对象所属的自定义类')

# 二、isinstance
# 1、可以判断一个对象 - 实例是否属于一个类
# 参数1是对象，参数2是类，如果对象是类创建的，就返回True
print(isinstance(p1,Person))  #True
print('--------------2-3 isinstance 判断实例属于哪个类')

# 2、可以判断参数1的数据类型是否是一个自定义类
print(isinstance(Person,type)) #True
print('--------------2-4 isinstance 判断参数1是否是自定义类名')










