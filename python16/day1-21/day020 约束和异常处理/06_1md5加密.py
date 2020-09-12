#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/13 6:57

import hashlib

'''
思路
1、创建一个md5对象
2、把要加密的内容（字节）给到md5对象
3、获取密文
'''

#1 创建一个md5对象
obj = hashlib.md5()
# print(obj)  #<md5 HASH object @ 0x0000015B447075F8>

#2 把要加密的内容（字节）给到md5对象
obj.update('你好'.encode('utf-8'))   #必须把字符串转换成字节
# print(obj)

#3 获取密文
val = obj.hexdigest()
print(val)  #7eca689f0d3389d9dea66ae112e5cfd7
print('------------------------------------------------1 不加盐')


#1 创建一个md5对象
obj = hashlib.md5(b'hahahfjajfda')   #这里小括号里面就是 加盐，字节形式
# print(obj)  #<md5 HASH object @ 0x000001D0E1667620>

#2 把要加密的内容（字节）给到md5对象
obj.update('你好'.encode('utf-8'))   #必须把字符串转换成字节
# print(obj)

#3 获取密文
val = obj.hexdigest()
print(val)  #2bd9a3ce4d49765e7d16a05dc89779b9
print('------------------------------------------------2 加盐')

'''
为什么会引入加盐？
1、md5的加密不可逆，但是可以通过撞库穷举的形式破解
   比如 字符串'你好'的md5的加密后固定就是  7eca689f0d3389d9dea66ae112e5cfd7
2、这时候，加盐后，就无法通过撞库穷举破解了
   盐的长度越长，破解难度越大
'''











