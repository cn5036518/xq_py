#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3, 写代码完成99乘法表.(升级题)
# 1 * 1 = 1
# 2 * 1 = 2 2 * 2 = 4
# 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
# ......
# 8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64
# 9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81


for i in range(1,10): #1-9
    for j in range(1,i+1): # 3 关键点是i+1
        print('%s * %s= %s' % (i,j,i*j),end='  ')  #2内循环，end默认是换行，改成每次内循环换不换行，而是空格
        #4 格式化输出
    print()  #1每一个外循环后，就换行

'''
第一次外循环
i=1的时候，i+1=2 j只有1次内循环（取值1）   输出      1*1=1

第二次外循环
i=2的时候，i+1=3 j有2次内循环(依次取值1 2)  输出     2*1=2 2*2=4

第三次外循环
i=3的时候，i+1=4 j有3次内循环(依次取值1 2 3) 输出    3*1=3 3*2=6 3*3=9

第8次外循环
i=8的时候，i+1=9 j有8次内循环 输出    8*1=8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64

第9次外循环
i=9的时候，i+1=10 j有9次内循环 输出   9*1=9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81

规律：
第一个乘数i，进行外循环，取值从1-9
第二个乘数j 每次内循环，它的个数是变动的   j的取值是关键
    （i是1的时候，j是1个-取值是1，内循环1次）
    （i是2的时候，j是2个-取值是1和2，内循环2次）
    （i是3的时候，j是3个-取值是1和2和3，内循环3次）
'''











