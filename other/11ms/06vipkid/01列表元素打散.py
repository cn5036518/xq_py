#!/usr/bin/env python
#-*- coding:utf-8 -*-

#列表中的元素打散（重新排列），每个元素不能出现在原来的位置
# 比如 li1= [1,2,3]  元素1不能出现在位置1  元素2不能出现在位置2 元素3不能出现在位置3
import random
li1= [1,2,3]
li2 = []
for i in range(len(li1)):
    num1 = random.randrange(0,len(li1))
    if i != num1:
        li2.append(li1[num1])
print(li2)
print("-----------0")

#1可以将列表的元素打乱重新排列，改变了原来的列表本身
import random
li1= [1,2,3]   #1直接定义列表
random.shuffle(li1)  #可以将列表的元素打乱重新排列，改变了原来的列表本身（但是还无法做到每个元素不在原来的位置）
print(li1)
print("-----------1")

#2可以将列表的元素打乱重新排列，改变了原来的列表本身
import random
x = [i for i in range(2)]   #2新建列表的方法2   列表推导式
print(x)
random.shuffle(x)  #可以实现把列表的元素随机排列
print(x)
print("-----------2")

#3 choice函数的参数是可迭代对象（元素、列表、字典、集合、元组），返回的是可迭代对象中任意一项
li1= [1,2,3]
li2 = random.choice(li1)
print(li2)  #1

s1 = "jack"
li2 = random.choice(s1)
print(li2)  #k
print("-----------3")

#4  从列表中随机选择n个元素，组成新的列表
li1= [1,2,3]
# tu1 = (1,2,3)
li2 = random.sample(li1,3)  #参数1是列表，参数2是要选择随机元素的个数，返回的是列表
# li2 = random.sample(tu1,3)  #参数1是元组，参数2是要选择随机元素的个数，返回的是列表
print(li2)
print("-----------4")

"""
总结：
1、给列表(可迭代对象)本身的元素重新排序
    random.shuffle（li1）
2、从列表（可迭代对象）中随机选择一个元素返回，返回的是字符串
    s1 = random.choice(li1)
3、从列表（可迭代对象）中随机选择n个元素返回，返回的是列表
    li2 = random.sample(li1,n)
"""
import random
li1 = [11,22,33]
li2 = []
for i in range(len(li1)):
    s1 = random.choice(li1[:i]+li1[i+1:])  #1先对列表切片，将当前位置的元素排查，选择当前位置之外的任意元素
    print(s1)
    #第一次 s1=33  li2=[33]
    #第二次 s1=33  li2=[33,11]
    #第三次 s1=22  li2=[33,11,22]-ok
            #s1 =11 li2[33,11]
    if s1 not in li2:  #2如果元素不在空列表2，就添加到列表2
        li2.append(s1)
    else:  #3如果元素在空列表2，如果不添加，就会少一个元素，所以必须添加
        #4通过集合的差集，将已经添加的元素去掉
        #5 由于集合的元素是去重的，所以将集合的元素循环遍历追加的列表2即可
        set1 = set(li1)  #{11,22,33}
        set2 = set(li2)  #{33}    {33,11}
        set3 = set1 - set2 #{11,22}  {22}
        print(set3)
        for i in set3:
            li2.append(i)
            # print(li2)
print(li2)
#目前存在的问题：最后一个元素是33的情况还没有排查，先到这里，先继续往下，后续再回头温习
# 22
# 11
# 22
# {33}
# [22, 11, 33]













