#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/20 6:37
#@author:wangtongpei
#@email: cn5036520@163.com

#1 判断对象是否是iterable
li1 = [1,2]
print('__iter__' in dir(li1))  #True
print('--------------------1 判断对象是否是iterable')

#2 把对象转换成iterator   iter() __iter__()
li2 = [2,3]
it2 = li2.__iter__()
# it2 = iter(li2)   #和上面行等效
print(it2)  #<list_iterator object at 0x0000009C633AB2C8>
print('--------------------2 把对象转换成iterator')

#3 惰性机制，一步一步next取值
li2 = [2,3]
it2 = li2.__iter__()
ret1 = it2.__next__()
print(ret1)  #2
ret2 = it2.__next__()
print(ret2)  #
# it2.__next__()  #报错 StopIteration
print('--------------------3 惰性机制，一步一步next取值')

#4 用迭代器写for循环的实现过程
li4 = [3,4]
it4 = iter(li4)
while 1:
    try:
        ret4 = next(it4)
        print(ret4)
    except StopIteration as e:
        print(e)   #这里e是一个空行
        print('没有值可以取了',e)
        # print('没有值可以取了%s，哈哈' % e)
        break  #跳出整个循环
print('--------------------4 惰性机制，用迭代器写for循环的实现过程')






