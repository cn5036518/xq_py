#!/usr/bin/env python
#-*- coding:utf-8 -*-

#输出正方形的个数，例如：a*b  4*4的格子就有4*4+3*3+2*2+1*1个正方形
#当a=b的时候，下面的成立；a和b不相等的时候，下面的就不成立了
n = 0
a = 3
b = 3
for i in range(1,a+1):
    for j in range(1,b+1):
        if i == j:  #如果两个边相等的时候
            n = n+i*j   #累加
            print(n)
#第一次，0+1*1
#第二次，0+1*1+2*2
#第三次，0+1*1+2*2+3*3
#第四次，0+1*1+2*2+3*3+4*4
print(n)















