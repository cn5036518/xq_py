#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 9:58

''''''
'''
需求：
md5在登录校验密码的应用

思路：
1、用户注册的时候，输入用户名和密码的明文
    数据库存储用户名的密码，密码通过加密算法转换成密文后，存储在数据库
2、用户登录的时候，再次输入用户名和密码的明文
    程序将用户输入的用户名和数据库存在的明文用户名进行对比，
    同时将用户输入的密码明文通过md5加密算法加密后，将加密后的密码密文和数据库存储的密码密文进行对比。
    上述两个比对结果一致，则登录成功，否则，登录失败。
'''
import hashlib

def md5_encrypt(s1):
    obj = hashlib.md5(b'jajdsaf')   #加盐，字节
    obj.update(s1.encode('utf-8'))  #字符串需要转成字节
    ciphertext = obj.hexdigest()
    print(ciphertext)
    return ciphertext

username = input('请输入用户名:')
password = input('请输入密码:')

#假设数据库存储的用户名和密码密文是   tom  af46d775967e238894400a16338426b1(明文密码是123)
ciphertext = md5_encrypt(password)   #将密码的明文加密后，变成密码的密文

if username == 'tom' and ciphertext == 'af46d775967e238894400a16338426b1':
    print('登录成功')
else:
    print('登录失败')

'''
用户名：tom
密码明文：123
密码密文：af46d775967e238894400a16338426b1（明文密码123通过md5加密算法-加盐后的密文密码，存储在数据库中）
'''











