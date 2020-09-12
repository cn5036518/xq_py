#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
集合的定义和特点：
特点：无序、去重、元素不可变
表示：用{}表示，空集合 set()
本质：集合是值保存key，不保存value的字典
注意：集合的元素是不可变对象，但是集合本身是可变的

不可变对象：int str bool tuple
可变对象：list dict set

可迭代对象：str list dict set tuple  （key遍历循环）
不可迭代对象：int bool
"""

#一 集合的3个特点 ：无序、去重、元素不可变
#1 集合的元素是不可变对象，但是集合本身是可变的
# set1 = {'1','alex',2,True,[1,2,3]}  #  报错 TypeError: unhashable type: 'list'  不可哈希-可变
# set2 = {'1','alex',2,True,{1:2}} #  报错 TypeError: unhashable type: 'dict'  不可哈希-可变
# set3 = {'1','alex',2,True,(1,2,[2,3,4])} #  报错 TypeError: unhashable type: 'list'
# 注意：集合的元素可以是元组，但是元组中嵌套列表就不符合要求

# 2集合是无序的，这个和字典的key的特点是一样的
# 所以才说，集合的本质是：只保存key，不保存value的字典

# 3集合的元素是不重复的，适用场景：给列表的元素去重
#   先把列表转换成集合（元素去重），然后把集合转换成列表，从而实现列表的元素去重

#二、集合的增删改查
#一、新增
#1 add方法   单个增加元素到集合
set1 = {'1','alex'}
set1.add("jack")
 # Add an element to a set.
 #        This has no effect if the element is already present.
print(set1)  #{'1', 'alex', 'jack'}

#2 update方法  一次添加多个元素到集合
set1 = {'1','alex'}
s1 = "jack"
set1.update(s1)  #1参数是可迭代对象，将参数的每个元素迭代添加到集合中
# Update a set with the union of itself and others.
print(set1)   #{'alex', '1', 'c', 'a', 'j', 'k'}

set1 = {'1','alex'}
li1 = ["jack","tom"]
set1.update(li1)  #1参数是可迭代对象，将参数的每个元素迭代添加到集合中
# Update a set with the union of itself and others.
print(set1)   #{'alex', 'jack', 'tom', '1'}
print("-----------1新增")

"""
可迭代对象：字符串、列表、字典、元组、集合  （可以用来for循环迭代取出每一个元素）
"""

#二、删除
#1 pop方法--随机删除
set1 = {'1','alex'}
ret1 = set1.pop()  #从集合中随机删除一个元素，并且获取这个元素，保存到一个变量中，#随机删除，不可控，了解即可
print(ret1)
print(set1)
 # Remove and return an arbitrary set element.
 #        Raises KeyError if the set is empty.
print("-----------2-1 删除 pop")

#2 remove方法--指定元素删除
set1 = {'1','alex'}
set1.remove("alex")  #指定集合的元素名称，进行删除
     # Remove an element from a set; it must be a member.
     #    If the element is not a member, raise a KeyError.
print(set1)  #1
print("-----------2-2 删除 remove")

#3 clear方法--清空
set1 = {'1','alex'}
set1.clear()  #清空集合中的所有元素
print(set1)  #set()   #空集合是set(),而不是{},{}表示的是空字典
print("-----------2-3 删除 clear")

#三 修改
# 集合中没有索引，元素是无序的，索引无法指定元素进行直接修改
# 间接修改集合的办法，先删除一个元素，然后新增一个元素，从而实现间接修改
set1 = {'1','alex'}   #将集合中的元素"jack"修改成"tom"
set1.remove("alex")   #1先从集合中删除元素"alex"
set1.add("tom")       #2再从集合中新增元素"tom"
print(set1)  #{'tom', '1'}
print("-----------3 修改 remove add")

#四 查询
#集合是可迭代对象（字符串、列表、字典、元组、集合），可以通过for循环进行遍历查看每一个元素
set1 = {'1','alex'}
for i in set1:
    print(i)
print("-----------4 查询 for")

#三 集合的其他操作
# 交集、并集、差集、反差集、子集、超集
#1 交集 & intersection
set1 = {'1','alex'}
set2 = {'1','tom'}
set3 = set1 & set2   #计算两个集合的交集（两个集合中都存在的元素）
set4 = set1.intersection(set2)
        # Return the intersection of two sets as a new set.
        # (i.e. all elements that are in both sets.)
print(set3)  #{'1'}
print(set4)  #{'1'}
print("-----------3-1 交集")

#2 并集 | union
set1 = {'1','alex'}
set2 = {'1','tom'}
set3 = set1 | set2  #计算两个集合的并集（）
set4 = set1.union(set2)
 # Return the union of sets as a new set.
 #        (i.e. all elements that are in either set.)
print(set3)  #{'alex', 'tom', '1'}
print(set4) #{'alex', 'tom', '1'}
print("-----------3-2 并集")

#3 差集 - difference
set1 = {'1','alex'}
set2 = {'1','tom'}
set3 = set1 - set2 #计算差集（将两个集合中交集的部分，从集合1中去掉）
set4 = set1.difference(set2)
    # Return the difference of two or more sets as a new set.
    #     (i.e. all elements that are in this set but not the others.)
print(set3)  #{'alex'}
print(set4)  #{'alex'}
print("-----------3-3 差集")

#4 反差集 ^ symmetric_difference（对称差）
set1 = {'1','alex'}
set2 = {'1','tom'}
set3 = set1 ^ set2  #计算反差集（将两个集合的并集-两个集合的交集=反差集）
set4 = set1.symmetric_difference(set2)
# Return the symmetric difference of two sets as a new set.
#         (i.e. all elements that are in exactly one of the sets.)
print(set3)  #{'tom', 'alex'}
print(set4)  #{'tom', 'alex'}
print("-----------3-4 反差集")

# 5 子集 < issubset
set1 = {'1', 'alex'}
set2 = {'1'}
print(set2 < set1)  # True  子集（计算返回集合2是否是集合1的子集，是的话，返回True，不是的话，返回False）
print(set2.issubset(set1))  # True
# Report whether another set contains this set.
print("-----------3-5 子集")

# 6 超集 > issuperset
set1 = {'1', 'alex'}
set2 = {'1'}
print(set1 > set2)  # True  超集（计算返回集合1是否是集合2的超集，是的话，返回True，不是的话，返回False）
print(set1.issuperset(set2))  # True
# Report whether another set contains this set.
print("-----------3-6 超集")

# 7 冻结的集合 frozenset
# 集合本身是可变的（可以修改）（列表、字典、普通集合set），因此不能作为字典的key，
# 字典的key必须是不可变的（可哈希）（字符串、整数、元组、布尔、冻结集合frozenset）
li1 = ["jack","tom","bob"]
frozenset1 = frozenset(li1)  #参数是列表等可迭代的类型(集合)
print(frozenset1)  #frozenset({'jack', 'bob', 'tom'})
dic1 = {"name":"alex",frozenset1:18}
print(dic1)  #{frozenset({'bob', 'jack', 'tom'}): 18, 'name': 'alex'}

set1 = {"jack","tom","bob"}
frozenset1 = frozenset(set1)  #参数是集合等可迭代的类型(列表、集合)
print(frozenset1)  #frozenset({'jack', 'bob', 'tom'})
dic1 = {"name":"alex",frozenset1:19}
print(dic1)  #{frozenset({'bob', 'jack', 'tom'}): 19, 'name': 'alex'}
print("----------------7-2")

s1 = "jack"
frozenset1 = frozenset(s1)  #参数是字符串等可迭代的类型(列表、集合、字符串、元组)
print(frozenset1)  #frozenset({'a', 'c', 'j', 'k'})
dic1 = {"name":"alex",frozenset1:20}
print(dic1)  #{'name': 'alex', frozenset({'a', 'c', 'j', 'k'}): 20}
print("----------------7-3")

dic1 = {"name":"jack","age":21}
frozenset1 = frozenset(dic1)  #参数是字典等可迭代的类型(列表、集合、字符串、元组、字典)
print(frozenset1)  #frozenset({'name', 'age'})
dic1 = {"name":"alex",frozenset1:20}
print(dic1)  #{'name': 'alex', frozenset({'name', 'age'}): 20}
print("----------------7-4")

dic1 = {"name":"jack","age":21}  #字典是可变的，字典本身不能作为其他字典的key
# dic2 = {"name":"alex",dic1:20}  #TypeError: unhashable type: 'dict'

#四 深浅拷贝
# 1 等号赋值  一变都变，联动
# 不管是列表、字典还是集合，通过等号赋值后，并没有把原来的列表或者字典拷贝一份，而只是拷贝了原列表或者字典的内存地址
# 所以，对原列表或者字典的内容修改后，等号赋值的新变量也随之修改
li1 = ["jack","tom"]
li2 = li1   #等号赋值后，新变量和老变量指向的是同一个对象（内存地址），新变量并没有对原列表复制一份
li1.append("bob")
print(li1)  #['jack', 'tom', 'bob']
print(li2)  #['jack', 'tom', 'bob']
print("----------------四 深浅拷贝 1--等号赋值")

# 对于list, set, dict来说, 直接赋值. 其实是把内存地址交给变量. 并不是复制一份内容. 所以.
# lst1的内存指向和lst2是一样的. lst1改变了, lst2也发生了改变

# 2 浅拷贝  不会出现一变都变，不会出现联动（浅拷贝后，两个对象的修改是彼此独立的）
#浅拷贝. 只会拷贝第一层. 第二层的内容不会拷贝. 所以被称为浅拷贝
#方式1  copy()
li1 = ["jack","tom"]
li2 = li1.copy()  #
li1.append("bob")
print(li1)  #['jack', 'tom', 'bob']
print(li2)  #['jack', 'tom']
print("----------------浅拷贝 2-1 copy（）")

#方式2  切片 [:]
li1 = ["jack","tom"]
li2 = li1[:]  #
li1.append("bob")
print(li1)  #['jack', 'tom', 'bob']
print(li2)  #['jack', 'tom']
print("----------------浅拷贝 2-2 [:]")
#  注意点：浅拷贝，只拷贝了第一层，第二层还是指向同一个对象（内存地址）
#        所以，浅拷贝后，修改第一层，两个对象是独立的，不是一改都改，不是联动的
#         浅拷贝后，如果修改第二层，就会出现一改都改，联动的现象（如何让修改第二层，也不出现联动现象呢？--深拷贝）

# 浅拷贝后，第二层的修改,会出现一改都改的联动现象
li1 = ["jack",["jack","tom"]]
li2 = li1.copy()
li1[1].append("bob")
print(li1)  #['jack', ['jack', 'tom', 'bob']]
print(li2)  #['jack', ['jack', 'tom', 'bob']]
print("----------------浅拷贝 2-3 修改第二层")

#3 深拷贝  两个对象完全是独立的，不管修改第一层还是第二层，还是任何一层，都不会出现一改都改的联动现象
# 判断2个对象是否指向同一个对象，用id()来判断
#深度拷贝. 把元素内部的元素完全进⾏拷贝复制. 不会产生一个改变另一个跟着改变的问题

import copy
li1 = ["jack",["jack","tom"]]
li2 = copy.deepcopy(li1)
#Deep copy operation on arbitrary Python objects
li1[1].append("bob")
print(li1)  #['jack', ['jack', 'tom', 'bob']]
print(li2)  #["jack",["jack","tom"]]
print("----------------深拷贝 3-1 修改第二层")

"""
等号赋值和深浅拷贝总结
1、等号赋值，等号赋值后，新老对象指向的是同一个对象（内存地址），一改都改、联动
    类比：夫妻不aa，共用一个账户，不是丈夫还是妻子花钱了，账户余额都变动了
