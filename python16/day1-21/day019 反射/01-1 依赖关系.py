#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/1/9 7:24
#@author:wangtongpei
#@email: cn5036520@163.com

#大象装冰箱
''''''
'''
伪代码：
1、定义大象类和冰箱类
2、大象类的普通方法
    1、开门
    2、装自己
    3、关门
3、冰箱类的普通方法
    1、开门
    2、关门
4、大象类的普通方法的参数是冰箱对象  --重点
   大象类的普通方法体是冰箱对象.冰箱的普通方法
'''

class Elephant:
    def __init__(self,name):
        self.name = name

    def open_fridge_door(self,f1):  #参数是冰箱对象
        print('%s 同学，请开门吧' % f1.brand)
        f1.open_door()#冰箱对象.冰箱对象的方法

    def put_yourself_in(self):
        print('把自己装进去')

    def close_fridge_door(self,f1):
        print('%s 同学，请关门吧' % f1.brand)
        f1.close_door() #冰箱对象.冰箱对象的方法

class Fridge:
    def __init__(self,brand):
        self.brand = brand

    def open_door(self):
        print('冰箱开门')

    def close_door(self):
        print('冰箱关门')

e1 = Elephant('jack')
f1 = Fridge('gree')

e1.open_fridge_door(f1)
# gree 同学，请开门吧
# 冰箱开门

e1.put_yourself_in()
#把自己装进去

e1.close_fridge_door(f1)
# gree 同学，请关门吧
# 冰箱关门













