#!/usr/bin/env python
#-*- coding:utf-8 -*-

#函数：对功能或者动作的封装
#登录验证函数（接口或者服务）
# 函数或者接口或者服务，都可以对外提供功能或者服务

#一、定义登录验证函数
def login(username,password):
    if username == 'alex' and password == '123':
        return True
    else:
        return False

#二、使用场景--调用登录验证函数
# name = input('请输入用户名:')
# pwd  = input('请输入密码：')
# if login(name,pwd):   #调用登录验证函数（接口，服务）
#     print("进入刘伟的空间")
# else:
#     print("用户名或者密码错误，请重新输入")

s1 = 'hello'
print(len(s1)) #5

#请写出len()这个内置函数的实现
#函数：对功能或者动作的封装
s1 = 'hello'

#1 定义函数
def my_len(arg):   #这里arg是形参
    count = 0
    for i in arg:
        count+=1
    # print(count)  #5
    return count
#2调用自定义函数
ret = my_len(s1)  #这里s1是实参
print(ret)  #5




