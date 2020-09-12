#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/28 8:06
#@author:wangtongpei

#dict() 函数  创建一个字典
# 方式1：关键字
dic1 = dict(name= 'jack',age = 18) #注意点：这里name和age是关键字，不能加双引号
print(dic1)  #{'name': 'jack', 'age': 18}

# 方式2：Iterable
# 方式3：映射函数

#创建字典方式2-多个键值对一次性定义字典
dic2 = {'name':'jack','age':19}
print(dic2)  #{'name': 'jack', 'age': 19}

#创建字典方式3--单个键值对，多次添加，给字典添加一个键值对
# 比如：往空字典中依次添加键值对
dic3 = {}
dic3['name'] = 'jack'
dic3['age'] = 20
print(dic3)  #{'name': 'jack', 'age': 20}
print('----------------1 dict() 函数')

s1 = 'bob'
s2 = 'alexab'

set1 = set(s1)  #把字符串转换成集合
print(set1)  #{'b', 'o'}  #去重和无序

set2 = set(s2)
print(set2)  #{'b', 'x', 'l', 'e', 'a'}

print(set1 & set2)   #{'b'}  求交集 （并且，两个集合都有的）
print(set1 | set2)  #{'x', 'o', 'e', 'a', 'l', 'b'}  求并集（合集）
print(set2 - set1)  #{'l', 'e', 'a', 'x'}  求差集
print('----------------2 set() 函数')

s1 = 'bob'
print(frozenset(s1))  #创建一个不可变的集合（不能添加或者删除元素）
#类比：set和frozenset list和tuple
#frozenset({'b', 'o'})
print('----------------3 frozenset() 函数')













