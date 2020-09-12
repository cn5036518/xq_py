#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/14 8:37

''''''
'''
需求
从[1,2,3,4,5,6,7,8,9]中取值，将大于6的放在一个列表，将小于等于6的放在一个列表

思路：
方法1、setdefault
方法2、defaultdict

'''
#方法1
li1 = [1,2,3,4,5,6,7,8,9]
li2 = []
li3 = []

for i in li1:
    if i >6:
        li2.append(i)
    else:
        li3.append(i)
print(li2,li3)
dic1 = {}
dic1['key1']=li2
dic1['key2']=li3
print(dic1)  #{'大于6': [7, 8, 9], '小于等于6': [1, 2, 3, 4, 5, 6]}
print('----------------------------------1  方法1')

#方法2  defaultdict
from collections import defaultdict
li1 = [1,2,3,4,5,6,7,8,9]
dd = defaultdict(list)  #一旦取值取不到，就会返回默认值list() 即[]
for i in li1:
    if i > 6:
        dd['key1'].append(i)   #这里的dd['key1'],当key1对应的value不存在的时候，返回是[]空列表
    else:
        dd['key2'].append(i)
print(dd)  #defaultdict(<class 'list'>, {'key2': [1, 2, 3, 4, 5, 6], 'key1': [7, 8, 9]})
print(dict(dd))  #{'key2': [1, 2, 3, 4, 5, 6], 'key1': [7, 8, 9]}
print('----------------------------------2  defaultdict 方法2')

#方法3 setdefault
li1 = [1,2,3,4,5,6,7,8,9]
dic1 = {}
for i in li1:
    if i > 6 :
        dic1.setdefault('key1',[]).append(i)
    else:
        dic1.setdefault('key2', []).append(i)
print(dic1)  #{'key2': [1, 2, 3, 4, 5, 6], 'key1': [7, 8, 9]}
print('----------------------------------3  setdefault 方法3')

dic2 = {}
# dic2 = {'key1':124,'key2':125}
ret = dic2.setdefault('key1',[])   #如果key1的value存在，则返回key1对应的value；
#如果key1的value不存在，则返回默认值[]
print(ret)  #124  #[]
print(dic2)  #{'key1': []}











