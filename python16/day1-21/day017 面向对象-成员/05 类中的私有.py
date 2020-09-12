#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/2 8:07
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
类中的私有
1、分类
    私有变量
    私有方法

2、写法
    私有变量：变量名字前面加上__
    私有方法：方法名字前面加上__

3、特点
    1、私有变量：
       对象无法访问私有变量
    2、私有方法：
        对象无法访问私有方法

4、如何访问私有变量和私有方法
    1、对象可以通过调用成员方法，间接访问私有变量
       私有变量只能在自己类中访问
    2、对象可以通过调用成员方法，间接调用私有方法
        私有方法只能在自己类中调用

5、适用场景
    1、用的比较少（私有变量和私有方法，在python中）

'''

class Tiger:
    def __init__(self,name,gender,money,house_num):
        self.name = name
        self.gender = gender
        self.__money = money   #私有变量
        self.__house_num = house_num  #私有变量

    def buy(self):  #成员方法可以访问私有变量
        print('我有 %s 元钱' % self.__money)

    def sell_house(self): #成员方法可以调用私有方法
        # __sell_house()  #报错 NameError: name '_Tiger__sell_house' is not defined
        self.__sell_house()  #对象调私有方法
        #注意点：私有方法前面的self必须保留，否则会报错

    def __sell_house(self):  #私有方法
        print('我要出售 %s 套房子' % self.__house_num)

t1 = Tiger('jack',18,10000,5)
print(t1.name)  #jack
# print(t1.__money)  #1 对象无法直接访问私有变量
#AttributeError: 'Tiger' object has no attribute '__money'   报错

#2 对象可以通过调用成员方法，间接访问私有变量
t1.buy() #我有 10000 元钱
print('------------1  对象可以通过调用成员方法，间接访问私有变量')

# t1.__sell_house()  #3 对象无法直接访问私有成员方法
#AttributeError: 'Tiger' object has no attribute '__sell_house'

#4 对象可以通过调用成员方法，间接调用私有方法
t1.sell_house()  #我要出售 5 套房子
print('------------2  对象可以通过调用成员方法，间接调用私有方法')

class Father:
    __mistress = 'panpan'
    def method1(self):
        print(self.__mistress)

class Son(Father):
    pass

# print(Father.__mistress)  #报错
#AttributeError: type object 'Father' has no attribute '__mistress'
f1 = Father()
f1.method1()  #panpan

s1 = Son()
# s1.__mistress  #报错
#AttributeError: 'Son' object has no attribute '__mistress'
s1.method1() #panpan
print('------------3  子类是无法继承父类的私有内容的（包括父类的私有变量和私有方法）')


