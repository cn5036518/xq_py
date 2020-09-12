#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/6 7:15
#@author:wangtongpei

''''''
'''
二分法
1、核心思想
    掐头去尾取中间（中位数）
2、前置条件
    已经完成了排序（升序或者降序）

二分法查找：
方法1：循环+左右边界位置变动（两者之差减半）
        --可以知道目标数在列表中的位置
方法2：递归+新产生列表（新列表长度减半）
        --无法知道目标数在列表中的位置
方法3：递归+左右边界位置变动（两者之差减半）
'''

# 方法1：循环 + 左右边界位置变动（两者之差减半）
# --可以知道目标数在列表中的位置
def find(n1,li1):
    left = 0
    right = len(li1)-1
    while left <= right:
        mid = (left+right)//2 #左右边界在变动，中位数就在变动
        if n1 < li1[mid]:
            right = mid - 1
        elif n1 > li1[mid]:
            left = mid + 1
        else:
            index1 = li1.index(n1)
            print('%s 找到了，目标数在列表的下标是 %s' % (n1,index1))
            break #跳出整个循环
    else:
        print('目标数 %s 没找到' % n1)
n1 = 3
li1 = [1,2,3,4,5]
find(n1,li1)
#3 找到了，目标数在列表的下标是 2
print('------------------------1 循环')

# 方法2：递归 + 新产生列表（新列表长度减半）
# --无法知道目标数在列表中的位置，因为每次都新产生一个列表
def recursion1(n2,li2):
    left = 0
    right = len(li2) - 1
    if left <= right:
        mid = (left+right)//2
        if n2 < li2[mid]:
            li21 = li2[:mid-1]
            return recursion1(n2,li21)  #注意点1：必须加上return  递归入口
        elif n2 > li2[mid]:
            li21 = li2[mid+1:]
            return recursion1(n2, li21)
        else:
            print('目标数 %s 找到了' % (n2))
    else:
        print('目标数 %s 没找到' % n2)
        #隐含一个return None  递归出口
n2 = 4
li2 = [1,2,3,4,5]
recursion1(n2,li2)
print('------------------------2 递归+ 新产生列表')

# 方法3：递归 + 左右边界位置变动（两者之差减半）
def recursion2(n3,li3,left,right):
    if left <= right:
        mid = (left+right)//2
        if n3 < li3[mid]:  #注意点1：这里小于号坐标是目标数，而不是left
            right = mid -1
            return recursion2(n3,li3,left,right)  #注意点：return加上
        elif n3 > li3[mid]:
            left = mid + 1
            return recursion2(n3, li3, left, right)
        else:
            index1 = li3.index(n3)
            print('%s 找到了，目标数在列表的下标是 %s' % (n3, index1))
            return True
    else:
        print('目标数 %s 没找到' % n3)
        return False
n3 = 5
li3 = [1,2,3,4,5]
left = 0
right = len(li1)-1
recursion2(n3,li3,left,right)
#5 找到了，目标数在列表的下标是 4
print('------------------------3 递归+左右边界位置变动')













