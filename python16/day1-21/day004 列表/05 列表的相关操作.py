#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1 计算列表中指定元素出现的个数
li1 = ["jack","tom","bob","james"]
print(li1.count("jack")) #1  计算列表中的元素"jack"在列表中出现的次数（列表的元素是可以重复的）

#2 列表中元素的排序
#1 对原列表做了修改
li1 = ["jack","tom","bob","james"]
li1.sort() #注意：sort()将原列表的元素顺序进行了修改--原列表发生了改变
print(li1) #['bob', 'jack', 'james', 'tom'] #默认是升序（参数是空 reverse默认是False），字符串就按照音序来升序排列

li1 = ["jack","tom","bob","james"]
li1.sort(reverse=True)
print(li1) #['tom', 'james', 'jack', 'bob'] #参数是reverse=True，字符串按照音序降序排列

li1 = ["jack","tom","bob","james"]
li1.reverse()  #反转
print(li1)  #['james', 'bob', 'tom', 'jack']

# s1 = "jack"
# s1.reverse()  #AttributeError: 'str' object has no attribute 'reverse'
# print(s1)
print("-------------原列表改动")

# s1 = "jack"
# s1.sort()  #AttributeError: 'str' object has no attribute 'sort'  报错
# print(s1)

#2 原列表不做修改，新产生的列表排序
li1 = ["jack","tom","bob","james"]
li_sort = sorted(li1)  #sorted是关键字，不同于sort（）是列表的内置方法（可以通过列表名. 调出来）
print(li1) #['jack', 'tom', 'bob', 'james']
print(li_sort) #['bob', 'jack', 'james', 'tom']  #默认是升序

li1 = ["jack","tom","bob","james"]
li_sort = sorted(li1,reverse=True)   #表示要倒序（按照音序倒序排列）
print(li1) #['jack', 'tom', 'bob', 'james']
print(li_sort) #['tom', 'james', 'jack', 'bob']
print("-------------原列表不改动")

s1 = "jack"
li2 = sorted(s1)
print(s1) #jack
print(li2) #['a', 'c', 'j', 'k']  #返回的是列表
s2 = "".join(li2)  #将列表的元素通过连接符，拼接成字符串
print(s2) #acjk
print("--------------1")

s1 = "jack"
li2 = sorted(s1,reverse=True)
print(s1) #jack
print(li2) #['k', 'j', 'c', 'a']  #返回的是列表
s2 = "".join(li2)  #将列表的元素通过连接符，拼接成字符串
print(s2) #kjca
print("--------------2")

"""
列表的排序
1、原列表做改动
    列表名.sort() #默认升序
    列表名.sort(reverse=True) #降序-倒序  sort（）是列表的内置函数
    列表名.reverse() #反转 reverse()是列表的内置函数
2、原列表不做改动
    新列表名 = sorted(老列表名) #默认升序-新列表
    新列表名 = sorted(老列表名,reverse=True) #降序-新列表  sorted()是关键字，不是列表的内置方法
    #sorted()的参数除了是列表，还可以是字符串等其他可迭代的对象(不管参数是字符串还是列表，返回的都是列表)

注意：如果列表的元素是汉字，那么排序的功能就不好理解（排序主要针对列表的元素是1数字或者2字母组成的字符串）

倒序和反转是不同的
1、前者是按照音序降序排列
2、后者是按照列表或者字符串的元素的先后顺序，反转顺序

倒序的方法
方法1、列表名.sort(reverse= True)
方法2、新列表名 = sorted(老列表名,reverse=True)  #这里的sorted是关键字

反转的方法：
方法1、列表名[::-1]或者字符串名[::-1]
方法2、列表名.reverse()
"""

#3 计算列表的长度
li1 = ["jack","tom","bob","james"]
print(len(li1))  #4






