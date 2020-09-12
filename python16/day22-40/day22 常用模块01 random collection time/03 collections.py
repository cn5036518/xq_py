#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/27 11:05

''''''
'''
计算字符串中字符出现的次数   #yanming

思路-算法：
1、遍历字符串
   定义一个空字典
2、如果字符不在空字典中，value置为1
3、如果字符在字典中，value自增1

思路2-内置模块
1、引入模块  from collection import Counter
2、创建一个Counter对象，参数传入字符串
3、返回值就是字符和字符出现次数的键值对
4、将返回值转换成字典类型
'''

s1 = 'ahfafafafd'

#方法1
dic1 = {}
for i in s1:
    if i not in dic1:
        dic1[i] = 1
    else:
        dic1[i] += 1  #自增1

print(dic1)  #{'a': 4, 'h': 1, 'f': 4, 'd': 1}
print('-----------------------1')

#方法1 函数  推荐  好理解
def count_charactor(s1):
    dic1 = {}
    for i in s1:
        if i not in dic1:  #如果字符不在空字典中，value置为1
            dic1[i] = 1
        else:  #如果字符在字典中，value自增1（这里的value用字典名[key]来表示）
            dic1[i] += 1  # 自增1
    print(dic1)

s1 = 'ahfafafafd'
count_charactor(s1)   #{'a': 4, 'h': 1, 'f': 4, 'd': 1}
print('-----------------------2 函数')

#方法2
s1 = 'ahfafafafd'
dic1 = {}
for i in s1:
    dic1[i] = dic1.get(i,0)+1
    #如果i不在字典中，value取1
    #如果i在字典中，取出i的value-次数，然后加1
print(dic1)  #{'a': 4, 'h': 1, 'f': 4, 'd': 1}
print('-----------------------2-1 简洁')

def count_charactor2(s1):
    dic1 = {}
    for i in s1:
        dic1[i] = dic1.get(i, 0) + 1
    print(dic1)
s1 = 'ahfafafafd'
count_charactor2(s1)  #{'a': 4, 'h': 1, 'f': 4, 'd': 1}
print('-----------------------2-2 简洁 函数')

#方法3   模块来解决
from collections import Counter
s1 = 'ahfafafafd'
print(Counter(s1))  #Counter({'a': 4, 'f': 4, 'h': 1, 'd': 1})
print(Counter(s1)['a'])  #4   #返回的结果可以当做字典来使用
print(type(Counter(s1)))  #<class 'collections.Counter'>
dic1 = dict(Counter(s1))  #转换成字典类型
print(dic1)  #{'a': 4, 'h': 1, 'f': 4, 'd': 1}
print('-----------------------3 模块')

li1 = ['a','a','b']
print(dict(Counter(li1)))  #{'a': 2, 'b': 1}
print('-----------------------4 传参数-可迭代的--列表')

'''
小结：
Counter的参数是可迭代的 iterable
比如：字符串、列表等都可以




'''



























