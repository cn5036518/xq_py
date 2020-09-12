#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/24 8:03
#@author:wangtongpei

# path1 = r'D:\Program\JetBrains\PycharmProjects\xq_py\全栈16\001\005.py'
path1 = r'..\003.py'   #相对路径  上一级目录

f = open(path1,mode='r',encoding='utf-8')
ret1 = f.read()
print(ret1)
print('-------------1')

path2 = r'..\..\005.py'   #相对路径  上上级目录

f = open(path2,mode='r',encoding='utf-8')
ret2 = f.read()
print(ret2)
print('-------------2')













