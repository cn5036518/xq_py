#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一、列表的循环遍历过程中的删除，实现内置函数clear的算法
#1循环遍历中-直接删除--无法全部删除（只能删除索引号是偶数的元素，保留索引号是奇数的元素）
li1 = ["jack","tom","bob","james","kevin"]
for i in li1:  #内部有一个变量来记录当前被循环的位置, 索引.
    li1.remove(i)   #循环遍历列表的时候，会删除索引号是偶数的元素，这里删除了索引号是0的"jack"和索引号是2的“bob”
    #删除列表元素过程分析：
    # 1、删除索引号是0的元素后，后面的3个元素"tom","bob","james"会向前移动
    # 2 当删除索引号是1的元素的时候，“tom”已经从索引号是1变成了索引号是0，而“bob”的索引号从2变成了1，此时就把“bob”给删除了
    #    而tom没有被删除
    # 3 当删除索引号是2的元素的时候，“james”已经从索引号是3变成了索引号是1，而“kevin”的索引号从4变成了2，此时就把“kevin”给删除了
    #    而james没有被删除
print(li1)  #['tom', 'james']   #这个直接删除的方式，只能删除索引号是偶数的元素，保留索引号是奇数的元素

#2循环遍历中-间接删除
li1 = ["jack","tom","bob","james","kevin"]
"""
思路：
1、循环遍历列表1，将要删除的元素，添加到一个新的空列表2中（这个和li2 = li1[:]，复制列表效果是一样的）
2、循环遍历列表2，过程中，li1.remove[i],就可以实现把列表1-li1清空（实现列表clear的算法）
   这样，就可以避免在循环遍历列表1的时候，直接删除列表1的元素
"""

#间接删除-方式1   这个就是clear内置函数的底层实现算法--重点掌握1
li1 = ["jack","tom","bob","james","kevin"]
li2 = []
for i in li1:  #1遍历循环列表1
    li2.append(i)  #2把要删除的元素，依次添加到列表2
# print(li2) #['jack', 'tom', 'bob', 'james', 'kevin']
# li2 = li1[:]
# print(li2)
for i in li2:  #3 循环遍历列表2
    li1.remove(i)  #4  删除列表1中的元素（这里的i是key映射列表1和列表2的元素）  关键点1
print(li1)  #[]

#间接删除-方式2
li1 = ["jack","tom","bob","james","kevin"]
li2 = li1[:]  #复制列表
print(li2)  #['jack', 'tom', 'bob', 'james', 'kevin']
for i in li2:
    li1.remove(i)  #关键点1
print(li1)  #[]

"""
总结：
涉及列表的删除，注意点：
1、不可再遍历循环列表的时候，直接删除列表1的元素
2、只能间接删除，就是通过复制列表1  li2 = li1[:]
3、在循环遍历列表2的时候，删除列表1的元素---曲线救国的方式
"""

# 二、课上练习
# 删除下面列表中，以字母"j"开头的名字
li1 = ["jack","tom","bob","james","kevin"]
li2 = li1[:]  #1复制当前列表
for i in li2:  #2 遍历循环列表2
    if i.startswith("j"): #3 判断列表的元素是否是字母"j"开头
        li1.remove(i)  #4 符合条件的，从列表1中删除
print(li1)  #['tom', 'bob', 'kevin']
print("--------------2")

#三、字典在循环遍历的过程中，可以修改key，但是不能直接删除也不能新增元素（键值对）
dic1 = {"name":"jack","age":18}
# for i in dic1:
#     dic1.pop(i)  #删除报错  RuntimeError: dictionary changed size during iteration
# for i in dic1:
#     dic1["hobby"] = "running"  #新增报错  RuntimeError: dictionary changed size during iteration

for i in dic1:
    dic1["name"] = "tom"  #字典在循环遍历的过程中，可以修改key
print(dic1)  #{'name': 'tom', 'age': 18}
print("--------------3")

#四、字典在循环遍历的过程中，如何间接删除？--实现clear的底层算法
"""
思路：
1、循环遍历字典，将要删除的key依次添加到空列表1
2、遍历循环空列表1，在循环过程中，dic1.pop(i)
"""

dic1 = {"name":"jack","age":18}
li1 = []
for i in dic1:  #1 遍历循环字典
    li1.append(i) #2 将要删除的字典的key依次添加到空列表1
print(li1)  #['age', 'name']

for i in li1:  #3 循环遍历列表1
    dic1.pop(i)  #4 删除字典的key
print(dic1)  #{}



