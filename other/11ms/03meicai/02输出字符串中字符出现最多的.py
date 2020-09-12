#!/usr/bin/env python
#-*- coding:utf-8 -*-

#题目：计算字符串"abbc"中,哪个字符出现的次数最多
s1 = "abbc"
#方法1   字符串的内置方法count
print(s1.count("b")) #输出字符串中单个指定字符出现的次数
for i in s1: #输出字符串中每个字符出现的次数
    print(i,s1.count(i))
print("----------1 count")

#方法2  #字典的方式  推荐1
s1 = "abbc"
dic1 = {}  #空字典  （类似空列表）
for i in s1:
    dic1[i] = s1.count(i)  #（往空字典中添加键值对，就类似往空列表追加append-元素）
    #添加的键值对中，key是i（字符串的元素-字符），value是s1.count(i)(字符串的元素-字符出现的次数)  #关键点1
print(dic1) #{'c': 1, 'b': 2, 'a': 1}

s1 = "abbc"
li1 = []
for i in s1:
    li1.append(i)  #把字符串的元素-字符 依次添加到空列表
print(li1) #['a', 'b', 'b', 'c']
print("----------2 字典的方式")

#方法3 collections模块下的Counter方法
from collections import Counter
s1 = "abbc"
print(Counter(s1))  #Counter({'b': 2, 'c': 1, 'a': 1})

li1 = ["a","b","b","c"]
print(Counter(li1)) #Counter({'b': 2, 'a': 1, 'c': 1})

dic1 = {'a': 1, 'b': 2}
print(Counter(dic1)) #Counter({'b': 2, 'a': 1})
print("------------3 collections模块下的Counter方法 ")
"""
collections模块下的Counter方法
1、参数是-字符串，输出了每个字符出现的次数，且按照出现次数进行从大到小排序
2、参数是-列表，输出了列表中每个元素出现的次数，且按照出现次数进行从大到小排序
3、参数是-字典，按照value的大小进行从大到小排序
"""

#方法4  推荐2   算法（s1.count("a")的底层实现）
s1 = "abbc"
dic1 = {}   #空字典（空字典添加）（空列表追加）（空字符串累计拼接）（空数字0累加）
for i in s1: #1遍历字符串的每个元素-字符
    if i in dic1: # 如果字符i在字典中，value的值加1，类似count+=1
        dic1[i] = dic1[i] + 1
    else: #2 如果字符i不在字典中，给与初始value=1
        dic1[i] = 1
print(dic1) #{'b': 2, 'c': 1, 'a': 1}
print("------------4-1 ")

s1 = "abbc"
dic1 = {}   #空字典（空字典添加）（空列表追加）（空字符串累计拼接）（空数字0累加）
for i in s1: #1 遍历循环字符串的每个元素-字符
    if i not in dic1: #2 如果字符i不在字典中，则给key=i,赋予初始value=1
        dic1[i] = 1 #i第一次出现，次数就是1
    else: # 如果字符i在字典中，则给key=i,value自增1
        dic1[i] += 1 #i后面没出现一次，次数就自增1
print(dic1) #{'c': 1, 'b': 2, 'a': 1}
print("------------4-2 ")

"""
字典方式输出 "abbc"字符串中出现次数最多的字符--4个方法
1、字符串的count方法（列表也有count方法）
2、for循环字符串，添加键值对到空字典
3、counter（可迭代）方法
4、for循环字符串，判断i是否在dic1中，在的话，value自增1,不在的话，给初始值1
"""






