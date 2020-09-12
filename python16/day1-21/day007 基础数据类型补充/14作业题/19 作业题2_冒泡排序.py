#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一 冒泡算法   推荐  好理解  内循环-两两比对
li1 = [9,1,3,2,5,8,7]
for j in range(len(li1)):
    # for i in range(len(li1)-1): #注意点1：这里如果不是-1，后面li1[i+1]就会出现索引越界
    for i in range(len(li1)-1-j): #注意点1：这里如果不是-1，后面li1[i+1]就会出现索引越界
        #注意点2： len(li1)-1-j  这里的-j是优化步骤（提升性能，优化时间复杂度），
        # 因为第一次外循环后，最大数在最右边（最大数在第二次外循环，是不用再两两比较的）
        #    第二次外循环后，次大数在右边倒数第二的位置 （次大数在第三次外循环，是不用再两两比较的）
        #    。。。以此类推
        if li1[i] > li1[i+1]: #1 内循环，相邻数两两比对，大的数放右边
            li1[i],li1[i+1] = li1[i+1],li1[i] #2 交换位置
    # print(li1)  #[1, 3, 2, 5, 8, 7, 9]
print(li1)  #[1, 2, 3, 5, 7, 8, 9]
"""
内循环：
第一次内循环，索引号是0和索引号是1两个位置上的数，进行相邻数两两比较，大的数换到右边
第二次内循环，索引号是1和索引号是2两个位置上的数，进行相邻数两两比较，大的数换到右边
第三次内循环，索引号是2和索引号是3两个位置上的数，进行相邻数两两比较，大的数换到右边
。。。

外循环：
第一次外循环，把最大数9放在了最右边
第二次外循环，把次大数8放在了右边倒数第二的位置
...
第n次外循环，把最小数留在了最左边
"""
print("----------冒泡")

#二 冒泡内循环
li1 = [9,1,3,2,5,8,7]
for i in range(len(li1) - 1):  # 注意点1：这里如果不是-1，后面li1[i+1]就会出现索引越界
    # 注意点2： len(li1)-1-j  这里的-j是优化步骤（提升性能），
    # 因为第一次外循环后，最大数在最右边（最大数在第二次外循环，是不用再两两比较的）
    #    第二次外循环后，次大数在右边倒数第二的位置 （次大数在第三次外循环，是不用再两两比较的）
    if li1[i] > li1[i + 1]:  # 1 内循环，相邻数两两比对，大的数放右边
        li1[i], li1[i + 1] = li1[i + 1], li1[i]  # 2 交换位置
print(li1)  #[1, 3, 2, 5, 8, 7, 9]
print("----------冒泡 内循环")
















