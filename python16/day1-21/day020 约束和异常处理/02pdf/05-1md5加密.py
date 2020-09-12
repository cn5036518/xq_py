#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 9:42

''''''
'''
需求：md5加密的基本算法、封装函数、加盐

思路：
1、导入hashlib模块
2、新建一个md5对象
3、把要加密的内容，转换成字节，给到md5对象
4、产生密文
'''

import hashlib

# 2、新建一个md5对象
obj = hashlib.md5()

# 3、把要加密的内容，转换成字节，给到md5对象
obj.update('jack'.encode('utf-8'))

# 4、产生密文
ciphertext = obj.hexdigest()
print(ciphertext)  #4ff9fc6e4e5d5f590c4f2134a8cc96d1
print('-------------------------------1 md5基础写法')

def md5_encrypt(s1):
    # 2、新建一个md5对象
    obj = hashlib.md5()

    # 3、把要加密的内容，转换成字节，给到md5对象
    obj.update(s1.encode('utf-8'))

    # 4、产生密文
    ciphertext = obj.hexdigest()
    print(ciphertext)

md5_encrypt('tom')  #34b7da764b21d298ef307d04d8152dc5
print('-------------------------------2 md5 封装函数')

def md5_encrypt_salt(s1):
    # 2、新建一个md5对象
    obj = hashlib.md5(b'jajdsaf')  #加的盐必须是字节，前面带b

    # 3、把要加密的内容，转换成字节，给到md5对象
    obj.update(s1.encode('utf-8'))

    # 4、产生密文
    ciphertext = obj.hexdigest()
    print(ciphertext)  #8c1ead344d4b6aad3c2c5546b7ddd5d9

md5_encrypt_salt('tom')  #34b7da764b21d298ef307d04d8152dc5
# md5_encrypt_salt('123')  #af46d775967e238894400a16338426b1
print('-------------------------------3 md5 加盐')














