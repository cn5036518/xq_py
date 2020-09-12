#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/5 10:29
#@author:wangtongpei

#二分法查找
#方法1 循环+左右边界变动，两者差减半
#方法2 递归+新列表长度减半
#方法3 递归+左右边界变动，两者差减半

#方法1 循环+左右边界变动，两者差减半
def recursion1(n1,li1):  #1 简洁  推荐
    left = 0
    right = len(li1)-1
    while left <= right:
        mid = (left + right) // 2
        if n1 < li1[mid]:
            right = mid -1
        elif n1 > li1[mid]:
            left = mid + 1
        else:
            print('%s 找到了' % n1)
            break
    else:
        print('%s 没找到' % n1)
        return False
n1 = 3
li1 = [1,2,3,4,5]
recursion1(n1,li1)
print('--------------------1 二分法 循环-左右边界变动，两者差减半')

#方法2 递归+新列表长度减半
def recursion2(n2,li2):
    left = 0
    right = len(li2)-1
    if left <= right:
        mid = (left + right) // 2
        if n2 < li2[mid]:
            li3 = li2[:mid-1]
        elif n2 > li2[mid]:
            li3 = li2[mid+1:]
        else:
            print('%s 找到了' % n2)
            return True
        return recursion2(n2,li3)  #注意点：递归的条件：列表在变
    else:
        print('%s 没找到' % n2)
        return False
n2 = 4
li2 = [1,2,3,4,5]
recursion2(n2,li2)
print('--------------------2 二分法 递归-新列表长度减半')

#方法3 递归+左右边界变动，两者差减半
def recursion3(n3,li3,left,right):
    if left <= right:
        mid = (left + right) // 2
        if n3 > li3[mid]:
            left = mid + 1
        elif n3 < li3[mid]:
            right = mid - 1
        else:
            print('%s 找到了' % n3)
            return True
        return recursion3(n3,li3,left,right) #注意点：递归的条件：左右边界在变
    else:
        print('%s 没找到' % n3)
        return False
n3 = 5
li3 = [1,2,3,4,5]
left = 0
right = len(li3)-1
recursion3(n3,li3,left,right)
print('--------------------3 二分法 递归-左右边界变动，两者差减半')

'''
递归的小结：
1、找到持续在变化-动的东西（找到规律）
    1、比如：每次产生一个新列表（列表长度减半）
    2、比如：每次左右边界位置都在变（两者之差减半）
2、递归就写出来了

二分法小结：
1、核心思想：
    掐头去尾取中间，一种在和中间值（中位数）比较
2、前提：
    必须有序

冒泡排序小结
1、核心思想
    交换-换位置

数据结构+算法=计算机
'''













