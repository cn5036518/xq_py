#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/1 7:54
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
类的变量分成2种：
1、成员变量
    概念：在构造方法中的变量，前面带有self
    特点：成员变量是每个对象特有的，即每个对象的成员变量各不相同（类比：有局部的意思）
    作用：可以在类中不同的方法间使用

2、类变量-静态变量
    概念：在类中，构造方法和普通方法之外，定义的变量
    特点：所有该类的对象都共享这个类变量（类比：有全局的意思）
    作用：
        1、调用
            1、类名可以调用       类名.类变量
            2、对象名也可以调用   对象名.类变量
        2、修改
            1、只能是类名才能修改   类名.类变量 = 类变量的新值
            2、对象名不能修改
               特别注意：如果用  对象名.类变量=值，这个是对对象新增了一个属性，和类变量没有任何关系

3、成员变量和类变量的区别
    1、前者是给对象用的
    2、后者是多个对象共享的。最好用类名来访问，这样更规范

总结：
1、类变量用类名来操作（访问和修改），比较规范
   类变量就不要用对象名来操作
2、类变量建议写在类中的构造方法之前，也是规范
'''

class Person:
    country = '中国' #类变量，类和对象都可以访问，但是只有类可以修改类变量
    def __init__(self,name,gender,birthday):
        #存的时候，一般不用年龄，而用生日（年龄每年会变，生日是不变的）
        #变量、属性、字段（成员变量对应数据库中表的字段）
        self.name = name  #成员变量，实例变量
        self.gender = gender
        self.birthday = birthday
    def marry(self,spouse): #成员方法，实例方法
        print('和 %s 结婚' % spouse)

p1 = Person('jack','男','1986-10-25')
print(p1.name) #jack  #打印对象的成员变量

print(Person.country)  #中国  类名访问类变量
print(p1.country)  #中国  对象访问类变量
print('---------------------1 类名或者对象名 访问类变量')

Person.country = '法国'
print(Person.country)  #法国  类名修改类变量
print('---------------------2 类名修改类变量')

p1.country = '英国'   #注意点：对象不会修改类变量，而是给对象新增了一个属性
print(Person.country)  #法国
print(p1.country) #英国
print('---------------------3 对象名不能修改类变量，只会给对象新增一个成员变量')

#4 通过类变量计算类的对象创建了多少次
class Student:
    count = 0  #多个对象共享的，有全局的意思
    def __init__(self):
        Student.count += 1  #类名来调用类变量

s1 = Student()
s2 = Student()
s3 = Student()
print(Student.count) #3
#类名来调用类变量  表示创建了3个学生对象







