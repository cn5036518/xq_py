#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1输出1-9，7除外
#方法1： for
# for i in range(1,10):  #推荐1 直接
#     if i!=7:  #直接法
#         print(i)

# for i in range(1,10):  #推荐2 简洁
#     if i ==7 :
#         continue  #跳出当次循环，进入下一次循环
#     print(i)  #for循环自增1

#方法2  while
# count=1
# while count<=9:
#     if count!=7: #直接法
#         print(count)
#     count+=1

# count=1
# while count<=9:
#     if count ==7:
#         count+=1  #注意：这里必须添加，否则到了7，就死循环了，因为continue后，最后一行的count+=1不执行了
#         continue  #跳出当次循环，进入下一次循环
#     print(count)
#     count+=1

# count=0
# while count<9:
#     count+=1  #在前面自增1，就避免了continue后，没有自增1，从而死循环的情况
#     if count ==7:
#         continue  #跳出当次循环，进入下一次循环
#     print(count)

#2 计算 1-2+3-4+5-6+...-98+99的值
"""
思路1：
1、计算1-99之间，奇数累加
2、计算1-99之间，偶数累减

思路2：
1、计算1-99之间，奇数累加a
2、计算1-99之间，偶数累加b
3、a-b

思路3：
1、计算1-99之间，奇数累加a
2、计算-2到-98之间，负偶数累加b
3、a+b
"""

# 思路1：
# 1、计算1-99之间，奇数累加
# 2、计算1-99之间，偶数累减
# sum = 0
# for i in range(1,100):
#     if i%2 ==1: #判断奇数
#         sum = sum+i  #累加 这里不用sum+=1是为了更好理解
#         #sum第一次取值是0，第二次取值是0+1，第三次取值是0+1+3，第四次取值是0+1+3+5
#         # print(i)  #1,3,5，---99
#     else: #如果是偶数
#         sum = sum-i #累减
#         #sum第一次取值是0+1-2，第二次取值是0+1-2+3-4,第三次取值是0+1-2+3-4+5-6
# print(sum)  #50

# 思路2：
# 1、计算1-99之间，奇数累加a
# 2、计算1-99之间，偶数累加b
# 3、a-b
sum_odd = 0
sum_even =0
for i in range(1,100):
    if i%2 ==1:#如果是奇数
        sum_odd = sum_odd +i #奇数累加
        #sum_odd第一次取值是0，第二次取值是0+1,第三次取值是0+1+3
    else:#如果是偶数
        sum_even = sum_even+i #偶数累加
        #sum_even第一次取值是0，第二次取值是0+2，第三次取值是0+2+4
print(sum_odd-sum_even)  #50











