#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
题目：
统计2个文件中，都出现的姓名；
并且统计都出现姓名的次数；
计算2个文件，都出现姓名的次数的差值
"""
"""
思路：
1、将文件1的每一行作为元素，读取到列表1中
2、通过集合包中counter统计列表1中每个元素出现的次数 转换成字典dic1

3、将文件2的每一行作为元素，读取到列表2中
4、通过集合包中counter统计列表2中每个元素出现的次数 转换成字典dic2

5、遍历字典dic1
    判断如果i在dic2中，则打印i在文件1中出现的次数dic1[i]
        打印i在两个文件2中出现的次数dic2[i]
        打印i在两个文件中出现的次数差值dic1[i]-dic2[i]

注意点：
如果字典1的键在字典2中，直接就等于是交集

"""


#1导包
import collections

#2指定文件路径
path1 = r"D:\xq_py\11gd\01gd\001.txt"
path2 = r"D:\xq_py\11gd\01gd\002.txt"

#3将文件1中每一行作为元素读取到列表1中
file_obj1 = open(path1,encoding="utf-8")  #参数2是用来处理乱码的
ret3 = file_obj1.readlines()
set1 = set(ret3)
# print(ret3)  #['张三\n', '张三\n', '李四\n', '李四\n', '王五']

#4将文件2中每一行作为元素读取到列表2中
file_obj2 = open(path2,encoding="utf-8")
ret4 = file_obj2.readlines()
set2 = set(ret4)  #列表转换成集合  去重
# print(ret4)  #{'张三\n', '王五\n', '李四\n'}

set_jiaoji = set1 & set2
# li1 = list(set_jiaoji)

#5统计列表的每个元素出现的个数
obj1 = collections.Counter(ret3) #统计文件1中
obj1 = dict(obj1)  #counter转换成字典 {'张三\n': 2, '王五\n': 1, '李四\n': 2}

obj2 = collections.Counter(ret4)  #统计文件2中
obj2 = dict(obj2)

# for i in li1:#遍历交集列表
for i in set_jiaoji:#遍历交集集合  #这里遍历交集和遍历列表都可以
    if i in obj2 and i in obj1: #判断i是否同时在字典1和字典2中
        if obj2[i] > obj1[i]:
            print("%s在文件1出现的次数是%s" % (i.strip(), obj1[i]))
            print("%s在文件2出现的次数是%s" % (i.strip(), obj2[i]))
            print("%s在两个文件出现的差值是%s" % (i.strip(),obj2[i] - obj1[i]))  #正负数-保证差值是正数
        else:
            print("%s在文件1出现的次数是%s" % (i.strip(), obj1[i]))
            print("%s在文件2出现的次数是%s" % (i.strip(), obj2[i]))
            print("%s在两个文件出现的差值是%s" % (i.strip(),obj1[i] - obj2[i])) #正负数-保证差值是正数


"""
01gd  1用到了文件操作-读取行到列表1 列表2；
      2集合包的counter计算每个列表元素出现的次数--转换成字典1 字典2；
       3判断字典1的键是否在字典2的键中，在的话，打印键在两个字典中出现的差值dic1[i]-dic1[2]
        注意点：通过判断dic1[i]和dic1[2]的大小，保证差值是正数           --推荐 更简洁
03gd  1用到了文件操作-读取行到列表1 列表2；
      2列表1和列表2分别转换成集合set1 set2
      3两个集合取交集，得到set_jiaoji
      4集合包的counter计算每个列表元素出现的次数--转换成字典1 字典2；
      5遍历循环set_jiaoji，循环中判断i in dic1 and i in dic2  (是否同时在两个字典中)
      6在的话，打印键在两个字典中出现的差值dic1[i]-dic1[2]
        注意点：通过判断dic1[i]和dic1[2]的大小，保证差值是正数           --也可以，这里用到了列表转集合，取交集

"""


