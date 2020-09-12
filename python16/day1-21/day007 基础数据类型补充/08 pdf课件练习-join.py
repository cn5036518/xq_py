#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一、join方法
#1列表
li1 = ["jack","tom","bob"]
s1 = "_".join(li1)  #参数是可迭代对象，返回是字符串，"_"是连接符号
# S.join(iterable) -> str
#         Return a string which is the concatenation of the strings in the
#         iterable.  The separator between elements is S.
print(s1)  #jack_tom_bob

# li2 = ["jack","tom",18]
# s1 = "_".join(li2) #注意点：可迭代对象（比如：列表）的元素必须是字符串类型才行，不能是int等其他类型，否则报错
# print(s1)  #报错 TypeError: sequence item 2: expected str instance, int found

#2字符串
s2 = "jack"
s3 = "_".join(s2)
print(s3)  #j_a_c_k

#可迭代对象：字符串、列表、字典、元组、集合--nok
#3字典
dic1 = {"name":"jack","age":18}
s1 = "_".join(dic1)  #参数是字典，连接的元素是key，由于key无序，所以是随机不可控-了解即可
print(s1)  #age_name 或者 name_age

#4 元组
tu1 = ("jack","tom","bob")
s1 = "_".join(tu1)
print(s1)  #jack_tom_bob

#5 集合
set1 = {"jack","tom"}
s1 = "_".join(set1) #参数是集合，由于集合的无序，所以是随机不可控-了解即可
print(s1) #jack_tom或者tom_jack
print("-----------join")















