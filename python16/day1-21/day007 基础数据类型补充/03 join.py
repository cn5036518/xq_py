#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1   join的用法  把列表转成字符串  参数是可迭代类型（列表、字符串、字典都行）
li1 = ["jack","tom","bob"]
s1 = "_".join(li1)  #这里的_是连接符，参数是列表，返回的是字符串  （将列表的元素通过连接符_ 进行连接后，返回大字符串）
print(s1)  #jack_tom_bob

s3 = "jack"
s4 = "_".join(s3)  #参数是字符串，返回的也是字符串（将字符串的每个元素通过连接符_ 进行连接后，返回字符串）
print(s4)  #j_a_c_k

dic1 = {"name":"jack","age":18}
s5 = "_".join(dic1) #参数是字典，返回的是字符串（将字典的key通过连接符_ 进行连接后，返回字符串）
print(s5)  #name_age或则age_name  #注意：这里由于字典的无序性，拼接的字符串是不可控的

dic1 = {"name":"jack","age":"18"}
s5 = "_".join(dic1.values())
#报错 TypeError: sequence item 1: expected str instance, int found  这个错误是"jack"和18 无法拼接（字符串和数字无法直接拼接）
print(s5)  #jack_18 或者18_jack  #注意：这里由于字典的无序性，拼接的字符串是不可控的
print("----------------1")

#2   split的用法  把字符串拆分成列表
s2 = "jack_tom_bob"
li2 = s2.split("_")  #这里"_"是分隔符，把字符串，以分隔符"_"进行拆分，查分后的小字符串，作为列表的元素，返回列表
print(li2)  #['jack', 'tom', 'bob']















