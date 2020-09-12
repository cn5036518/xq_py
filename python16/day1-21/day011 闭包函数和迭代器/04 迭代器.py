#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/5 15:43
#@author:wangtongpei

#可迭代的对象：str、list、tuple、dict、set、open()、range()
''''''
'''
1、对象中含有__iter__ 就是可迭代对象


'''
li1 = [1,2,3]
print(dir(li1))  #dir()函数可输出当前对象（比如：列表、字符串）的内置方法
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__',
# '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
a1 = '__iter__' in dir(li1)  #判断li1这个对象中是否包含__iter__
print(a1)  #True

a2 = '__iter__' in dir(range(3)) #判断range(3)这个对象中是否包含__iter__
print(a2)  #True

a3 = '__iter__' in dir(open('03 闭包函数.py',mode='r',encoding='utf-8'))
#判断open()这个对象中是否包含__iter__
print(a3)  #True
print('--------------------1')

li2 = [2,3,4]
for i in li2:
    print(i)
else:  #for循环正常运行结束后，会执行else；如果中间有break，就不会执行else
    print('结束了')
print('--------------------2')


li3 = [2,3,4]
it3 = li3.__iter__()  #迭代器对象--iterator
print(dir(it3))
print('__next__' in  dir(it3))  #True
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__',
#  '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
# '__str__', '__subclasshook__']
print(it3.__next__())  #2
print(it3.__next__())  #3
print(it3.__next__())  #4
# it3.__next__()
print('--------------------2-2')

li4 = [2,3,4]
it4 = li4.__iter__()  #迭代器对象--iterator
print(type(it4))  #<class 'list_iterator'>
while 1:
    try:
        print(it4.__next__())  #__next__()是迭代器对象的方法
    except StopIteration:
        print('结束了')
        break
print('--------------------3')
'''
小结：
1、for循环的内部原理，是调用了迭代器（即for循环的底层算法用的是迭代器）
2、迭代器对象是如何产生的
    it1 = li1.__iter__()  #这里的it1就是迭代器对象--iterator
3、迭代器对象中有__next__()方法，每调一次整个方法，就输出一个元素
4、迭代器给所有的数据类型提供了一种统一的遍历方式（可迭代协议）

迭代器--iterator
可迭代的--iterable
可迭代对象-列表等内置方法--__iter__()
迭代器--内置方法--__next__()

迭代器特点：
1、节省内存
2、惰性机制（只有调用依次__next__()才取值一次）
3、只能向前，不能后退
'''

li22 = [3,4,5]
for i in li22:
    print(i)
else:
    print("结束了")
print('--------------------4-1 for循环遍历列表li22')

li23 = [3,4,5]
it23 = li23.__iter__() #列表对象调方法__iter__()生成-迭代器对象
print(it23)  #<list_iterator object at 0x0000000002579940>
print(it23.__next__())  #3
print(it23.__next__())  #4
print(it23.__next__())  #5
# print(it23.__next__())  #StopIteration
print('--------------------4-2 迭代器单个next')

li24 = [3,4,5]
it24 = li24.__iter__()  #列表对象调方法__iter__()生成-迭代器对象--iterator
while 1:
    try:
        print(it24.__next__())
    except StopIteration:
        print('结束了')
        break #跳出整个循环
print('--------------------4-3 迭代器-while')







