#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
6，写函数，接收两个数字参数，返回比较大的那个数字。
'''

def get_a_bigger(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

n1 = 5
n2 = 6
ret = get_a_bigger(n1,n2)
print(ret)
print('------------------1')

#三目运算
a=10
b=20
d= 'jack'

c = a if a > b else b
# c = a if d.isalpha() else b   #
print(c)













