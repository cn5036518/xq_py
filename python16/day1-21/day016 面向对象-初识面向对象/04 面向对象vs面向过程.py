#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/24 7:32
#@author:wangtongpei
#@email: cn5036520@163.com

#需求1：要把大象装冰箱
#方法1：面向过程--脚本
print('打开冰箱门')
print('把大象装进去')
print('关上冰箱门')
print('------------------1 面向过程')

#方法2：函数式编程--可以重复使用（面向过程）
def open_fridge():
    print('打开冰箱门')
def put_into():
    print('把大象装进去')
def close_fridge():
    print('关上冰箱门')

open_fridge()
put_into()
close_fridge()
print('------------------2 函数式编程')

#方法3：面向对象
#把这个装大象封装到大象这个类中
class Elephant:
    def open_door(self):
        print('打开冰箱门')

    def put_into(self):
        print('把自己装进去')

    def close_door(self):
        print('关上冰箱门')

elephant = Elephant()  #新建对象
elephant.open_door()
elephant.put_into()
elephant.close_door()
print('------------------3 面向对象')

# 练习2 小猪佩奇大战奥特曼. 说. 有一个小猪, 名叫佩奇, 今年40岁了了. 会使用嘴巴嘟嘟必杀技. 他
# 不光大战奥特曼, 还会⼤战蝙蝠侠, 蜘蛛侠
#方法1 面向过程-函数式编程
def pk_altman(name,age,skill):
    print('姓名%s,年龄%s,技能%s 打奥特曼' % (name,age,skill))
def pk_batman(name,age,skill):
    print('姓名%s,年龄%s,技能%s 打蝙蝠侠' % (name,age,skill))
def pk_spider_man(name,age,skill):
    print('姓名%s,年龄%s,技能%s 打蜘蛛侠' % (name,age,skill))
pk_altman('小猪佩奇',18,'嘟嘟必杀技')
pk_batman('小猪佩奇',18,'嘟嘟必杀技')
pk_spider_man('小猪佩奇',18,'嘟嘟必杀技')
print('------------------2-1 面向过程-函数式编程')

#方法2 面向对象
#分析：小猪佩奇是一只猪，建一个猪的类
#001
class Pig:
    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
    def pk_altman(self):
        print('姓名%s,年龄%s,技能%s 打奥特曼' % (self.name,self.age,self.skill))
    def pk_batman(self):
        print('姓名%s,年龄%s,技能%s 打蝙蝠侠' % (self.name, self.age, self.skill))
    def pk_spider_man(self):
        print('姓名%s,年龄%s,技能%s 打蜘蛛侠' % (self.name, self.age, self.skill))
peppa = Pig('小猪佩奇',18,'嘟嘟必杀技')  #新建对象，自动调构造方法
peppa.pk_altman() #对象调方法
peppa.pk_batman()
peppa.pk_spider_man()
print('------------------2-2-1 面向对象')

#002
class Pig2:
    def __init__(self,name,age,skill):
        self.name = name
        self.age = age
        self.skill = skill
    def pk_hero(self,cartoon):
        print('姓名%s,年龄%s,技能%s 打%s' % (self.name,self.age,self.skill,cartoon))

peppa = Pig2('小猪佩奇',19,'嘟嘟必杀技')  #新建对象，自动调构造方法
peppa.pk_hero('奥特曼') #对象调方法  传入参数
peppa.pk_hero('蝙蝠侠') #对象调方法
peppa.pk_hero('蜘蛛侠') #对象调方法
print('------------------2-2-2 面向对象')
#一个对象把同一个方法调用3次，分别传入不同的参数

#003   推荐
class Pig3:
    def __init__(self,name,age,skill,cartoon):
        self.name = name
        self.age = age
        self.skill = skill
        self.cartoon = cartoon
    def pk_hero(self):
        print('姓名%s,年龄%s,技能%s 打%s' % (self.name,self.age,self.skill,self.cartoon))

peppa1 = Pig3('小猪佩奇',19,'嘟嘟必杀技','奥特曼')  #新建对象1，自动调构造方法
peppa2 = Pig3('小猪佩奇2',20,'嘟嘟必杀技','蝙蝠侠')  #新建对象2，自动调构造方法
peppa3 = Pig3('小猪佩奇3',21,'嘟嘟必杀技','蜘蛛侠')  #新建对象3，自动调构造方法

peppa1.pk_hero()
peppa2.pk_hero()
peppa3.pk_hero()
print('------------------2-2-3 面向对象')
#新建3个对象，3个对象分别把同一个方法各调用一次，方法参数是空，参数在新建对象的时候已经传入了

'''
小结
1、面向过程和面向对象的适用场景
    面向对象：适合属性和方法比较多的情况，优势就可以发挥出来
'''



















