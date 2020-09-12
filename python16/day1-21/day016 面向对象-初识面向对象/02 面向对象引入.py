#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/23 7:01
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
多态的概念引入
1、小明是一个具体的人-对象（实例）
2、小明是人类，也是动物类，也是学生类，还是中国人这个类
   上述一个具体对象，从不同的角度，分别属于不同的类，就是多态

面向对象的引入
真实世界：
造一辆车的步骤：
1、画车的设计图
2、开始制造

程序世界：
造一辆车的步骤：
1、定义一个car的类（类比：画车的设计图）
'''

#1 定义类，类的对象，对象的属性-变量
class Car:  #定义一个类  表示车这个类型
    pass

c1 = Car() #创建一个对象，一个具体的车（比如你家的tesla）
c1.colour = '黑色'   #具体车tesla的属性  车的颜色
c1.plate = '京A11111'  #具体车tesla的属性  车的车牌
c1.capacity = '2t'  #具体车的属性 车的排量
c1.owner = 'jack'   #具体车对象的属性 车主

c2 = Car() #创建一个对象，一个具体的车（比如你家的保时捷）
c2.colour = '白色'   #具体车的属性  车的颜色
c2.plate = '京B22222'  #具体车tesla的属性  车的车牌
c2.capacity = '1.8t'  #具体车的属性 车的排量
c2.owner = 'tom'   #具体车对象的属性 车主
print(c2.colour)  #白色
print('------------------------1 对象的属性')

#2 类的构造方法-初始方法
class Car:
    def __init__(self,colour,plate,capacity,owner):  #构造方法是车这个类的出场设置  这个里self就是当前的对象  关键点1
        # self.colour = '灰色'  #这么写，所有的车对象都是灰色
        self.colour = colour   #这里的self就相当于c1 c2
        self.plate = plate
        self.capacity = capacity
        self.owner = owner
        print('我在制造汽车，车的颜色是 %s' % self.colour)

c1 = Car('红色','京A11111','1.8t','jack')  #制造一辆红色的车
# c1.colour = '灰色'
print(c1.__dict__)  #{'colour': '红色', 'plate': '京A11111', 'capacity': '1.8t', 'owner': 'jack'}
# 把对象的属性名和属性值打印出来，字典的形式  #注意点：__dict__后面没有小括号
print(c1.colour)  #红色
c1.colour = '黑色'  #车出厂是红色，这里把红色改成黑色
#类比：字典的键值对的value的修改
print(c1.colour)  #黑色

# c2 = Car('蓝色','京B22222','1.5t','tom')  #制造一辆蓝色的车
# # 创建车的对象，自动调构造方法  关键点2
# print(c2.colour)  #蓝色
print('------------------------2 类的构造方法')

#3 类的普通方法
class Car:
    def __init__(self,colour,plate,capacity,owner):  #构造方法是车这个类的出场设置  这个里self就是当前的对象  关键点1
        # self.colour = '灰色'  #这么写，所有的车对象都是灰色
        self.colour = colour   #这里的self就相当于c1 c2
        self.plate = plate
        self.capacity = capacity  #属性-变量
        self.owner = owner
        print('我在制造汽车，车的颜色是 %s' % self.colour)

    #车可以跑起来，普通方法--动作
    def run(self):
        print('%s 车在路上跑起来了' % self.colour)
        #这里self.colour可以在不同的方法之间使用  #关键点
        #这里的self是当前的对象

c1 = Car('红色','京A11111','1.8t','jack')  #新建对象，字典调构造方法
c1.run()  #红色 车在路上跑起来了
print('------------------------3 类的普通方法')







