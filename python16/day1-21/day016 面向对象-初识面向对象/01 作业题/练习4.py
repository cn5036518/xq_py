#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/30 8:24
#@author:wangtongpei
#@email: cn5036520@163.com

# 16.	补充代码：实现用户注册和登录
# class User:
#     def __init__(self,name,pwd):
#         self.name = name
#         self.pwd = pwd
#
# class Acount:
#     def __init__(self):
#         pass
#         self.user_list = []  #用户列表，数据格式[用户1，用户2，用户3]
#
#     def register(self):
#         pass
#         # 用户注册，动态创建user对象，并添加到self.user_list中
#
#     def login(self):
#         pass
#         #用户登录，用户输入用户名和密码，并去self.user_list中检查是否合法（即用户名和密码匹配）
#
#     def run(self):
#         pass
#         #先进行2次用户注册（注册2个用户名和密码），再进行用户登录（3次重试机会）
#
# if __name__ == '__main__':
#     a1 = Acount()
#     a1.run()

class User:  #用户类
    def __init__(self,name,pwd):  #用于把用户名和密码封装到用户这个对象
        self.name = name
        self.pwd = pwd

class Acount: #账户类
    def __init__(self,user_list): #1 形参是列表，用于存放用户对象（或者用户名和密码的元组）
        self.user_list = user_list  #用户列表，数据格式[用户1，用户2，用户3]

    def register(self,username,password): #注册方法
        # 注册方法，把用户输入的用户名和密码作为元组，存入到列表中
        # 列表的元素是元组，元组的元素是用户名和密码
        self.user_list.append((username,password))
        # 用户注册，动态创建user对象，并添加到self.user_list中
        print(self.user_list)  #[('jack', '123'), ('tom', '123')]  这里模拟数据库存在正确的用户名和密码

    def login(self):  #登录方法（也可以叫登录接口）
        #用户登录，用户输入用户名和密码（先写死，后写活），并去self.user_list中检查是否合法（即用户名和密码匹配）
        count = 0
        while 1:
            user1 = input('请输入用户名:')  #模拟用户的登录输入
            pwd1 = input('请输入密码:')

            u11 = User(user1,pwd1)  #1 登录时，将用户输入的用户名和密码封装到对象
            # print(u11)
            if (u11.name,u11.pwd) in self.user_list: #2 判断用输入的用户名和密码组成的元组是否和正确的用户名密码匹配
                print('登录成功')
                break  #3 登录成功，就退出整个while循环
            else:
                print('登录失败')
                print('你还有 %s 次登录机会' % (2-count))  #一共是3次重新登录机会
            count+=1
            if count == 3:
                print('3次登录机会用完了')
                break  #4 3次登录机会使用完了，就退出整个循环while

    def run(self):
        pass
        #先进行2次用户注册（注册2个用户名和密码），再进行用户登录（3次重试机会）

# if __name__ == '__main__':
#     a1 = Acount()
#     a1.run()

#1 创建2用户对象（用户名和密码）  用户注册 （注册成功后，把用户名和密码存在数据库）
u1 = User('jack','123')   #先写死
u2 = User('tom','123')    #1 把用户名和密码封装到用户这个具体对象

#2 创建2个账户对象，用户列表中是2个用户对象（用户名和密码）
user_list = []
a1 = Acount(user_list)
a1.register(u1.name,u1.pwd)  #第1次注册  参数是对象的用户名和密码，是否支持参数是对象呢？

a2 = Acount(user_list)
a2.register(u2.name,u2.pwd)  #第2次注册

# a1.login()
a2.login()   #调登录方法（判断用户输入的用户名和密码，和正确的用户名和密码是否匹配）  和上面行是等效的

'''
扩展：
1、目前用的是对象的用户名和密码进行登录成功的判断
     --列表的元素是元组，元组的元素是用户名和密码  是否可以变成列表的元素是对象（对象封装了用户名和密码）
   是否可以直接用对象进行登录成功的判断（把用户名和密码封装到1个对象中）

思路：
1、注册
    用户在注册的时候，用户输入用户名和密码，这个用户名和密码会存入到数据库（或者放列表-内存中）--（期望结果）
2、登录
    用户在登录的时候，会输入用户名和密码（实际结果），登录接口会拿到用户名输入的用户名和密码去数据库（或者列表-内存）
    中进行比对，如果用户名和密码都匹配，则登录成功
    如果用户名和密码不匹配，则登录失败
'''







