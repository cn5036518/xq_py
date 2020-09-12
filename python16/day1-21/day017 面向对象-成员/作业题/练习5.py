#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/8 7:24
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
19.在昨天最后一题的基础上.把数据写入到文件中.并且注册的时候需要到文件中判断是否重
复.如果重复提示不能注册.(升级题
'''

# 16.	补充代码：实现用户注册和登录
# class User:
#     def __init__(self,user,pwd):
#         self.user = user
#         self.pwd = pwd

class Account:
    def __init__(self):
        # user_list = []  #存放user对象  这个必须加上self变成成员变量才行
        # self.user_list = []  #存放user对象   #注意点2：这里必须加self，表示成员变量（可以在方法间使用）

        #新建文件
        # self.f1 = open('acount.txt',mode='w+',encoding='utf-8')  #先w+  后a+  可写可读 每次都清空，覆盖
        self.f1 = open('acount.txt',mode='a+',encoding='utf-8')  #先w+  后a+   可追加可读
        #1 新建文件，文件对象存储成成员变量，方便方法间使用

    def register(self): #1 注册功能
        print('欢迎来到注册页面')
        username = input('请输入你要注册的登录用户名:')
        password = input('请输入你要注册的登录密码:')
        # u1 = User(username,password)  #新建对象，对象中封装正确的用户名和密码
        # self.user_list.append(u1)  #self.user_list 表示成员变量（可以在方法间使用）
        # print(self.user_list) #[<__main__.User object at 0x00000098C5EDF0C8>]

        #一、先判断用户名是否在文件中已经存在
        self.f1.seek(0, 0)  # 1光标到文件开头   关键点1
        #是在第二次运行程序的时候，判断用户名是否存在的时候，从历史注册用户名中进行查找、判断、去重
        for i in self.f1:  # 2 遍历文件对象，读取文件中每一行
            if username == i.split('|')[0]:#3 判断用户输入的用户名和文件中已经存在的用户名进行比对
                print('用户名已经存在')
                break  #4，如果已经存在，就跳出整个for循环
        else: #5 如果没有任何break 正常结束，执行else，如果有break，else下面就不会执行
        # 如果不写else，即使有break，下面的内容也会执行； 有没有else，在break的情况下，执行是完全不同的
            #6 往空白文件中写入用户名和密码
            self.f1.write(username+'|'+password+'\n')
            self.f1.flush()  #7 将写入的及时刷新到文件
            # self.f1.seek(0,0)  #光标到文件开头
            # self.f1.close()  #8 先不关闭,如果在这里关闭，就会报错
            #ValueError: I/O operation on closed file.

    def login(self): #2 登录接口
        print('欢迎来到登录页面')
        n = 0
        for i in range(3):  #3次重试机会
            username2 = input('请输入你要登录的登录用户名:')
            password2 = input('请输入你要登录的登录密码:')
            # for i in self.user_list:   #循环遍历用户对象  self.user_list表示成员变量（可以在方法间使用）
            self.f1.seek(0, 0)  # 1、光标到文件开头  关键点2
            #2 在用户输入用户名和密码登录的时候，需要从文件开头遍历已经注册的用户名和密码
            for i in self.f1:   #3 循环遍历文件对象  self.f1表示成员变量（可以在方法间使用）
                # if i.user == username2 and i.pwd == password2:  #关键点1 i.user取的是对象的属性
                if i.split('|')[0].strip() == username2 and i.split('|')[1].strip() == password2:  #
                    #4 strip()是为了去掉换行符
                    #5 把用户输入的用户名密码和文件中的用户名密码进行匹配
                    print('登录成功')
                    # self.f1.close()  #关闭文件  检查点
                    #ValueError: I/O operation on closed file.
                    # break  #注意点3  只能退出当层内循环
                    return  #注意点4  可以退出内层循环和外层循环(一次退出2层循环)
            else:  #6 这个else必须是和for同级，而不能是和if同级  关键点2
                #因为期望结果的每行判断完，才能说明登录失败
                n+=1
                print('登录失败，请重新输入,你还有 %s 次重试机会' % (3-n) )
        self.f1.close()  # 7关闭文件 注意这行代码的位置  关键点3

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
   保存之前，先判断用户名在文件中是否已经存在，如果重复提示不能注册
2、登录的时候，输入登录用户名和密码，拿用户输入的用户名和密码 和之前注册的用户名和密码进行比对
   如果相等匹配，就是登录成功
   如果不相等不匹配，就是登录失败
3、之前是将注册后的用户名和密码存在列表中--内存中
   现在需要存在文件中（类似于-持久化到数据库）

注意点：
1、光标的位置回到文件的开头
2、关闭文件对象的代码所在的位置

扩展：
1、能否把对象写入文件中--不能
   --文件中只能写入字符串，不能写入对象
2、先实现用户名|密码+换行符 写入文件
3、注册用户名去重--ok

接口的概念：
1、接口可以对外提供服务，对外提供功能，接口是服务端
2、客户端-发起端发起请求，调用登录接口
    只需要传入正确的参数（用户名和密码），就可以登录成功
'''














