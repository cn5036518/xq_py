#!/usr/bin/env python
#-*- coding:utf-8 -*-

#输出5*5星号中的对角线

"""
思路：
1、2个for循环
2、一个判断条件
    i = j or i+j =4(左上角是原点，横轴是i 纵轴是j)
    左上角到右下角的线上的星号满足，i=j
    右上角到左下角的显示的星号满足，i+j=4
"""
# li = ["*","*","*","*","*"]

for i in range(5): #0-4  #这里的i是行数，换行5次
    for j in range(5):  #5-0 #这里的j是列数
        if i == j or i+j ==4:
            print("*",end=" ") #去掉换行
        else:
            print(" ",end=" ")
    print("") #解决换行
print("----------------1")

n=3
for i in range(n): #0-4  #这里的i是行数，换行5次
    for j in range(n,-1,-1):  #5-0 #这里的j是列数
        if i == j or i+j ==n-1:
            print("*",end=" ") #去掉换行
        else:
            print(" ",end=" ")
    print("") #解决换行
print("----------------100")

#输出三角形
# for i in range(5):  #0-4
#     for j in range(0, 5 - i): #4
#         print(end=" ")  #把换行符变成空格
#     for k in range(5 - i, 5): #4  #当i=0,第一行打印空白；当i=1，第二行打印一个$,当i=2，第三行打印$ $;当i=3，第四行打印$ $ $
#         #当i=4，第五行打印$ $ $ $
#         print("$", end=" ")
#     print("")  #换行 i是0-4 就换行5次

# 1输出直角三角形如下：这里第一行是空白
#
# $
# $ $
# $ $ $
# $ $ $ $
for i in range(5): #0-4
    for k in range(5 - i, 5):  # 4
        # 当i=0, 第一行打印空白；
        # 当i=1，第二行打印一个$,
        # 当i=2，第三行打印$ $;   #中间的空格就是end=" "
        # 当i=3，第四行打印$ $ $
        # 当i=4，第五行打印$ $ $ $
        print("$", end=" ") #这里的end默认是换行，这里改成空格
    print("") #换行 i是0-4 就换行5次
print("----------------1")

# 2输出直角三角形如下：这里第一行不是空白
# $
# $ $
# $ $ $
# $ $ $ $
for i in range(5): #0-4
    for k in range(5 - i-1, 5):  # 4
        # 当i=0, 第一行打印一个$；
        # 当i=1，第二行打印        $ $,
        # 当i=2，第三行打印        $ $ $;   #中间的空格就是end=" "
        # 当i=3，第四行打印$ $ $ $
        # 当i=4，第五行打印$ $ $ $ $
        print("$", end=" ") #这里的end默认是换行，这里改成空格
    print("") #换行 i是0-4 就换行5次












