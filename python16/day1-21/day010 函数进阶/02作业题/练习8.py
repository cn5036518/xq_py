#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 8，写函数,接收两个数字参数,将较小的数字返回.
#方法1
def compare(num1,num2):
    if num1 < num2:
        return num1
    elif num2 < num1:
        return num2
n1 = 5
n2 = 4
ret = compare(n1,n2)
print(ret)
print('------------------1')

#方法2 三目运算 老师思路
def compare2(a,b):
    return a if a>b else b  #三目运算

a1 = 5
b1 = 4
ret2 = compare(a1,b1)
print(ret2)












