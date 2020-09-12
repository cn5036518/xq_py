#!/usr/bin/env python
#-*- coding:utf-8 -*-

#创建字典的两种方式
#方法1--单个元素添加
# 先定义空字典，一个一个添加键值对的方式

#方法2--多个元素（键值对）添加  fromkeys
li1 = ["jack","tom"]
dic1 = {}
dic2 = dic1.fromkeys(li1,19)
dic3 = dic1.fromkeys(li1)
dic4 = dic1.fromkeys(li1,[])
# 将参数1的每一个元素作为key(参数1是可迭代对象)，参数2作为value，一次添加到字典，参数2不写默认是None
# dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
#         v defaults to None.
print(dic2)  #{'tom': 19, 'jack': 19}
print(dic3)  #{'tom': None, 'jack': None}
print(dic4)  #{'tom': [], 'jack': []}
# 注意点，所有的key都是共用同一个列表（同一个对象)，所以改变其中一种，其余的也随着改变
print(id(dic4["jack"]))  #35442120
print(id(dic4["tom"]))  #35442120

dic4["jack"].append(18)
print(dic4)  #{'jack': [18], 'tom': [18]}













