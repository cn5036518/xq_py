#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一、字典
#字典的key不能重复，如果重复，就是后面的key的值覆盖前面的key的值
#字典的key必须是可哈希的，不可变的（int str bool 元组），而不能是列表、字典
dic1 = {"a":"娃哈哈","a":"爽歪歪"}
print(dic1)  #{'a': '爽歪歪'}  #前面的key的值被覆盖了

# dic1[[1,2,3]] = "娃哈哈"  #TypeError: unhashable type: 'list'  报错
dic1[(1,2,3)] = "娃哈哈"
print(dic1)  #{'a': '爽歪歪', (1, 2, 3): '娃哈哈'}
# dic1[(1,[1,2],3)] = "娃哈哈2"  #TypeError: unhashable type: 'list'  报错
#注意点：这里的元组内嵌列表也是不可哈希的，会报错
print("---------1 字典")

"""
#1字典的key不能重复，如果重复，就是后面的key的值覆盖前面的key的值
#2字典的key必须是可哈希的，不可变的（int str bool 元组），而不能是列表、字典
  注意点：元组中内嵌列表的话，也是可变的（不可哈希），会报错
3 字典的key是无序的（散列）
"""

# 二、集合  set  特点:1去重、2无序、3元素不可变   -重点1
#集合的理解：集合就是不存value，只保存key的字典    -重点2

# 1空集合
set1 = set()   #而不能是{}，{}表示的是空字典
#2 集合的元素是去重的，用{}来表示
set1 = {1,2,3,3,2,1}
print(set1)  #{1, 2, 3}
#3 集合的元素是无序的(所以没有索引)   对比：字典是无序的，根据key来取值（key不可重复）；列表是有序的，有索引（key重复）
   #集合就是不存value，只保存key的字典--关键点 理解
#4 集合set的元素必须是可哈希（不可变的）--int str bool tuple
# set1 = {1,2,3,3,2,1,[1,2]}  #TypeError: unhashable type: 'list'  报错
print("------------  集合2")

#列表的去重,通过集合set--重点掌握1
li1 = [1,1,2,3,4,4,5]
set1 = set(li1)  #列表转成集合--就可以去重
print(set1)  #{1, 2, 3, 4, 5}
li2 = list(set1)  #集合转成列表
print(li2)  #[1, 2, 3, 4, 5]

#列表去重的底层算法--方法1  简洁  推荐
li1 = [1,1,2,3,4,4,5]
li2 = []
for i in li1:
    if i not in li2:  #如果元素不在li2中，就往其中添加
        li2.append(i)
print(li2)  #[1, 2, 3, 4, 5]

#列表去重的底层算法--方法2  练习continue的用法
li1 = [1,1,2,3,4,4,5]
li2 = []
for i in li1:
    if i in li2:  #如果元素在li2中，就跳过当次循环，进入下一次循环
        continue
    else:  #如果元素不在新列表li2中，就添加到新列表li2中
        li2.append(i)
print(li2)  #[1, 2, 3, 4, 5]

print("--------------2 列表去重")

#三 集合的增删改查
#一、新增
#1单个元素新增  add
set1 = {1,2,3,4}
set1.add(33)
# set1.add(33,44)  #TypeError: add() takes exactly one argument (2 given)  报错
# 一次只能添加一个元素到集合中，一次添加多个元素到集合中，会出现报错
 # Add an element to a set.   #如果有多个换行，就有类似右键 “选择性粘贴”--paste simple
 #        This has no effect if the element is already present.
print(set1)  #{1, 2, 3, 4, 33}
#注意点：虽然打印后，集合的元素是固定顺序-表明现象，但是集合的元素在内存中的存储就是无序的--实质现象1

#2 迭代新增  update  一次添加多个元素到原集合  （类似于列表的extend方法--迭代添加）
set1 = {1,2,3,4}
set1.update("jack")  #参数是可迭代类型（字符串、列表、字典、元组、集合），将参数的每个元素依次添加到集合
# Update a set with the union of itself and others.
print(set1)  #{1, 2, 3, 4, 'a', 'c', 'k', 'j'}

li1 = ["tom","bob"]
set1.update(li1)  #将列表的元素依次添加到集合中
print(set1)  #{1, 2, 3, 4, 'bob', 'j', 'k', 'tom', 'c', 'a'}

tu1  = (88,99)
set1.update(tu1)  #将元组的元素依次添加到集合中
print(set1)  #{'j', 1, 2, 3, 4, 'k', 'c', 'a', 99, 'bob', 88, 'tom'}
print("-----------3-1 新增")

#二删除
#1 pop 随机删除
set1 = {1,2,3,4}
ret1 = set1.pop()  #随机删除集合的一个元素  随机不可控--用的少
   # Remove and return an arbitrary set element.
   #      Raises KeyError if the set is empty.
