#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/15 14:48
#@author:wangtongpei
#@email: cn5036520@163.com

#12题 一行代码获取对象f1中所有成员变量（字典类型）

class Foo:
    def __init__(self):
        self.name = 'jack'
        self.age = 18

f1 = Foo()
setattr(f1,'email','xxx@163.com')
#给对象临时新增一个成员变量（参数1：对象  参数2：变量名字  参数3：变量的值）

print([i for i in dir(f1) if not i.startswith('_')])
#['age', 'email', 'name']

print(f1.__dict__)   #对象名.__dic__
#{'name': 'jack', 'age': 18, 'email': 'xxx@163.com'}
print('------1   一行代码获取对象f1中所有成员变量（字典类型）')


'''
12题小结：
对象调属性__dict__
可以返回一个字典，字典的键值对是对象的成员变量的名称和值

'''

#13题 看代码写结果
class Foo2:
    def __init__(self):
        self.name = 'jack'
        self.age = 18

f2 = Foo2()
setattr(Foo2,'email','xxx@163.com')  #给类添加了一个成员变量

ret1 = getattr(Foo2,'email')
ret2 = getattr(f2,'email')
print(ret1)  #'xxx@163.com'
print(ret2) #'xxx@163.com'
print('-----------------------------13-1')


class Foo3:
    def __init__(self):
        self.name = 'jack'
        self.age = 18

f3 = Foo3()
setattr(f3,'email','xxx@163.com')  #给对象添加了一个成员变量

# ret3 = getattr(Foo3,'email')
ret4 = getattr(f3,'email')
# print(ret3)  #报错
#AttributeError: type object 'Foo3' has no attribute 'email'
print(ret4) #'xxx@163.com'
print('-----------------------------13-2')

'''
13题小结
1、用setattr给类添加一个成员变量
   用getattr从类中可以获取到这个成员变量的值
   用getattr从类的对象也可以获取到这个成员变量的值

2、用setattr给类的对象添加一个成员变量
   用getattr从类中不能获取到这个成员变量的值
      --会报错，#AttributeError: type object 'Foo3' has no attribute 'email'
   用getattr从类的对象可以获取到这个成员变量的值
'''

#14题 什么是可迭代对象？如何将一个对象变成可迭代对象？
'''
定义：
对象中包含__iter__的就是可迭代对象 iterator  iterable
'''
li1 = [1,2]
# print(dir(li1))
bool1 = '__iter__' in dir(li1)
print(bool1) #True

#将列表转成可迭代对象-迭代器
li2 = [1,2]
it1 = li2.__iter__()
print(it1)  #<list_iterator object at 0x0000003BE151F608>
print(type(it1))  #<class 'list_iterator'>

'''
14题小结：
1、可迭代对象的定义
    对象中包含__iter__的就是可迭代对象
    dir(对象)可以列出对象中的所有成员
2、列表转换成可迭代对象
    it1 = li.__iter__()
    #列表调__iter__()方法后，就会返回一个迭代器（迭代器是可迭代对象）
'''
print('-----------------------------14')

#15题 如何让一个对象可以被执行？即后面加()








