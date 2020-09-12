#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/13 9:28

''''''
'''
需求：
1写一个参数，就不加盐；写2个参数，就加盐

思路：
不定参数来实现   *args 在形参位置处，*是把多个参数打包聚合成元组
在函数体中    写法是args，这个args是个元组  *args在函数体，是解包成元组的元素

方法1：位置参数+不定参数
方法2：不定参数

'''

import hashlib

#方法1   位置参数+不定参数
def md5_algorithm(password,*args):
    # print(*args)  #(b'234',)   #元组的元素
    # print(args)   #(b'234',)   #元组
    if len(args) > 0:  # 这里的args是元组，当不定参数的长度大于0
        obj = hashlib.md5(args[0])  # 创建一个md5对象,小括号里面是加盐，盐必须是字节
    else:  # 2 当不定参数长度是0
        obj = hashlib.md5()  # 创建一个md5对象,小括号里面是加盐，不写就是不加盐
    obj.update(password.encode('utf-8'))  # 把要加密的内容（字节）给到md5对象,必须把字符串转换成字节
    val = obj.hexdigest()  # 获取密文
    return val

#方法2  不定参数，通过判断元组的长度来进行逻辑判断
def md5_algorithm2(*args):
    # print(*args)  #(b'234',)   #元组的元素
    # print(args)   #(b'234',)   #元组
    if len(args) == 2:  # 这里的args是元组，当不定参数的长度大于0
        obj = hashlib.md5(args[1])  # 创建一个md5对象,小括号里面是加盐，盐必须是字节
    elif len(args) == 1:  # 2 当不定参数长度是0
        obj = hashlib.md5()  # 创建一个md5对象,小括号里面是加盐，不写就是不加盐
    obj.update(args[0].encode('utf-8'))  # 把要加密的内容（字节）给到md5对象,必须把字符串转换成字节
    val = obj.hexdigest()  # 获取密文
    return val

# ret = md5_algorithm2('123',b'234')   #bc4e71768c878be0e0636839756a8af0
ret = md5_algorithm2('123')            #202cb962ac59075b964b07152d234b70
print(ret)


















