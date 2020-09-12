#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/7 8:12
#@author:wangtongpei
#@email: cn5036520@163.com

""""""
'''
11. 看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
12. 看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
13. 看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
14. 看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
15. 看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
'''
#11
class Foo:
    a1 = 1
    __a2 = 2

    def __init__(self,num):
        self.num = num
        self.__salary = 1000

    def get_data(self):
        print(self.num + self.a1)

obj1 = Foo(666)
obj2 = Foo(999)
print(obj1.num)  #666
print(obj1.a1)  #1

obj1.num = 18
obj1.a1 = 99
print(obj1.num)  #18
print(obj1.a1)   #99

print(obj2.a1)   #1
print(obj2.num + Foo.a1) #999+1 =1000
print(obj2.num + obj1.a1) #999+99 =1098
print('------------------------11 ')

#12
class Foo:
    hobby = "保健"

    def __init__(self,num):
        self.num = num
        self.__salary = 1000

    def f1(self):
        print(Foo.hobby)

    @staticmethod
    def f2():
        print(Foo.hobby)

    @classmethod
    def f3(cls):
        obj2 = cls(2)  #新建对象
        print(cls.hobby)  #类名.类变量   保健

obj1 = Foo(1)
obj1.f1()  #保健
Foo.f2()  #保健  类名调用静态方法
Foo.f3()  #保健  类名调用类方法
print('------------------------12 ')

#13
class Foo:
# class Foo(object):   #和上面行是等效的，万事万物都是对象
    @classmethod
    def f3(cls):
        print(cls)  #打印当前类
Foo.f3()  #类名.类方法  <class '__main__.Foo'>
print('------------------------13 ')

#14
class Foo:
    @classmethod
    def f3(cls):  #成员方法的self表示的是当前对象
                    #类方法的cls表示的是当前类
        print(cls)
obj = Foo()
obj.f3() #<class '__main__.Foo'>  对象名.类方法
print('------------------------14 ')

#15
class Foo:
    @classmethod
    def f3(cls): #类方法的cls表示的是当前类
        print(cls) #打印类
    def f2(self):
        self.f3()  #<class '__main__.Foo'>  对象调类方法
        Foo.f3()  #<class '__main__.Foo'>   类名调类方法
obj = Foo()
obj.f2()
print('------------------------15 ')
#对象名和类名都可以调类方法，还是推荐类名来调类方法，比较符合规范









































