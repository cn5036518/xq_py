#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1 字符串和列表的不同
s1 = "jack"
print(s1[2])
# s1[2] = "a"  #报错 TypeError: 'str' object does not support item assignment

li1 = ["jack","tom","bob"]
li1[1] = "james"
print(li1) #['jack', 'james', 'bob']

"""
1、字符串的元素-字符是不能修改的
2、列表的元素是可以修改的
"""

#2 元组的第二层的修改
tu1 = ("jack","tom",[],"bob")
# tu1[2] = ["james"]  #报错 TypeError: 'tuple' object does not support item assignment
tu1[2].append("james")
print(tu1)  #('jack', 'tom', ['james'], 'bob')
"""
1、元组的元素是空列表
2、可以往空列表追加元素 append
    但是不可以直接用新列表赋值给空列表
"""










