#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 4、有字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....}  (升级题)
s1 = "k:1|k1:2|k2:3|k3:4"
# dic1 = {'k': 1, 'k1': 2....}
li1 = s1.split("|")  #以"|"作为分割符，将字符串拆分成字字符串，然后将子字符串作为元素添加到列表
print(li1)  #['k:1', 'k1:2', 'k2:3', 'k3:4']

dic1 = {}
for i in li1:
    # print(i)
    # print(type(i))
    k,v = i.split(":")  #将字符串'k:1'进行拆分，
    dic1[k] = int(v)  #key-k和value-v依次添加到空字典  关键点  #遍历循环列表后，讲每个元素分拆成key和value后，依次添加到空字典
    # 注意点：这里的v是字符串，需要转换成int
print(dic1)  #{'k2': 3, 'k3': 4, 'k1': 2, 'k': 1}












