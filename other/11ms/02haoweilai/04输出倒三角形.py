#!/usr/bin/env python
#-*- coding:utf-8 -*-

#输出倒三角形如下  (第一行不是空行,第一列不是空列)
# $ $ $ $
#  $ $ $
#   $ $
#    $

for i in range(4):
    for j in range(4-i,4):
        print(end=" ")
        #    0个空格
        #3   1个空格
        #2-3 2个空格
        #1-3 3个空格
    for k in range(i,4):
        print("$",end=" ")
        #0-3 4个$
        #1-3 3个$
        #2-3 2个$
        #3   1个$
    # print("") #0-3 4个换行
    print() #0-3 4个换行














