#!/usr/bin/env python
#-*- coding:utf-8 -*-

li1 = ["jack","tom","bob"]
# 需求：把列表的每个元素用连接符号"_"进行连接，返回一个字符串
#方法1  join方法
s1 = "_".join(li1)  #参数是可迭代对象（列表、字典、字符串、元组、集合）
print(s1)  #jack_tom_bob

#方法2  join方法的实现算法
# 思路：遍历循环列表，将空字符串，依次进行拼接   --累加-拼接的思想  要掌握
s2 = ""  #空字符串
for i in li1:
    s2 = s2+i+"_"  #累计拼接的思想  关键点
# 第一次取值  jack_
# 第二次取值  jack_tom_
# 第三次取值  jack_tom_bob_
s2 = s2[:-1]  #切片去掉最后一位
print(s2)  #jack_tom_bob















