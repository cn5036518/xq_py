#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/25 15:18

''''''
'''
需求1：
1、计算一个字符串中，每个字符出现的次数
   展示要求：字符是key,字符次数是value，组成的字典

思路：
方法1、算法来计算-for循环
方法2、内置模块
'''

#方法1
s1 = 'bob'
dic1 = {}
for i in s1:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 0
print(dic1)  #{'b': 1, 'o': 0}

#方法2
s1 = 'bob'
dic1 = {}
for i in s1:
    dic1[i] =dic1.get(i,0)+1
print(dic1)  #{'b': 2, 'o': 1}

#方法3  内置模块
from collections import Counter
s1 = 'bob'
print(Counter(s1))  #Counter({'b': 2, 'o': 1}) #这个结果可以当字典来使用
print(dict(Counter(s1)))  #{'b': 2, 'o': 1}
