2、浅拷贝，浅拷贝后，新老对象指向的不是同一个对象（内存地址），不会一改都改，不联动--第一层
        但是，浅拷贝只拷贝第一层，如果第二层修改了，还是会出现一改都改的联动现象--第一层之外的其它层（第2,3,4...层）
        因为，第二层、第三层等都指向的是同一个对象（内存地址）
    类比：夫妻aa，但是还设立了一个双方共用的家庭账户
        夫妻花各自账户的钱，是不会影响对方账户的余额。但是家庭公共账户是公共的，只要一方花了，就是一改都改、联动
3、深拷贝，深拷贝后，新老对象的每一层都是独立的（没有任何一层是指向同一个对象的），
        所以不管修改那一层，都不会出现一改都改，不会出现联动
    类比：夫妻aa，各自花各自的钱，账户是完全独立的

结论总结：
1、等号赋值：一改都改、联动
2、深拷贝： 不会出现一改都改，不会出现联动   （不管哪一层，都是独立的，都不会出现一改都改，不会出现联动）
3、浅拷贝： 第一层，不会出现一改都改，不会出现联动
            第一层之外（第2,3...层），一改都改、联动

1. 赋值。   不会产生新对象。 和拷贝没关系
2. 浅拷贝。 只会复制自身第一层。 会创建对象
2. 深拷贝。 把内部所有的内容都进行拷贝。
"""














