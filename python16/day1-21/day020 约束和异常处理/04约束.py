#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/2 8:31

''''''
'''
需求：
1、普通人登录贴吧-普通会员--程序员张三编写
2、吧务登录贴吧--管理员--李四编写
3、超级管理员登录--版主--王五编写
上述3个角色的人登录贴吧，输入验证码，进入主页

思路：
1、定义3个类，每个类是一个角色
   类的普通方法是登录方法
2、总的登录入口，一个总的登录方法
    参数是角色的对象
    角色的对象调用类中的普通方法
3、打印输入验证码
   进入主页
'''

class Normal:   #1 张三编写
    def login(self):
        print('普通会员登录')

class Member:  #2 李四编写
    def denglu(self):
        print('吧务登录')

class Admin:  #3 王五编写
    def login(self):
        print('管理员登录')

def logining(obj):  #4 架构师编写，参数是上述角色的对象
    obj.login()
    print('请输入验证码')
    print('欢迎登录主页')

#新建3个对象
n = Normal()
m = Member()
a = Admin()

#3 调登录入口，传入角色对象
logining(n)
# logining(m) #这里会报错，因为李四写的不是login，而是denglu
#AttributeError: 'Member' object has no attribute 'login'
logining(a)
print('===========================================1')

'''
需求2：
如何让张三、李四、王五都写统一的login方法呢？

思路：
1、新建一个父类
   父类里面写一个login方法
   该方法是主动抛出一个异常‘没有实现login方法’
2、张三、李四、王五继承父类
    子类必须重写父类的login方法，如果没有重写，子类就会抛出异常
'''

class Base:
    def login(self):   #这个约束在于，只要子类没有重写父类的login方法，就会主动抛出异常
        # raise Exception('没有实现login方法')
        raise NotImplementedError('没有实现login方法')  #专有的异常

class Normal2(Base):   #1 张三编写
    def login(self):
        print('普通会员登录')

class Member2(Base):  #2 李四编写
    def denglu(self):
        print('吧务登录')

class Admin2(Base):  #3 王五编写
    def login(self):
        print('管理员登录')

def logining(obj):  # 4 架构师编写，参数是上述角色的对象
    obj.login()
    print('请输入验证码')
    print('欢迎登录主页')

#新建3个对象
n2 = Normal2()
m2 = Member2()  #这里可以正常创建对象
a2 = Admin2()

#3 调登录入口，传入角色对象
logining(n2)
# logining(m2) #这里会报错，因为李四写的不是login，而是denglu
#NotImplementedError: 没有实现login方法
logining(a2)
print('===========================================2')











