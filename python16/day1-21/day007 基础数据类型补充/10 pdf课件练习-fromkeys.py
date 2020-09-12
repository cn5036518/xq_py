#!/usr/bin/env python
#-*- coding:utf-8 -*-

#fromkeys用来新建字典，可以一次新建多个键值对，是类方法，通过类来调用
# 普通字典的额新建，是新建一个空字典，通过键值对一个一个的添加

#1 普通用法
li1=[1,2]
dic1 = dict.fromkeys(li1,"jack")   #类方法，通过字典类调用，会产生新的字典，对原来的字典没有任何改变
# 参数1必须是可迭代对象（字符串、列表、字典、元组、集合）
# 取参数1的每一个迭代元素作为字典的key，参数2不写默认是None，参数2指定的话，就作为字典的value
# 特点：可以新建字典，一次添加多个键值对，key是迭代元素，value都相同，value是参数2
 # dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
 #        v defaults to None.
print(dic1)  #{1: 'jack', 2: 'jack'}

#2 特殊用法
li1=[1,2]
li2 = []
dic2 = dict.fromkeys(li1,li2)   #类方法，通过字典类调用
print(dic2)  #{1: [], 2: []}
print(id(dic2[1]),id(dic2[2])) #35861128 35861128  说明2个key对应的value是同一个对象，一改都改，联动
dic2[1].append("jack")
print(dic2)  #{1: ['jack'], 2: ['jack']}












