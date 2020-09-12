#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 元组 不可变的列表-只读列表，小括号()括起

#1 小括号的算数优先级--特殊性
print((3+8)*7) #这里的小括号还表示算数优先级

print((1)) #1 #这里的小括号表示的是算数优先级，如果元组里面只有一个元素，就必须加上逗号
print(type(1)) #<class 'int'>

print((1,)) #(1,) #如果元组里面只有一个元素，就必须加上逗号；不加逗号就是整数（小括号还表示算数优先级）
tu1 = (1,)
print(type(1,))  #<class 'int'>   #注意：这里的1,就是整数，没有小括号就是整数
print(type((1,)))  #<class 'tuple'>
print(type(tu1))  #<class 'tuple'>

#2 空元组
tu1 = tuple()  #空元组正确表示1
tu1 = ()  #空元组的正确表示2
print(tu1)  #
print(type(()))  #<class 'tuple'>
# tu1 = (,) #空元组的错误表示

tu2 =("jack","tom","bob",) #元组--这个后面的逗号是允许添加的
print(tu2) #('jack', 'tom', 'bob')

#空列表的表示
li1 = []
li2 = list()

li3 =["jack","tom","bob",] ##列表--这个后面的逗号是允许添加的
print(li3)  #['jack', 'tom', 'bob']

#3 元组也有索引和切片，和列表字符串的索引切片是一样的
tu2 =("jack","tom","bob")
print(tu2[1]) #tom
print(tu2[:2]) #('jack', 'tom')  切片之后还是元组
print(tu2[::-1]) #('bob', 'tom', 'jack') 元组的反转 步长是-1 从右往左
# tu2[1] = "james" #报错 TypeError: 'tuple' object does not support item assignment
# 元组是可读的，不可修改（指第一层元素不可修改）
print("------------------3")

#4 元组的第一层元素是不可修改，第二层元素是否可以修改，取决于其数据类型
# 如果第二层元素是列表，则可以修改；如果第二层元素是元组，则不可以修改
tu1 = ("jack","tom","bob",["jack","tom","bob"])
tu1[-1].append("james") #元组的第二层元素是列表，可以修改第二层
print(tu1) #('jack', 'tom', 'bob', ['jack', 'tom', 'bob', 'james'])

# tu1[-1] = "kevin"  #报错 TypeError: 'tuple' object does not support item assignment
# 元组的第一层元素是不可修改的

#5 元组可以支持len() count() index()、遍历 但是不能排序（排序后就修改了）--可查不能修改
tu2 =("jack","tom","bob")
# for i in tu2: #元组也是可迭代对象（字符串、列表、元组都是可迭代对象）
#     print(i)








