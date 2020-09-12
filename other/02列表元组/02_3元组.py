#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 元组
# 元组的元素不能修改

#1 查 获取元组的元素-切片
tu1=(1,2,3)
tu2=("jack","tom")
print(tu1[0])  #1  #获取元组的一个元素
print(tu1[1:3]) # (2,3) #获取元组的多个元素

#2 修改  元组的元素不能修改
tu1=(1,2,3)
tu2=("jack","tom")
# tu1[2]="bob" #TypeError: 'tuple' object does not support item assignment

#3 拼接  2个元组是可以拼接的，通过+
tu1=(1,2,3)
tu2=("jack","tom")
tu3 = tu1 +tu2
print(tu3) #(1, 2, 3, 'jack', 'tom')
# 注意：1、合并两个列表用的是extend内置方法，将列表2合并到列表1（改变了列表1）
    #  2、合并两个元组，用的是拼接+（拼接元组1和元组2，形成元组3，没有修改原元组，产生了拼接后的新元组）

#4 计算元组的长度-元素个数    len
tu1=(1,2,3)
print(len(tu1)) #3

#5 判断某个元素是否在元组中   in
tu1=(1,2,3)
print(3 in tu1)  #True
print(5 in tu1)  #False

#4 删除  元组的元素不可单独删除，但是可以用del删除整个元组，元组就不存在了
#01 删除整个元组
tu1=(1,2,3)
del tu1 #删除整个元组，元组不存在了
# print(tu1)  #NameError: name 'tu1' is not defined

#02 删除元组的元素 不允许
tu1=(1,2,3)
# del tu1[2] #TypeError: 'tuple' object doesn't support item deletion
"""
1、可以通过del删除列表的元素，但是不能通过del删除元组的元素--元组的元素不可修改
2、li3=[0,1,2,3]
    del li3[2]  #del 通过索引号-下标删除某个元素 该方法不限于列表
    tu1=(1,2,3)
    del tu1 #删除整个元组，元组不存在了
"""

#5 del方法（1、删除单个元素，2、删除所有元素-清空  3、删除整个变量-回收内存空间）
#1 del方法删除单个元素
#01 del删除列表中元素
li1=[1,2]
del li1[0]
print(li1) #[2]

#02 del删除字符串中元素-字符--不允许，因为字符串和数字 元组是不可变的
str1="jack"
# del str1[0]  #TypeError: 'str' object doesn't support item deletion
# print(str1)  #

#03 del删除元组中元素-不允许
tu1=(1,2)
# del tu1[0]  #TypeError: 'tuple' object doesn't support item deletion

#1 del方法删除整个列表、元组、字符串
#01 del删除整个列表--允许
li1=[1,2]
del li1  #和clear清空是不同的
# print(li1)  #NameError: name 'li1' is not defined

#02 del删除整个字符串-允许
str1="jack"
del str1  #
# print(str1)  #NameError: name 'str1' is not defined

#03 del删除整个元组-允许
tu1=(1,2)
del tu1 #
# print(tu1) #NameError: name 'tu1' is not defined








