#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/8 6:09
#@author:wangtongpei
#@email: cn5036520@163.com

""""""
'''
16. 看代码写结果：【禁⽌运行，如果报错可认为程序会继续向后执行】
17.请编在写一个私有的静态方法，并通过代码证明私有方法不能再外部方法但可以在内部访问。
18.现有500W条数据.请使用面向对象的思维来完成这500W条数据的分页工作(升级题)
19.在昨天最后一题的基础上.把数据写入到文件中.并且注册的时候需要到文件中判断是否重
复.如果重复提示不能注册.(升级题
'''

#16
class Base:
    @classmethod
    def f3(cls):
        print(cls)  #4这个场景下，cls指的是子类Foo

    def f1(self):
        print('base.f1')
        self.f3()  #3这个场景下，self指的是obj（子类的对象）
class Foo(Base):
    def f2(self):  #1 这里的self指的是obj
        print('foo.f2')  #foo.f2
        self.f1()  #base.f1  继承父类的成员方法  #2 self指的是obj
obj = Foo()
obj.f2()
# foo.f2
# base.f1
# <class '__main__.Foo'>   #注意点：这里的cls指的是子类Foo，而不是父类Base
print('------------------------16 ')

# 17.请编在写一个私有的静态方法，并通过代码证明私有方法不能在外部方法但可以在内部访问。
class Foo:
    @staticmethod
    def __method1(a,b):
        print(a+b)
        return a+b
    def method2(self):
        self.__method1(1,2)  #类中，成员方法中，对象调私有的静态方法是可以的

    def method3(self):
        Foo.__method1(2, 2)  #类中，成员方法中，类名调私有的静态方法是可以的

f1 = Foo()
# f1.__method1(2,3) #报错 对象不能直接调私有的静态方法
#AttributeError: 'Foo' object has no attribute '__method1'
# Foo.__method1(2,3) #报错  类名不能直接调私有的静态方法
#AttributeError: type object 'Foo' has no attribute '__method1'

f1.method2()  #3  对象可以通过调成员方法，来调私有的静态方法（静态方法的调用写在成员方法中）
Foo.method2(Foo) #3  和上面行是等效的

f1.method3()  #4
Foo.method3(Foo) #4  和上面行是等效的
print('------------------------17 ')

# 18.现有50条数据.请使用面向对象的思维来完成这50条数据的分页工作(升级题)
class Page:
    def __init__(self,lst,pagesize):
        self.lst = lst
        self.pagesize = pagesize
    def start(self):
        '''
        返回第一页的内容
        '''
    def end(self):
        '''
        返回最后一页的内容
        '''
    def index(self):
        '''
        返回指定页的内容
        '''
        page = input('请输入你要查询的数据的页数：')

'''
伪代码思路：
第一步
1、一共是6条数据，每页2条，分成3页
2、输入页数1，打印1-2(索引号和值都是1,2)
3、输入页数3，打印5-6

第二步
1、一共是5条数据，每页2条，分成3页
2、输入页数1，打印1-2(索引号和值都是1,2)
3、输入页数3，打印5

'''

class Page:
    def __init__(self,lst,pagesize):
        self.lst = lst
        self.pagesize = pagesize
    def start(self):
        '''
        返回第一页的内容
        '''
        # total_page = len(self.lst)/self.pagesize
        print(self.lst[:self.pagesize])
        return self.lst[:self.pagesize]

    def end(self):
        '''
        返回最后一页的内容
        '''
        total_page = len(self.lst) / self.pagesize
        # print(total_page)
        if type(total_page) == int:
            print(self.lst[-self.pagesize:])
            return self.lst[-self.pagesize:]
        else:
            result, remainder = divmod(len(self.lst),self.pagesize)
            # print(result)  2 商是2
            # print(remainder) 1 余数是1
            print(self.lst[-remainder:])  #[5]
            return self.lst[-remainder:]

    def specified_page(self,n):
        print(self.lst[self.pagesize*(n-1):self.pagesize*n])
        return self.lst[self.pagesize*(n-1):self.pagesize*n]

    def index(self):
        '''
        返回指定页的内容
        '''
        while 1:
            page = input('请输入你要查询的数据的页数,输入q退出：')
            if page.upper() == 'Q':
                print('退出了')
                break
            elif page == '1':
                self.start()
            elif page == '-1':
                self.end()
            elif page.isdigit() == False:
                print('只能输入数字，请输入数字')
            elif int(page) < (len(self.lst)/self.pagesize)+1 :
                # 注意这里是小于号 不能是小于等于   --边界值
                self.specified_page(int(page))
            # elif int(page) > (len(self.lst) / self.pagesize) + 1 :
            #     print('页码超出范围了')
            else:
                print('页码超出范围了')

# li1 = [1,2,3,4,5,6]
# li1 = [1,2,3,4,5]
li1 = [i for i in range(101)]
p1 = Page(li1,2)  #一共是5条记录，每页2条记录
p1.index()
print('------------------------18 ')



















