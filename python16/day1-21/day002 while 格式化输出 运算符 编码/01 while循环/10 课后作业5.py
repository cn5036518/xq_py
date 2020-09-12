#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 11.求1-2+3-4+5 ... 99的所有数的和.
# 先计算1+3+5+。。。+99
# 再计算2+4+。。。+98
# 再计算差

# #for写法
# sum = 0 #存放最后的和--结果
# for i in range(100):#0-99
#     # print(i)
#     if i%2==0:  #如果除以2的余数是0,说明是偶数,跳出当次循环,余下的就是奇数
#         continue
#     # print(i)
#     sum = sum + i
#     #sum第一次取值0 第二次取值0+1 第三次取值0+1+3 第四次取值0+1+3+5
# print(sum)  #2500
#
# sum_ou = 0
# for i in range(99):#0-98  #限定范围
#     # print(i)
#     if i%2==1:  #如果除以2的余数是1,说明是奇数,跳出当次循环,余下的就是偶数
#         continue
#     # print(i)
#     sum_ou = sum_ou + i
#     #sum第一次取值0 第二次取值0+2 第三次取值0+2+4 第四次取值0+2+4+6
# print(sum_ou)  #2450
#
# result = sum -sum_ou
# print(result)  #50

#for写法--优化版
sum_ji=0
sum_ou=0
for i in range(100):  #0-99
    if i%2==1:
        sum_ji = sum_ji +i  #0-99的奇数的累加
    if i%2==0:
        sum_ou = sum_ou +i  #0-99的偶数的累加
print("0-99奇数的和",sum_ji)  #2500
print("0-99偶数的和",sum_ou)  #2450
print(sum_ji - sum_ou)  #50

# 求1-100之间所有的数的和
sum = 0
for i in range(100):#0-99 限定范围
    sum = sum +i+1
print(sum)  #5050

# 9.输出 1-100 内的所有奇数及奇数的和
sum = 0
for i in range(100):  #0-99
    if (i+1)%2==1:
        sum = sum+i+1
        # print(i+1)  #输出所有的奇数
print(sum)  #2500   输出所有的奇数的和

# 10.输出 1-100 内的所有偶数及偶数的和
sum = 0
for i in range(100):  #0-99
    if (i+1)%2==0:
        sum = sum+i+1
        # print(i+1)  #输出所有的偶数
print(sum)  #2550   输出所有的偶数的和
















