#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1导包
import collections

#2指定文件路径
path1 = r"D:\xq_py\11gd\001.txt"
path2 = r"D:\xq_py\11gd\002.txt"

#3将文件1中每一行作为元素读取到列表1中
file_obj1 = open(path1,encoding="utf-8")
ret3 = file_obj1.readlines()
print(ret3)  #['张三\n', '张三\n', '李四\n', '李四\n', '王五']
ret1 = set(ret3)  #列表转换成集合  去重
print(ret1)  #{'张三\n', '李四\n', '王五'}
# print(type(ret1))

#4将文件2中每一行作为元素读取到列表2中
file_obj2 = open(path2,encoding="utf-8")
ret4 = file_obj2.readlines()
ret2 = set(ret4)  #列表转换成集合  去重
print(ret2)  #{'张三\n', '王五\n', '李四\n'}

ret_jiaoji = ret1 & ret2
print("交集",ret_jiaoji)  #交集 {'张三\n', '王五\n', '李四\n'}

# ret_chaji = ret1 - ret2
# print("差集",ret_chaji)

li1 = list(ret_jiaoji)
print(li1)  #集合的交集转换成列表   #['张三\n', '王五\n', '李四\n']

obj1 = collections.Counter(ret3) #统计文件1中
print(obj1) #Counter({'张三\n': 2, '李四\n': 2, '王五\n': 1})
obj1 = dict(obj1)  #counter转换成字典 {'张三\n': 2, '王五\n': 1, '李四\n': 2}
# obj3 = list(obj1)
print(obj1)
# print(obj3)
print(type(obj1))  #<class 'dict'>

obj2 = collections.Counter(ret4)  #统计文件2中
# print(obj2)
obj2 = dict(obj2)
print(obj2)   #{'张三\n': 1, '王五\n': 1, '李四\n': 1}
# print(type(obj2))

# count = 0
# for i in ret3:
#     # print(i.strip())
#     if i == li1[0]:
#         count+=1
# print("文件1张三出现次数",count)
#
# count2 = 0
# for i in ret3:
#     # print(i.strip())
#     if i == li1[-1]:
#         count2+=1
# print("文件1王五出现次数",count2)
#
#
# count3 = 0
# for i in ret4:
#     print(i.strip())
#     if i == li1[0]:
#         count3+=1
# print("文件1张三出现次数",count3)
#
# count4 = 0
# for i in ret4:
#     # print(i.strip())
#     if i == li1[-1]:
#         count4 += 1
# print("文件2王五出现次数",count4)


for i in li1:
    # print(i.strip())
    if i in obj1:
        print("文件1中，%s出现的次数%s"% (i.strip(),obj1[i]))  #strip去掉换行\n

for i in li1:
    # print(i.strip())
    if i in obj2:
        print("文件2中，%s出现的次数%s"% (i.strip(),obj2[i]))  #strip去掉换行\n


for i in obj1:#遍历字典
    if i in obj2: #如果字典1的键在字典2中，直接就判断了交集
        if obj2[i] > obj1[i]:
            print("%s在两个文件出现的差值是%s" % (i,obj2[i] - obj1[i]))
        else:
            print("%s在两个文件出现的差值是%s" % (i.strip(),obj1[i] - obj2[i]))





