#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/1 17:32
#@author:wangtongpei
#@email: cn5036520@163.com

def add(a,b):
    if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
        return a+b
    else:
        print('请输入数字或者小数')
        # raise   #抛出异常

print(add(1,2))   #3
print(add(1.2,2))  #3.2
print(add(-1,2))   #1
print(add('哈哈',2))   #请输入数字或者小数











