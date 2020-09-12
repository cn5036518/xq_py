#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一、昨日回顾
#1 分割拆分（字符串拆分成列表）
s1 = """ha
djs
hah"""

s2 = s1.split() #默认是空白（空格、tab、回车换行\r\n）作为分隔符,返回的是列表
print(s2) #['ha', 'djs', 'hah']

#2 连接（列表的元素连接成字符串）
li1 = ["jack","tom","bob"]
s1 = "_".join(li1)  #这里 "_"是连接符  join后的参数是可迭代对象-例如列表
print(s1)  #jack_tom_bob   #返回的是字符串

"""
#3 while循环和for循环的区别
# while循环特有的特点：可以实现死循环-无限循环，for循环实现不了
# 2 while循环可以拿到元素的索引号，而for循环直接拿到的就是元素，而无法拿到元素的索引号
"""








