#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1输出直角三角形如下，第一行是空白
#
# $
# $ $
# $ $ $
# $ $ $ $

for i in range(5): #0-4
    for j in range(5-i,5):
        #i=0,第一行打印是空行
        #i=1，第二行打印是$
        #i=2,第三行打印是$ $
        #i=3,第四行打印是$ $ $
        #i=4,第五行打印是$ $ $ $
        print("$",end=" ") #这里的end默认是换行，这里用空格代替换行
    print("")  #i是0-4，就是换行5次
print("-----------1")

#2输出直角三角形如下，第一行不是空白
# $
# $ $
# $ $ $
# $ $ $ $
# $ $ $ $ $

for i in range(5): #0-4
    for j in range(5-i-1,5):
        #i= 0 ，第一行打印$
        #i=1,   第二行打印$ $
        #i=2,   第三行打印$ $ $
        #i=3,   第四行打印$ $ $ $
        #i=4,   第五行打印$ $ $ $ $
        print("$",end=" ") #这里的end默认是换行，这里变成空格
    print("") #i是0-4，换行5次












