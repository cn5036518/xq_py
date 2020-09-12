#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/7 6:56
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
6. 面向对象的方法中那个无需传参数？
    静态方法无需传参数
    成员方法self
    类方法cls

7. 面向对象中公有和私有成员，在编写和调用时有哪些不同？
    1、编写上
        后者名字前面需要加上__,前者不需要
    2、调用上
        后者不能通过对象直接访问
        后者可以通过对象调用公有成员方法的形式，访问私有变量或者私有方法
        （把私有变量或者私有方法写在公有成员方法中）

        前者可以通过对象直接访问

8. 看代码写结果：【禁止运行】
9.  看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
10. 看代码写每个打印结果：【禁⽌运行，如果报错可认为程序会继续向后执行】

'''
#8
class Foo(object):
    a1 = 11   #类变量
    a2 = 12
    print(a1)  #11
    print(a2)  #12
    def __init__(self):
        self.a1 = 1
        print(self.a1)  #1
    print(a1) #11
    print(a2)  #12
obj = Foo() #新建对象，自动调构造方法
print(obj.a1) #1
print(obj.a2) #12
print('------------------------8')

#9
class Foo:
    a1 = 11
    def __init__(self,num):
        self.a2 = num
obj = Foo(999)
print(obj.a2)  #999  成员变量
print(obj.a1)  #11  类变量

print(Foo.a1)  #11 类变量
# print(Foo.a2)  #报错  类名不能调用成员变量
#AttributeError: type object 'Foo' has no attribute 'a2'
print('------------------------9')

class Foo:
    a1 = 1
    __a2 = 2  #私有类变量

    def __init__(self,num):
        self.num = num
        self.__salary = 1000  #私有成员变量

    def get_data(self):
        print(self.num+self.a1)

obj = Foo(666)
print(obj.num)  #666
print(obj.a1)  #1
# print(obj.__salary)  #报错  对象不能直接调用私有成员变量
#AttributeError: 'Foo' object has no attribute '__salary'
# print(obj.__a2)  #报错   对象不能直接调用私有类变量
#AttributeError: 'Foo' object has no attribute '__a2'
print(Foo.a1)  #1
# print(Foo.__a2)  #报错   类名不能调用私有类变量
#AttributeError: type object 'Foo' has no attribute '__a2'
print('------------------------10')












