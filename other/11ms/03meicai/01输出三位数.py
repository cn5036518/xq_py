#!/usr/bin/env python
#-*- coding:utf-8 -*-

#输出所有的三位数，要求123-987，即每个三位数，个十百位的数字都不相同，且首位不是0，122或者111或者012就不满足要求
#方法1： 每次只输出一个三位数满足要求
import random
li1 = [0,1,2,3,4,5,6,7,8,9]
first1 = random.randint(1,9)   #输出1-9的随机数，限定了首位不是0
# print(first1)

li1.remove(first1)  #从0-9的列表中，删除第一个数，从余下的9个数中，随机取一个
second1 = random.choice(li1) #参数是列表
# print(second1)

li1.remove(second1)  #从0-9的列表中，删除第一个数和第二个数，从余下的8个数中，随机取一个
third1 = random.choice(li1)
# print(third1)

print(first1*100 + second1*10 + third1)  #输出3个数字  --方式1
print(str(first1)+str(second1)+str(third1))  #输出3个数字，转换成字符串进行拼接   方式2和方式1结果等效

#方法2 #一次输出所有满足要求的三位数
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i!=j and j!=k and i!=k: #判断三位不同
                print(i,j,k,sep="",end=" ")
                # print(i,j,k)
                #这里sep默认是空格分割（分割的是前面的2个或者3个参数），这里从空格改成空白（此时就是拼接的作用）
                #end默认是\n换行，这里从换行改成空格

"""
 1输出三位数不同--3层for+print的（sep和end）--2个方法
"""







