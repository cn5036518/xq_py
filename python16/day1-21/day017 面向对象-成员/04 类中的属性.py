#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/2 7:02
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
类中的属性
1、概念
    用一个方法的返回值来表示属性
2、写法
    1、 @property
    2、方法的参数只有一个self
    3、方法必须有返回值 return
3、调用
    1、对象名.属性名
        注意：属性名就是方法名，属性后面不能加小括号
4、适用场景
    1、人的年龄就不适合当做成员变量来存储，而应该把生日作为成员变量-字段
    2、但是年龄是人的一个属性，就可以通过生日来换算出来
    3、人的年龄是一个属性，如果通过成员方法-动作来计算也可以，但是用属性-名词更好一些
5、注意点
    调成员方法和调属性的区别
    1、前者  对象名.成员方法名()  方法名后面有小括号
    2、后者  对象名.属性    属性后面没有小括号
'''
import datetime
class Person:
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday

    @property  #表示属性
    def age(self):
        # return 今年-birthday
        this_year = int(str(datetime.datetime.now())[:4])
        print(this_year)  #2019   #获取今年的年份
        year_of_birth = int(self.birthday[:4])
        print(year_of_birth)  #1983  #获取生日中的出生年份
        return  (this_year-year_of_birth)

    def age2(self):  #注意点  这里的成员方法名字不能和前面的属性名字相同
        # return 今年-birthday
        this_year = int(str(datetime.datetime.now())[:4])
        # print(this_year)  # 2019   #获取今年的年份
        year_of_birth = int(self.birthday[:4])
        # print(year_of_birth)  # 1983  #获取生日中的出生年份
        return (this_year - year_of_birth)

p1 = Person('jack','1983-10-25')
print(p1.age)  #36
#注意点：这里的age是属性，所以后面没有小括号

print(p1.age2())  #36
#这里是对象调方法得到年龄的，age2后面加了小括号
#注意点  这里的成员方法名字不能和前面的属性名字相同