print(ret1) #1
print(set1)  # {2, 3, 4}

#2 remove 指定删除
set1 = {1,2,3,4}
set1.remove(2)  #指定元素的名字，进行删除
  # Remove an element from a set; it must be a member.
  #       If the element is not a member, raise a KeyError.
print(set1)  #{1, 3, 4}

#3 clear  清空
set1 = {1,2,3,4}
set1.clear() #清空集合中的元素
# Remove all elements from this set.
print(set1)  #set()而不是{}   空集合
print("-----------3-2 删除")

#三 集合的修改
""""
列表可以根据索引指定位置后修改
字典key根据key指定value后，对value进行重新赋值来修改
但是，集合是无序的（所以没有索引），集合也没有key，索引集合无法直接修改
修改集合：间接修改的方式  先删除指定元素-remove，然后新增一个元素-add
"""
set1 = {1,2,3,4}
set1.remove(3)   #把集合中元素3改成6，先删除3，然后添加元素6来完成
set1.add(6)
print(set1)  #{1, 2, 4, 6}
print("-----------3-3 修改")

#四 集合的查询
# 因为集合是可迭代对象，所有可以for循环遍历
#可迭代对象（字符串、列表、字典、元组、集合）--已知5种
set1 = {1,2,3,4}  #特点:1去重、2无序、3元素不可变（int str bool tuple），而不能是列表、字典、集合
#可变类型（列表、字典、集合）
# set2 = {1,2,{1,3},4}  # 报错  TypeError: unhashable type: 'set'
# print(set2)

for i in set1:
    print(i,end=" ")  #1 2 3 4
print()  #换行

for i in set1:
    print(i,end="")  #1234   把集合（列表）的元素拼接起来，输出
print()  #换行
print("-----------3-4 查询")

"""
小结：
一、是否是可迭代类型（对象）
1、可迭代类型--可以for循环遍历
    字符串、列表、字典、元组、集合
2、不可迭代类型
    int bool

二、是否是可变类型
    1、不可变类型(可哈希-hash)
        字符串 整数 元组 布尔
    2、可变类型(不可哈希-不可hash)
        列表、字典、集合
"""

#四、集合的常用操作  交集-并集-差集-反交集等
set1 = {1,2,3,4}
set2 = {3,4,5,6}

#1 交集  & intersection(交点)
print(set1&set2)  #{3, 4}
print(set1.intersection(set2))  #{3, 4}
 # Return the intersection of two sets as a new set.
 #        (i.e. all elements that are in both sets.)

#2 并集   |  union(联合、联盟)
print(set1|set2)  #{1, 2, 3, 4, 5, 6}
print(set1.union(set2)) #{1, 2, 3, 4, 5, 6}
  # Return the union of sets as a new set.
  #       (i.e. all elements that are in either set.)

#3 差集  - difference(差别)
print(set1-set2)  #{1, 2}  集合1中的元素，去掉集合2的元素（集合1的元素，去掉2个集合的交集）
print(set2-set1)  #{5, 6}
print(set2.difference(set1))  #{5, 6}
 # Return the difference of two or more sets as a new set.
 #        (i.e. all elements that are in this set but not the others.)

#4 反交集  ^  symmetric_difference（对称差）
# (反交集=并集-交集) 2个集合各自特有的元素，合并起来
print(set1^set2)  #{1, 2, 5, 6}
print(set1.symmetric_difference(set2))  #{1, 2, 5, 6}

set3 = {3,4}
set4 = {3,4,5,6}
#5 子集  <  issubset
print(set3<set4)  #True
print(set3.issubset(set4))  #True  判断集合3是否是集合4的子集
# Report whether another set contains this set.

#6 超集  >  issuperset
print(set4 > set3)  #True
print(set4.issuperset(set3)) #True 判断集合4是否是集合3的超集
# Report whether this set contains another set.

#7 集合set是可变的，还有一种集合frozenset是不可变的（只读，类似元组）  不常用-了解即可
frozenset1 = frozenset("jack")  #参数是可迭代类型（字符串、列表、字典、元组、集合）
print(frozenset1)  #frozenset({'a', 'j', 'c', 'k'})

li2 = ["jack","tom"]
frozenset2 = frozenset(li2)
print(frozenset2) #frozenset({'tom', 'jack'})

dic1 = {frozenset2:18}  #不可变的集合-frozenset（冻结集合）可以作为字典的key，而普通set是可变的，不能作为字典的key
print(dic1)  #{frozenset({'jack', 'tom'}): 18}

"""
集合set的重点总结
特点:1去重、2无序、3元素不可变（和字典的key类似，必须是不可变得的）
#集合的理解：集合就是不保存value，只保存key的字典

"""








