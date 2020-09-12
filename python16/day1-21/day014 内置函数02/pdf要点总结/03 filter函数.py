#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/5 17:11
#@author:wangtongpei

''''''
'''
filter函数
1、写法
    filter(func,iterable)
2、原理
    将iterable中的每一个元素，作为参数传递给自定义函数，返回值是True或者False，保留True
'''

#1筛选偶数
li1 = [1,2,3,4,5,6]
li2 = filter(lambda x:x%2==0,li1)
print(li2) #迭代器
print(list(li2))  #[2, 4, 6] 将迭代器转换成列表
print('-------------------------1 filter')

#2筛选学生信息，将大于18岁的筛选出来
li2 = [{'name': 'jack', 'age': 18},
             {'name': 'tom', 'age': 15},
             {'name': 'bob', 'age': 19}]
li3 = filter(lambda dic:dic['age']>18,li2)
print(li3)  #迭代器
print(list(li3)) #[{'name': 'bob', 'age': 19}]  将迭代器转换成列表
print('-------------------------2 filter')
























