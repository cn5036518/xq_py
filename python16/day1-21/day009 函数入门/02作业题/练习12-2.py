#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 12，写一个函数完成注册功能(升级题)

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
#一 注册函数
#方法1
def register(username1,pwd1):
    with open('002.txt',mode='a+',encoding='utf-8') as f:  #可追加可读
        # print(f.tell())  #a+下，光标在文件末尾
        f.seek(0)  #回到文件开头
        li1 = []  #定义空列表
        for i in f: #1遍历循环文件
            # print(i)
            name,pwd = i.strip().split('|')  #2拆分用户名和密码，分隔符是'|'
            # print(name)
            li1.append(name)  #3把文件中已有的用户名存入列表
        # print(li1)
        if username1 not in li1: #4判断是否在已经存在的用户名列表 （如果用户名很多几千万，这个列表就很大） 改进点
            f.write(username1+'|'+pwd1+'\n')  #5不在的话，就写入用户名和密码到文件（数据库），提示注册成功或者返回True
            f.seek(0)
            s1 = f.read()
            print(s1)
            # print('注册成功')
            return True
        else: #6如果在的话，就提示用户或者返回False
            # print('对不起，你的用户名已经存在，请重新输入')
            return False

# username1 = 'jack2'
# pwd1 = '123'
# # username1 = input('请输入用户名:')
# # pwd1 = input('请输入密码:')
# ret = register(username1,pwd1)
# if ret:
#     print('注册成功')
# else:
#     print('对不起，你的用户名已经存在，请重新输入')

'''
方法2思路
1、判断用户输入的用户名是否在文件中（数据库），在的话，提示用户名已经存在
2、不在的话，将用户名和密码写入到文件末尾（数据库新插入一行）
'''

#方法2 老师思路--推荐
def register2(username,password): #参数是用户注册时输入的用户名和密码
    with open('register.txt',mode='r+',encoding='utf-8') as f: #1读写模式
        for i in f: #2遍历循环文件
            if i == '':  #3应对最后的空行
                continue  #跳出当次小循环（continue之后的代码不执行），进入下一次小循环
            name,pwd = i.split('|') #4分隔符是'|'拆分每一行的用户名和密码
            if username == name: #5如果用户输入的用户名和文件中的用户名相等
                print("用户名已经存在，请重新输入")
                return False
        f.write(username+'|'+password+'\n')   #6末尾添加一个换行
        #注意点：register.txt这个文件中的最后一行需要是空行，否则执行2次就会报错
        #注意点2：上面这行在for循环结束后，写入用户输入的用户名和密码
        #而不能写在for循环之中     #关键点
        print('用户注册成功')
        return True

# username1 = 'bob2'
# pwd1 = '123'
# # # username1 = input('请输入用户名:')
# # # pwd1 = input('请输入密码:')
# register2(username1,pwd1)  #调函数

'''
登录函数思路
1、用户输入登录用户名和密码
2、和文件中正确的用户名和密码进行匹配
3、如果匹配到了，提示登录成功
4、如果没有匹配到，提示用户名或者密码错误
'''

#二 登录函数
#方法1 单次登录
def login(user,pwd):
    with open('register.txt',mode='r',encoding='utf-8') as f:
        for i in f:
            name,password = i.strip().split('|')  #注意点：文件中密码后面有换行符，必须去掉，
            # 否则正确的用户名和密码也无法登录
            if user == name and pwd == password:
                print('登录成功')
                return True
        else:
            print('用户名或者密码错误，请重新输入。')
            return  False
# # username2 = 'jack2'
# # pwd2 = '123'#
# username2 = input('请输入用户名:')
# pwd2 = input('请输入密码:')
# login(username2,pwd2)

#方法2 3次登录机会
def login2(user,pwd):  #参数是用户输入的登录用户名和密码
    with open('register.txt',mode='r',encoding='utf-8') as f:
        for i in f:
            if i.strip() == user+'|'+pwd: #注意点1：i必须去掉两端的空白（包括换行），否则不对
                #注意点2：用户输入的用户名和密码用'|'进行连接
                return True
        else:  #else必须写在for外面
            return False

for i in range(2,-1,-1): #2,1,0一共3次输入机会
    username2 = input('请输入用户名:')
    pwd2 = input('请输入密码:')
    ret = login2(username2,pwd2)
    if ret:
        print('登录成功')
        break  #跳出整个循环
    else:
        print('用户名或者密码错误，你还有 %s 次输入机会'% i)






