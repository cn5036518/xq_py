#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 8题
class Foo(object):
    a1 = 11
    a2 = 12

    def __init__(self):
        self.a1 = 1

obj = Foo()
print(obj.a1)   #1
print(obj.a2)   #12
print(Foo.a1)   #11
print(Foo.a2)   #12

# # 9题
# class Foo(object):
#     a1 = 11
#
#     def __init__(self, num):
#         self.a2 = num
#
# obj = Foo(999)
# print(obj.a2)       #999
# print(obj.a1)       #11
# print(Foo.a2)       #报错:AttributeError: type object 'Foo' has no attribute 'a2'
# print(Foo.a1)       #11

# # 10题
# class Foo(object):
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000
#
#     def get_data(self):
#         print(self.num+self.al)
#
# obj = Foo(666)
# print(obj.num)      #666
# print(obj.a1)       #1
# print(obj.__salary) #报错：AttributeError: 'Foo' object has no attribute '__salary'
# print(obj.__a2)     #报错：AttributeError: 'Foo' object has no attribute '__a2'
# print(Foo.a1)       #1
# print(Foo.__a2)     #报错：AttributeError: type object 'Foo' has no attribute '__a2'

# # 11题
# class Foo(object):
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000
#
#     def get_data(self):
#         print(self.num+self.a1)
#
# obj1 = Foo(666)
# obj2 = Foo(999)
# print(obj1.num)     #666
# print(obj1.a1)      #1
#
# obj1.num = 18
# obj1.a1 = 99
#
# print(obj1.num)     #18
# print(obj1.a1)      #99
#
# print(obj2.a1)      #1
# print(obj2.num + Foo.a1)    #1000
# print(obj2.num + obj1.a1)   #1098

# 12题
class Foo(object):
    hobby = "大保健"
    def __init__(self, num):
        self.num = num
        self.__salary = 1000

    # f1实例方法
    def f1(self):
        print(Foo.hobby)

    # f2静态方法
    @staticmethod
    def f2():
        print(Foo.hobby)

    # f3类方法
    @classmethod
    def f3(cls):
        print(cls.hobby)

f = Foo(555)
f.f1()
Foo.f2()
Foo.f3()

# 13题\14题\15题
class Foo(object):
    @classmethod
    def f3(cls):
        print(cls)

    def f2(self):
        self.f3()
        Foo.f3()

Foo.f3()        #<class '__main__.Foo'>

obj = Foo()
obj.f3()          #<class '__main__.Foo'>

obj.f2()        #<class '__main__.Foo'>

# 17. 请编写一个私有的静态⽅法，并通过代码证明私有⽅法不能再外部⽅法但可以在内部访问。
class Dog:
    @staticmethod
    def __sleep():
        print("狗睡觉")

    def sleep(self):
        self.__sleep()

Dog().sleep()

# 18. 现有500W条数据.请使用面向对象的思维来完成这500W条数据的分页工作(升级题)
lst = ["python第%s期" % i for i in range(1,76)]
class Page:
    def __init__(self, lst, pagesize):
        self.lst = lst      #总页数
        self.pagesize = pagesize    #每页条数

    def start(self):
        '''
        返回第一页的内容
        '''
        data = lst[0:self.pagesize]
        for d in data:
            print(d)


    def end(self):
        '''
        返回最后一页的内容
        '''
        #计算出最后一页数据的条数
        size = len(lst)-self.pagesize*(self.lst-1)
        data = lst[len(lst)-size:]
        for d in data:
            print(d)

    def index(self):
        '''
        返回指定页的内容
        '''
        ye = int(input("请输入你要查询的数据的页数："))
        if ye == 1:
            self.start()
        elif ye == self.lst:
            self.end()
        else:
            start = (ye-1) * self.pagesize
            end = start + self.pagesize
            data = lst[start:end]
            for d in data:
                print(d)

p = Page(4, 5)
# p.start()
# p.end()
p.index()
# 19. 在昨天最后一题的基础上.把数据写入到文件中.并且注册的时候需要到文件中判断是否重
# 复.如果重复提示不能注册.(升级题)