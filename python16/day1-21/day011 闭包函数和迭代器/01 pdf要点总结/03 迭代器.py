#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 6:58
#@author:wangtongpei

''''''
'''
1、可迭代类型的对象有哪些？
    str list tuple dict set open() range(3)
2、概念：
    1、可迭代的--iterable
    2、迭代器--iterator
    3、迭代--iteration  主要应用：StopIterration
3、如何判断对象或者类是可迭代类型的--iterable？
    方法1：
    看对象或者类中的方法或者函数是否包含__iter__(),用dir()函数
    方法2：
    isinstance()函数  --导包
4、可迭代类型的（可迭代的）对象如何生成迭代器？
5、for循环的内部原理--单步next while循环
    通过迭代器来实现for循环  --关键点

总结：
可迭代类型的（可迭代的）--iterable：内部有__iter__()方法
迭代器--iterator：内部有__iter__()和__next__()方法
迭代器的特点：
1、节省内存
2、惰性（每调用一次__next__()方法，才往下取一个元素）
3、只能向前，不能退后
'''

# 3、如何判断对象或者类是可迭代类型的--iterable？
#     方法1：
#     看对象或者类中的方法或者函数是否包含__iter__(),用dir()函数
li1 = [1,2,3]
print('__iter__' in dir(li1))  #True #说明列表对象是可迭代类型的（简称-可迭代的）-iterable
#注意 __iter__后面是不带小括号的（方法或者函数名字不带小括号）
#dir（）函数是列出对象或者类中所有的方法或者函数
print('__iter__' in dir(list)) #True #说明列表类型（简称-类）是可迭代类型的-iterable
print('---------------------3-1  判断对象或者类是可迭代类型的--方法1')

#     方法2：
#     isinstance()函数  --导包
from collections import Iterable  #注意：首字母I是大写的
from collections import Iterator  #注意：首字母I是大写的

li2 = [1,2,3]
li2_iter2 = li2.__iter__()  #对象调__iter__()后，就生成了迭代器
print(isinstance(li2,Iterable))  #True  参数1：对象  参数2：类型
#判断对象是否是可迭代类型的（可迭代的）
#li2对象是可迭代类型的（可迭代的）--iterable
print(isinstance(li2,Iterator))  #False
#判断对象是否是迭代器
#li2对象不是迭代器--iterator

print(isinstance(li2_iter2,Iterable)) #True
#迭代器li2_iter2是可迭代类型的（可迭代的）
print(isinstance(li2_iter2,Iterator)) #True
#迭代器li2_iter2是迭代器
print('---------------------3-2 判断对象或者类是可迭代类型的--方法2 isinstance()')

# 4、可迭代类型的（可迭代的）对象如何生成迭代器？
li4 = [1,2,3]
li4_iter4 = li4.__iter__()  #可迭代类型的（可迭代的）对象调__iter__()方法，就生成了迭代器
print(li4_iter4)  #<list_iterator object at 0x00000000026386A0>
print('---------------------4 可迭代类型的（可迭代的）对象如何生成迭代器？')

# 5、for循环的内部原理--通过迭代器来实现for循环
li5 = [1,2,3]
for i in li5:
    print(i)
else:  #前面的for循环正常结束后，才会执行else；如果有break，else是不执行的
    print('循环遍历结束了')
print('---------------------5-1' )

li5 = [1,2,3]
li5_iter5 = li5.__iter__()  #生成迭代器
print(li5_iter5)
print(li5_iter5.__next__())  #1
print(li5_iter5.__next__())  #2
print(li5_iter5.__next__())  #3
# print(li5_iter5.__next__())  #报错  StopIteration
print('---------------------5-2 for循环的内部原理--一步步next' )

li5 = [1,2,3]
li5_iter5 = li5.__iter__()  #生成迭代器
while 1:
    try:
        print(li5_iter5.__next__())
    except StopIteration:
        print('循环遍历结束了2')
        break
print('---------------------5-3 for循环的内部原理--while循环' )













