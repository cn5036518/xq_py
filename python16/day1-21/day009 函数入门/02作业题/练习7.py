#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
	PS:字典中的value只能是字符串或列表
'''


# for k, v in dic1.items():
#     print(k)
#     print(v)

#方法1  应该不对
def first_two(dic1):
    li1 = []
    for k,v in dic1.items():  #注意items必须加上，否则报错   注意点
        if len(v) > 2:
            # return v[:2]
            # return v[0],v[1]
            # return v[0],v[1]
            li1.append(v[:2])
    return li1

dic1 = {"k1": "v1v1", "k2": [11,22,33,44]}
ret = first_two(dic1)
print(ret)   #[[11, 22], 'v1']
print('--------------------------------1')

'''
问题：
由于字典的无序性
这里有时返回[11, 22]或者(11,22)，有时返回v1或者 (v,1)  #必须换思路
复习循环遍历字典--'''

#方法2   正确
def first_two2(dic1):
    for k,v in dic1.items():  #注意items必须加上，否则报错   注意点
        if len(v) > 2:
            v=v[0:2]  #获取字典value的前2位
            dic1[k] = v   #关键点，组成字典
    return dic1

dic1 = {"k1": "v1v1", "k2": [11,22,33,44]}
ret = first_two2(dic1)
print(ret)   #{'k1': 'v1', 'k2': [11, 22]}










