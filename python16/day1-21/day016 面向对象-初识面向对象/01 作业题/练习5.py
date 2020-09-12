#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/30 17:59
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


class User:
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

class Account:
    def __init__(self):
        # user_list = []  #存放user对象  这个必须加上self变成成员变量才行
        self.user_list = []  #存放user对象   #注意点2：这里必须加self，表示成员变量（可以在方法间使用）

    def register(self): #1 注册功能，新建user对象
        print('欢迎来到注册页面')
        username = input('请输入你要注册的登录用户名:')
        password = input('请输入你要注册的登录密码:')
        u1 = User(username,password)  #新建对象，对象中封装正确的用户名和密码
        self.user_list.append(u1)  #self.user_list 表示成员变量（可以在方法间使用）
        # print(self.user_list) #[<__main__.User object at 0x00000098C5EDF0C8>]

    def login(self): #2 登录接口
        print('欢迎来到登录页面')
        n = 0
        for i in range(3):  #3次重试机会
            username2 = input('请输入你要登录的登录用户名:')
            password2 = input('请输入你要登录的登录密码:')
            for i in self.user_list:   #循环遍历用户对象  self.user_list表示成员变量（可以在方法间使用）
                if i.user == username2 and i.pwd == password2:  #关键点1 i.user取的是对象的属性
                    #i.user存的是期望结果   username2存的是用户登录输入的实际结果
                    print('登录成功')
                    # break  #注意点3  只能退出当层内循环
                    return  #注意点4  可以退出内层循环和外层循环
            else:  #2 这个else必须是和for同级，而不能是和if同级  关键点2
                #因为期望结果的每行判断完，才能说明登录失败
                n+=1
                print('登录失败，请重新输入,你还有 %s 次重试机会' % (3-n) )

    def run(self):#3 选择注册还是登录，先注册，后登录
        while 1:
            choice = input('请选择，1表示注册，2表示登录，Q表示退出:')
            if choice == '1':
                self.register()  #注意点1  方法前面必须加上self
            elif choice == '2':
                self.login()  #注意点1  方法前面必须加上self
            elif choice.upper() == 'Q':
                print('已经退出了')
                break
            else:
                print('你输入的不对，请重新输入')

a1 = Account()
a1.run()
'''
注册和登录的逻辑：
1、注册的时候，把正确的用户名和密码，比如：jack/123 存入数据库（或者对象中，列表中）
2、登录的时候，输入登录用户名和密码，拿用户输入的用户名和密码 和之前注册的用户名和密码进行比对
   如果相等匹配，就是登录成功
   如果不相等不匹配，就是登录失败

接口的概念：
1、接口可以对外提供服务，对外提供功能，接口是服务端
2、客户端-发起端发起请求，调用登录接口
    只需要传入正确的参数（用户名和密码），就可以登录成功
'''























