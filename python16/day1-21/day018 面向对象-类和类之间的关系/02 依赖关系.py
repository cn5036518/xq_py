#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/15 8:46
#@author:wangtongpei
#@email: cn5036520@163.com

""""""
'''
需求：要把大象装冰箱
伪代码思路：
1、新建2个类，大象类和冰箱类
2、关系：大象类要依赖冰箱类
3、大象类--成员方法：
    1、开冰箱门--依赖冰箱类--传入冰箱对象
    2、装自己
    3、关冰箱门--依赖冰箱类
4、冰箱类--成员方法：
    1、开门
    2、关门

需求2：要把大象装高压锅  -这里的冰箱和高压锅  多态
伪代码思路：
1、新建2个类，大象类和高压锅类
2、关系：大象类要依赖高压锅类
3、大象类--成员方法：
    1、开高压锅门--依赖高压锅类--传入高压锅对象
    2、装自己
    3、关高压锅门--依赖高压锅类
4、高压锅类--成员方法：
    1、开门
    2、关门
'''
class Elephant:  #大象类
    def __init__(self,name):
        self.name = name

    def open_one_door(self,obj):  #开xx的门  形参是冰箱对象
        # （想要的是一个冰箱-泛指，具体是哪个冰箱没有指定-没有特指）
        #这里的obj是多态  即可以是冰箱，也可以是高压锅  关键点1
        #这里是依赖关系，依赖是冰箱或者高压锅
        print('%s 同学，开门吧' % obj.name)
        obj.open_door()  #冰箱对象.冰箱类的成员方法()  开门方法
        #这里的obj既可以是冰箱也可以是高压锅，换句话说，只要这个对象有open_door（）这个成员方法，都可以

    def pack(self): #装入
        print('把自己装进去')

    def close_one_door(self,obj): #关xx的门  形参是冰箱对象
        # 这里的obj是多态  即可以是冰箱，也可以是高压锅  关键点2
        print('%s 同学，关门吧' % obj.name)
        obj.close_door()  #冰箱对象.冰箱类的成员方法()  关门方法

class Bridge:  #冰箱类
    def __init__(self,name):
        self.name = name

    def open_door(self):  # 开门
        print('开门')

    def close_door(self):  # 关门
        print('关门')

class Pressure_cooker:   #高压锅类
    def __init__(self,name):
        self.name = name

    def open_door(self):  # 开门
        print('开门')

    def close_door(self):  # 关门
        print('关门')

e1 = Elephant('jack') #1 新建对象，自动调构造方法
b1 = Bridge('haier')  #2 新建冰箱对象--海尔
e1.open_one_door(b1) #3 大象对象调成员方法-开xx的门，传入的实参是冰箱对象
# haier 同学，开门吧
# 开门
e1.pack()
#把自己装进去
e1.close_one_door(b1)
#haier 同学，关门吧
# 关门
print('------------------1 大象开冰箱门')

p1 = Pressure_cooker('gree')  #2 新建高压锅对象-格力
e1.open_one_door(p1) #3 大象对象调成员方法-开xx的门，传入的实参是高压锅对象
print('------------------2 大象开高压锅门')
# gree 同学，开门吧
# 开门

'''
小结：
1、依赖是一种松耦合的关系
    大象开冰箱门，冰箱坏了，大象还可以开高压锅门
2、多态思想
    大象开冰箱门，开高压锅门  冰箱和高压锅对象就是多态
3、依赖的写法
    1、类a依赖类b
       大象类依赖冰箱类
    2、类a的成员方法，形参是类b的对象
       类a的成员方法的内容： 类b的对象.类b的成员方法()
4、依赖的概念
    在方法中引入另一个类的对象
5、没有特指
    大象开冰箱门，想要的对象是一个冰箱-泛指，
        具体是哪个冰箱（是那台haier冰箱，还是这台美的冰箱）没有指定--没有特指（这台还是那台）


'''
















