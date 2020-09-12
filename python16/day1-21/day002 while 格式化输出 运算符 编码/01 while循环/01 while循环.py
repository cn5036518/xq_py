#!/usr/bin/env python
#-*- coding:utf-8 -*-

count = 1  #初始值   count作用：计数，控制循环范围
while count <= 3:  #打印10次
    print(count)   #打印1-3
    count += 1  #自增1
# else:  #当条件为假的时候，执行else
#     print("hi")
print("hi")

for i in range(3):  #0,1,2   #推荐  简洁
    print(i+1)  #打印1-3
else:  #当条件为假的时候，执行else
    print("hello")


#计算1+2+3+。。。+100的和    --累加
count =1
sum = 0  #这里的sum存放最终的结果
while count<=100:
    sum = sum+count  #第二个数是count（当前数）   第一个数是上一次循环中2个数的和    累加
    #sum首次是0  sum第二次是0+1  sum第三次是0+1+2  sum第四次是0+1+2+3 sum第五次是0+1+2+3+4
    # 注意：sum的值用表达式来表示，不要算出来，一旦算出来成一个数（比如：0+1+2=3），这个3就不好分析
    # print(count)
    count+=1  #自增1
print(sum)  #5050

sum = 0
for i in range(100):  #推荐 简洁   i是0-99  i+1就是1-100
    sum = sum + i+1  #这里的i+1就是count（当前数）  sum就是上一次循环中2个数的和   累加
    # sum首次是0  sum第二次是0+1  sum第三次是0+1+2  sum第四次是0+1+2+3 sum第五次是0+1+2+3+4
    # print(i+1)
print(sum)  #5050    #这里的sum存放最终的结果

"""
思路
1+2=3+3=6+4=10+5=15
从3+3开始
第二个数就是count   3,4,5    count+=1
第一个数是前面2个数的和       sum = sum+count  #这里的第二个数就是count （3，4,5...）
#     第一个数sum是前面2个数的和

"""

#计算2+3+。。。+100的和
count =1
sum = -1
while count<=100:
    sum = sum+count  #第二个数是count   第一个数是前面2个数的和
    # print(count)
    count+=1
print(sum)  #5049

#计算2+3+。。。+99的和
count =1
sum = -1
while count<=99:
    sum = sum+count  #第二个数是count   第一个数是前面2个数的和
    # print(count)
    count+=1
print(sum)  #4949
print("-------------1")

#计算1+2+。。。+100的和   累加
#while写法
count =1
sum=0   #存放最终的值
while count<=100:
    # print(count)
    sum =sum +count  #第二个数是count   1-100  第一个数是前面一次循环2个数的和
    #sum的取值第一次0+1 第二次0+1+2 第三次0+1+2+3  第四次 0+1+2+3+4
    count+=1
print(sum)  #5050

#计算1+2+。。。+100的和   累加
#for写法
sum =0 #存放最终结果和
for i in range(100): #0-99
    # print(i+1)  #1-100
    sum = sum + i+1   #i+1就是count 1-100
  # sum的取值：第一次0+1 第二次0+1+2 第三次0+1+2+3
print(sum)  #5050








