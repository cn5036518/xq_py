#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
12，写一个函数完成三次登录功能
'''

'''
思路：
步骤：
1、先写死用户名和密码，
2、然后用input

1、先写三次登录
2、然后转换成三次登录函数
'''

def login1(user,pwd): #参
    with open('register.txt',mode='r',encoding='utf-8') as f:
        for i in f:
            name,password = i.strip().split('|')
            if user == name and pwd == password:
                return True   #
            else:
                return False

for i in range(2,-1,-1):
    username1 = input("请输入用户名:")  # 用户的自定义输入，
    password1 = input("请输入密码:")
    ret = login1(username1,password1) #实参是用户的自定义输入
    if ret:
        print("登录成功")
        break
    else:
        print("用户名或者密码错误，你还有 %s 次输入机会" % i)





