#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/4 7:26
#@author:wangtongpei


li1 = [1,2,3,4,5]
print(li1[1+1:])  #冒号的优先级高于+


def recursion1(n, li):
    left = 0
    right = len(li) - 1
    if left <= right:
        mid = (left + right)//2
        if n > li[mid]:
            li2 = li[mid+1:]
            return recursion1(n, li2)
        elif n < li[mid]:
            li2 = li[:mid]
            return recursion1(n, li2)
        else:
            print("刚刚好, 在这里出现了")
            return True
    else:
        return False

li1 = [1, 1, 1, 1, 2, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 8, 9, 16, 32, 44, 55, 78, 89]
ret = recursion1(88, li1)
print(ret)










