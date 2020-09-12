#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/5 17:36
#@author:wangtongpei

''''''
'''
map函数
1、写法
    map(func,iterable)
    参数1：自定义函数或者匿名函数
    参数2：Iterable
    返回值：Iterator-迭代器
2、原理
    将iterable中的元素，作为参数依次传递入自定义函数，计算返回值，返回迭代器-iterator
'''

#1 计算列表中的每个元素平方，返回新列表
li1 = [1,2,3]
li2 = map(lambda x:x*x,li1)
print(li2) #迭代器
print(list(li2))  #[1, 4, 9]  将迭代器转换成列表
print('------------------------1 map')

#2 计算两个列表相同位置的元素之后
li3 = [1,3,5]
li4 = [2,4,6]
li5 = map(lambda x,y:x+y,li3,li4)
print(li5)
print(list(li5)) #[3, 7, 11]
print('------------------------2 map')












