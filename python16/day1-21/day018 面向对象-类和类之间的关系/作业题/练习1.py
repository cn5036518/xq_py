#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/24 6:02
#@author:wangtongpei
#@email: cn5036520@163.com

#1 看代码写结果
class F3:
    def f1(self):
        ret = super().f1()
        print(ret)
        return 123

class F2:
    def f1(self):
        print('123')

class F1(F3,F2):  #继承2个类，没明白？--nok
    pass

obj = F1()
obj.f1()
print('-----------------------练习1')

#2 看代码写结果
class F1:
    def __init__(self,a1):
        self.a1 = a1
    def f2(self,arg):
        print(self.a1,arg)

class F2(F1):
    def f2(self,arg):
        print('666')

obj_list = [F1(1),F2(2),F2(3)]
# for obj in obj_list:
#     obj.f2()  #报错，f2方法缺少参数arg
    #        TypeError: f2() missing 1 required positional argument: 'arg'
    # item.f2()
print('-----------------------练习2')

#4 看代码写结果
class F1:
    def __init__(self,num):
        self.num = num

    def func(self,request):
        print(self.num,request)

    def run(self):
        self.func(999)

class F2(F1):
    def func(self,request):
        print(666,self.num)

objs = [F1(1),F2(2),F2(3)]
objs[1].run() #666 2  #这里run方法下的self表示的是F2的对象，而不是F1的对象
objs[2].run() #666 3
print('-----------------------练习4')

#5 看代码写结果
class UserInfo: #用户信息类
    pass

class Department: #部门类
    pass

class Starkconfig:  #整体配置
    def __init__(self,num):
        self.num = num

    def changelist(self,request):
        print(self.num,request)

    def run(self):
        self.changelist(999)

class RoleConfig(Starkconfig): #角色配置
    # #子类RoleConfig调父类Starkconfig的run方法，run方法中的changelist用的是子类的
    def changelist(self,request):
        print(666,self.num)

class AdminSite: #管理员站点类
    def __init__(self):
        self._registry = {}  #注册列表-字典  私有字典

    def register(self,k,v):
        self._registry[k] = v(k)   #私有变量

site = AdminSite() #创建一个空的注册字典
site.register(UserInfo,Starkconfig)

# # site._registry[UserInfo] = starkconfig(UserInfo)
# starkconfig1 = Starkconfig(UserInfo)
# {UserInfo:starkconfig1(UserInfo)}   #类名是可哈希的-不可变的，可以作为字典的key

site.register(Department,RoleConfig)

# site._registry[Department] = RoleConfig(Department)

# roleConfig1 = RoleConfig(Department)
# {UserInfo:starkconfig1(UserInfo),Department:roleConfig1(Department)}
# 这里的字典是2个键值对，而不是一个键值对  注意点

for k,row in site._registry.items():
    row.run()   #starkconfig1(UserInfo).run()  #对象调方法，对象的参数是类名
                #roleConfig1(Department).run()

# starkconfig1.run()  #<class '__main__.UserInfo'> 999   #类名作为参数
#  run方法中的self指的是starkconfig1对象
# roleConfig1.run()   #666 <class '__main__.Department'>
#  run方法中的self指的是roleConfig1对象

print('-----------------------练习5')











