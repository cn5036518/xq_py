#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/30 7:41

li1 = []
li1.insert(1,'jack')  #这个是列表的内置方法，支持的
print(li1)


def method_name():
    li3 = []
    li3[0] = 'jack'  # 这个是字典的写法，列表不支持这个写法
    print(li3)  # IndexError: list assignment index out of range


method_name()





















