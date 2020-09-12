#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 12，先注册后登录

'''
'''

'''
思路--不校验用户名是否已经存在于数据库
1、用户输入用户名
2、用户输入密码
3、将用户输入的用户名和密码追加到文件中（模拟数据库用户表增加了一条记录）
   用户注册成功

扩展一下功能--校验用户名是否存在于数据库，如果存在，就需要换一个用户名；如果不存在，就可以使用
1、用户输入用户名后
2、拿这个用户名和文件中的数据  jack|123 进行比对，如果文件没有，说明用户名可用
3、用户输入密码
4、将用户输入的用户名和密码追加到文件中（模拟数据库用户表增加了一条记录）
   用户注册成功

步骤：
1、先写注册功能3
2、然后转换成注册函数4

1、用户名和密码先写死1
2、再换成input输入2
'''

#一、注册函数
def register(username1,pwd1):
    f = open('002.txt',mode='a+',encoding='utf-8')
    # print(f.tell())  #a+下，光标在文件末尾
    f.seek(0)  #回到文件开头
    li1 = []  #定义空列表
    for i in f:
        # print(i)
        name,pwd = i.strip().split('|')  #拆分用户名和密码，分隔符是'|'
        # print(name)
        li1.append(name)  #把文件中已有的用户名存入列表
    # print(li1)
    if username1 not in li1: #判断是否在已经存在的用户名列表
        f.write(username1+'|'+pwd1+'\n')  #不在的话，就写入用户名和密码到文件（数据库），提示注册成功或者返回True
        f.seek(0)
        s1 = f.read()
        print(s1)
        # print('注册成功')
        return True
    else: #如果在的话，就提示用户或者返回False
        # print('对不起，你的用户名已经存在，请重新输入')
        return False
    f.close()

# username1 = 'jack2'
# pwd1 = '123'
# # username1 = input('请输入用户名:')
# # pwd11 = input('请输入密码:')
# ret = register(username1,pwd1)
# if ret:
#     print('注册成功')
# else:
#     print('对不起，你的用户名已经存在，请重新输入')

'''
登录函数思路
1、读取文件（数据库）中的用户名和密码
2、拿用户输入的用户名和密码和文件中的正确的用户名和密码比对
3、如果相等，就是登录成功
4、如果不相等，就是用户名或者密码错误

步骤：
1、先单次登录
2、后3次登录机会

'''

#二、登录函数
def login1(user,pwd): #
    with open('register.txt',mode='r',encoding='utf-8') as f:  #只读
        for i in f: #1 遍历循环文件对象
            name,password = i.strip().split('|') #2 分隔符'|'拆分文件中的用户名和密码
            if user == name and pwd == password: #3 用户输入的用户名和密码和文件中的完全匹配
                return True   #
        else: #注意点：必须放在for循环之外
            return False

for i in range(2,-1,-1):  # 2 1 0   #一共是3次登录机会
    username1 = input("请输入用户名:")  # 用户的自定义输入
    password1 = input("请输入密码:")
    ret = login1(username1,password1) #实参是用户输入的用户名和密码
    if ret:
        print("登录成功")
        break
    else:
        print('用户名或者密码错误，请重新输入，你还有 %s 次输入机会' % i)










