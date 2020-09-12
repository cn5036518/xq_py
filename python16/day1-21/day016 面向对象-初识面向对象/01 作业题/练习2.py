#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/30 6:07
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
6.	面向对象中的self指的是什么？
    指的是当前正在执行动作的对象

7.	以下代码体现面向对象的什么特点？
    class A:   #定义类
          def __init__(self,name,age,hobby):
              self.name = name
              self.age = age
              self.hobby = hobby
     a1 = A('jack',19,'run')

     封装：把姓名，年龄，爱好等一系列属性封装到了一个对象之中

8.	以下代码体现面向对象的什么特点？
    class Message:
        def email(self):
            pass
        def msg(self):
            pass
        def wechat(self):
            pass
    封装：把不同的动作方法封装到一个类中

9. 看代码写结果

10.	定义一个类，其中有计算周长和面积的方法（圆的半径通过参数传递到构造方法）。
'''
class Foo:
    def func(self):
        print('foo.func')
f1 = Foo()
ret1 = f1.func()
print(ret1)  #none
print('--------------------------------9 ')

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2*math.pi*self.radius
        print(perimeter)

    def calculate_area(self):
        area = math.pi*self.radius**2
        print(area)

c1 = Circle(1)  #新建对象
c1.calculate_perimeter()  #6.283185307179586
c1.calculate_area()  #3.141592653589793















