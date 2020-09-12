#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/12 9:07
#@author:wangtongpei
#@email: cn5036520@163.com

#第6题，看代码写结果
class Stark_config:
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0,33)
        return self.list_display

class Role_config(Stark_config):
    list_display = [11,22]

s1 = Stark_config()#父类对象1
s2 = Stark_config()#父类对象2

result1 = s1.get_list_display()
print(result1)  #[33]  #类变量，对象1调方法后，类变量变成从[]变成了[33]

result2 = s2.get_list_display()
print(result2) #[33,33] #类变量，对象2调方法后，类变量变成从[33]变成了[33,33]
#注意点：这里的类变量是类中的一个共享内存，不同的对象调方法，都会共同修改这个共享内存
#类变量就相当于类中的全局变量（共享内存属性）
print('------------------------第6题  类变量 2个父类对象')

#第7题，看代码写结果
class Stark_config:
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0,33)
        return self.list_display

class Role_config(Stark_config):
    list_display = [11,22]  #这里 类变量会重写父类的类变量

s1 = Stark_config()  #父类对象
s2 = Role_config()  #子类对象

result1 = s1.get_list_display()
print(result1)  #[33]  #类变量，对象1调方法后，类变量变成从[]变成了[33]

result2 = s2.get_list_display()
print(result2)  #[33,11,22]
print('------------------------第7题  子类的类变量重写父类的类变量')

#第8题，看代码写结果
class Stark_config:
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0,33)
        return self.list_display

class Role_config(Stark_config):
    list_display = [11,22]  #这里 类变量会重写父类的类变量

s1 = Role_config()  #子类对象1
s2 = Role_config()  #子类对象2

result1 = s1.get_list_display()
print(result1)  #[33，11,22]  #类变量，子类对象1调方法后，类变量变成从[]变成了[33，11,22]

result2 = s2.get_list_display()
print(result2)  #[33，33,11,22]
# #类变量，子类对象2调方法后，类变量变成从[33，11,22]变成了[33,33，11,22]
print('------------------------第8题 类变量 2个子类对象')
#注意点：类变量的共享属性，有修改可叠加的效果

class Animal:
    pass

class Cat(Animal):
    pass

class Persian_cat(Cat):  #波斯猫
    pass

print(issubclass(Cat,Animal)) #True
#参数1是子类（孙子类等）  参数2是父类（祖父类）

print(issubclass(Persian_cat,Animal))  #True
print('------------------------第9题 issubclass')

