#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/25 6:57
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
7、背写你了解的所有特殊方法并附上示例
特殊方法：__双下划线开头的方法

__init__()

__enter__()  with

__exit__()  with

__new__()

__str__()

'''

#1 构造方法，初始化方法
class Foo:
    def __init__(self,num):
        self.num = num

f1 = Foo(15)
print(Foo) #<class '__main__.Foo'>
print(f1)  #<__main__.Foo object at 0x000000351887D2C8>
print(f1.num)  #15

#2  __str__()方法
class Foo2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        # return self.name,self.age  #报错 #TypeError: __str__ returned non-string (type tuple)
        return '%s %s' % (self.name,self.age)  #jack 19

f2 = Foo2('jack',19)
print(f2)  #jack 19
'''
__str__()方法的作用：
1、保持默认的__str__()方法，打印对象的时候，输出对象的内存地址
   <__main__.Foo object at 0x000000A6CE88DAC8>

2、重写__str__()方法后，再次打印对象的时候，就可以自定义输出对象（比如，人的对象，打印人的姓名和年龄）
    return '%s %s' % (self.name,self.age)  #jack 19
'''
print('--------------------------------------2  __str__()方法')

#3  __new__()方法
class Foo3:
    def __init__(self,name,age):
        print('2开始对象的初始化')
        self.name = name
        self.age = age
        print('3对象的初始化完成')

    # def __new__(cls):   #报错，TypeError: __new__() takes 1 positional argument but 3 were given
    def __new__(cls,*args,**kwargs):  #这里不能是self，因为对象还没有初始化出来，还不存在
        print('1准备开辟内存空间')
        return object.__new__(cls)  #这里的cls表示类名本身  关键点在这里
        # print('2开辟内存空间完成，内存空间是空的')

f3 = Foo3('bob',18)

'''
创建对象的步骤
1、加载类
2、开辟内存空间：通过__new__()
    此时，开辟出来的内存空间是空的
3、对象的初始化：系统自动调用构造方法，通过__init__()
4、使用对象调方法等
'''
print('-----------------------------------------3  __new__()方法')

#4 with的原理  __enter__() __exit__()   打开文件和对象
class Foo4:
    def __enter__(self):
        print('开始enter')
        return '周润发'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('开始exit')

f4 = Foo4()

with f4 as temp:
    print(temp)  #周润发  接收的是__enter__()方法的返回值

#with在打开文件中的例子
# with open('001.py') as f41:  #内部原理是，自动进行了写入刷新和关闭文件对象
#     print(f41.read())
print('-----------------------------------------4  __enter__() __exit__()方法 with')

class Foo5(object):
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print('我是__call__方法')

f5 = Foo5() #新建对象 自动调构造方法
f5()  #对象后面加小括号，是调__call__()方法，是python特有的(其他编程语言可能没有)
#我是__call__方法
print('-----------------------------------------5  __call__()方法')

class Foo6:
    def __init__(self):
        pass
    def __getitem__(self, item):
        print('我是__getitem__方法',item)
        return item
f6 = Foo6()
ret1 = f6['name']  #对象和类都是可哈希的，不可变的，可以作为字典的key
print(ret1)  #name
#我是__getitem__方法 name
print('-----------------------------------------6  __getitem__()方法')

'''
小结：
对象[key]会自动执行__getitem__方法
所以说，对象其实有类似字典的特性

扩展：
1、输入一个字符串，然后让类的对象原封不动的返回这个字符串
   除了用input外，还可以用  对象[key]会自动执行__getitem__方法的方式来实现
'''

class Foo7:
    def __init__(self):
        pass
    def __setitem__(self, key, value):
        print('我是__setitem__方法',key,value)

f7 = Foo7()
f7['name'] = 'jack'
# 我是__setitem__方法 name jack
print('-----------------------------------------7  __setitem__()方法')

'''
小结：
对象[key]=value 会自动执行__setitem__方法
'''

class Foo8:
    def __init__(self):
        pass
    def __setitem__(self, key, value):
        self.key = key
        self.value = value
        print('添加',key,value)  #name tom

    def __getitem__(self, item):
        print('获取',item)

    def __delitem__(self, key):
        print('删除',key)

    def __str__(self):
        return '%s %s' % (self.key,self.value)
        # return "{'%s':'%s'}" % (self.key,self.value)

f8 = Foo8()
f8['name']='tom'  #添加键值对
f8['name']  #获取value
del f8['name']  #删除键
print(f8)  #name tom
print('-----------------------------------------8  __delitem__()方法')












