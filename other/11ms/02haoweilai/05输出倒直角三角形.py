#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1输出倒直角三角形如下，第一行不是空白
# $ $ $ $
# $ $ $
# $ $
# $
for i in range(4):
    for j in range(i,4):
        #0-3 4个$
        #1-3 3个$
        #2-3 2个$
        #3   1个$
        print("$",end =" ") #end默认是换行符，这里是空格
    print("")  #0-3 换行4次














