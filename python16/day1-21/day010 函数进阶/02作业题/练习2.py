#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2,写函数，接收n个数字，求这些参数数字的和。（动态传参）

#方法1
def sum1(*args):  #注意点:这里的函数名不能是sum，因为sum是内置函数名字
    # print(args)  #(1, 2, 3, 4)
    a = sum(args)  #内置函数sum的参数是可迭代类型，返回的是参数的和
    print(a)  #10
li1 = [1,2,3,4] #输出列表中的所有元素-数字的和
sum1(*li1)  #10
print('--------------1')

#方法2  不用内置函数sum-老师思路
def sum2(*args):  #把多个位置参数打包聚合成元组
    # print(args)  #(1,2,3)  元组
    n = 0
    for i in args:
        n += i  #累加
    print(n)  #6
    return n  #6

li2 = [1,2,3]
ret2 = sum2(*li2) #把列表解构成多个位置参数  函数的返回值得到了，可以继续往下了
print(ret2) #6











