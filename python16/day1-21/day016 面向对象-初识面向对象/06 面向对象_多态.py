#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/28 7:06
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
多态伪代码：
需求：动物园，饲养员饲养动物
1、一个动物父类
    方法-吃
2、2个子类（猴子和老虎）
    方法-吃
3、一个饲养员类
    方法-喂动物
    注意点：方法的形参是动物

4、新建一个饲养员对象
5、新建2个动物对象
6、饲养员对象调方法，传入动物对象--多态
'''

#1 定义4个类，1个动物父类，2个子类，1个饲养员类  动物园里
class Animal:#动物
    def eat(self):
        print('动物吃东西')

class Monkey(Animal):
    def eat(self):
        print('猴子吃香蕉')

class Tiger(Animal):
    def eat(self):
        print('老虎吃肉')

class Stockman:  #饲养员  动物园  关键点
    def feeding(self,animal):  #多态，传入动物对象，不管是什么具体的动物，都统一当做动物对象来看
        # 形参代指动物对象  多态是核心逻辑-可扩展性超强，也是面向对象的核心
        # 注意点1：这里不需要把animal-具体成动物对象
        animal.eat()

#2 新建2个动物具体对象（猴子和老虎），新建饲养员对象
monkey1 = Monkey()  #新建猴子对象--一只猴子
tiger1 = Tiger()   #新建老虎对象--一只老虎
stockman1 = Stockman()  #新建饲养员--一个饲养员

#3 饲养员对象调方法，参数数具体的动物对象
stockman1.feeding(monkey1)  #实际参数是具体的动物对象
# 猴子吃香蕉
stockman1.feeding(tiger1)
# 老虎吃肉
print('------------------------ 多态1 动物园  饲养员饲养动物')

'''
多态例子2
西游记，孙悟空打妖精
多态思想：不管是白骨精，蜘蛛精（具体的妖精），孙悟空都当妖精（统称）来打

伪代码：
1、定义4个类
    1个妖精父类
        方法：干坏事
    2个子类
        方法：干坏事
    1个孙悟空类
        方法：打妖精  形参是妖精统称   --多态
2、新建3个对象
    1、2个妖精对象（白骨精、蜘蛛精）
    2、1个悟空对象
3、悟空对象调方法-大妖精
   实参是具体的妖精对象（白骨精、蜘蛛精）  --多态
'''

#1 定义4个类
class Demon:   #新建妖精类
    def do_evil(self):
        print('妖精害人')

class White_bone_demon(Demon):
    pass      #这里 下面2行注释掉都可以的，子类会继承父类的方法
    def do_evil(self):
        print('白骨精吃人')

class Spider_goblin(Demon):
    def do_evil(self):
        print('蜘蛛精干坏事')

class Sunwukong:
    def do_good(self,demon):  #多态，不管传入的对象是白骨精还是蜘蛛精-具体的，都统一当做妖精-统称 来对待 扩展性极强
        #比如：当新定义了一个新妖精-蝎子精类，孙悟空这个类和类中的方法，不会有任何修改--核心逻辑不会有任何变动
        #注意点：在定义类的时候，白骨精、蜘蛛精都继承妖精这个父类
        demon.do_evil()

#2 新建3个对象，白骨精、蜘蛛精、孙悟空
white1 = White_bone_demon()
spider1 = Spider_goblin()
sunwukong1 = Sunwukong()

#3 孙悟空对象调方法-打妖精 实参是具体的妖精对象
sunwukong1.do_good(white1)  #白骨精吃人
sunwukong1.do_good(spider1)  #蜘蛛精干坏事
print('------------------------ 多态2 西游记  孙悟空打妖精')

#1 定义4个类
class Demon:   #新建妖精类
    def do_evil(self):
        print('妖精害人')

class White_bone_demon(Demon):
    pass      #这里 下面2行注释掉都可以的，子类会继承父类的方法
    def do_evil(self):
        print('白骨精吃人')

class Spider_goblin(Demon):
    def do_evil(self):
        print('蜘蛛精干坏事')

class Scorpion_demon(Demon):  #新增一个--扩展
    def do_evil(self):
        print('蝎子精做坏事')

class Sunwukong:
    def do_good(self,demon):  #多态，不管传入的对象是白骨精还是蜘蛛精-具体的，都统一当做妖精-统称 来对待 扩展性极强
        #比如：当新定义了一个新妖精-蝎子精类，孙悟空这个类和类中的方法，不会有任何修改--核心逻辑不会有任何变动
        #注意点：在定义类的时候，白骨精、蜘蛛精都继承妖精这个父类
        demon.do_evil()
        #注意点2： 这里的方法名，子类方法名和父类方法名相同，就会覆盖；子类方法名和父类方法名不同，就会继承父类方法

#2 新建3个对象，白骨精、蜘蛛精、孙悟空
white1 = White_bone_demon()
spider1 = Spider_goblin()
sunwukong1 = Sunwukong()
scorpion1 = Scorpion_demon()

#3 孙悟空对象调方法-打妖精 实参是具体的妖精对象
sunwukong1.do_good(white1)  #白骨精吃人
sunwukong1.do_good(spider1)  #蜘蛛精干坏事
sunwukong1.do_good(scorpion1)  #蝎子精做坏事
print('------------------------ 多态3 西游记2  孙悟空打妖精 增加一个妖精-蝎子精')

#1 定义4个类
class Demon:   #新建妖精类
    def do_evil(self):
        print('妖精害人')

class White_bone_demon(Demon):
    pass      #这里 下面2行注释掉都可以的，子类会继承父类的方法
    # def do_evil(self):  #
    #     #子类会继承父类方法
    #     #1 子类的方法和父类的方法名字相同，会覆盖父类的方法
    #     #2 子类的方法和父类的方法名字不同，会继承父类的方法
    #     print('白骨精吃人')

class Spider_goblin(Demon):
    def do_evil(self):   #子类的方法会覆盖父类的方法
        print('蜘蛛精干坏事')

class Scorpion_demon(Demon):  #新增一个--扩展
    def do_evil(self):
        print('蝎子精做坏事')

class Sunwukong:
    def do_good(self,demon):  #多态，不管传入的对象是白骨精还是蜘蛛精-具体的，都统一当做妖精-统称 来对待 扩展性极强
        #比如：当新定义了一个新妖精-蝎子精类，孙悟空这个类和类中的方法，不会有任何修改--核心逻辑不会有任何变动
        #注意点：在定义类的时候，白骨精、蜘蛛精都继承妖精这个父类
        demon.do_evil()

#2 新建3个对象，白骨精、蜘蛛精、孙悟空
white1 = White_bone_demon()
spider1 = Spider_goblin()
sunwukong1 = Sunwukong()
scorpion1 = Scorpion_demon()

#3 孙悟空对象调方法-打妖精 实参是具体的妖精对象
sunwukong1.do_good(white1)  #妖精害人   这里继承的父类方法  注意点
sunwukong1.do_good(spider1)  #蜘蛛精干坏事
sunwukong1.do_good(scorpion1)  #蝎子精做坏事
print('------------------------ 多态4 西游记3  孙悟空打妖精 子类继承父类方法')

'''
子类继承父类方法
1 子类的方法和父类的方法名字相同，会覆盖父类的方法
2 子类的方法和父类的方法名字不同，会继承父类的方法
    比如：父类有1个方法-method1，子类有1个方法-method2
          那么子类实际上有2个方法，分别是method1和method2
'''







