#!/usr/bin/env python
#-*- coding:utf-8 -*-

#输出三角形如下  #第一行是空行
#
#   $
#  $ $
# $ $ $

for i in range(4):
    for j in range(0,4-i):
        #i=0 j是0-3  第一行打印4个空格
        #i=1 j是0-2  第二行打印3个空格
        #i=2 j是0-1  第三行打印2个空格
        #i=3 j是0    第四行打印1个空格
        print(end= " ")
    for k in range(4-i,4):
        #i=0 第一行打印一个空格
        #i=1 k是3    第二行打印$  （加上前面就是3个空格和一个$）
        #i=2 k是2-3，第三行打印$ $ （加上前面就是2个空格和$ $）
        #i=3 k是1-3，第四行打印$ $ $ （加上前面就是1个空格和一个$ $ $）
        print("$",end=" ")
    print("") #i是0-3 换行4次
print("-----------1")

#输出三角形如下  (第一行不是空行,第一列是空列)
#     $
#    $ $
#   $ $ $
#  $ $ $ $
for i in range(4):
    for j in range(i,4):        #4个空格,3个空格，2个空格，1个空格
        print(end=" ")
    for k in range(4-i-1,4):   #1个$，2个$,3个$,4个$
        print("$",end=" ")
    print("")   #换行    #i是0-3 换行4次
print("-----------2")

#输出三角形如下  (第一行不是空行,第一列不是空列)
#    $
#   $ $
#  $ $ $
# $ $ $ $
for i in range(4):
    for j in range(i+1,4):   #3个空格，2个空格，1个空格
        print(end=" ")
    for k in range(4-i-1,4): #1个$，2个$,3个$,4个$
        print("$",end=" ")
    print("") #换行














