#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/24 6:14
#@author:wangtongpei
#@email: cn5036520@163.com

# 1. 创建一个武松-对象（属性：名字，外号，爱好）. 武松可以打老虎, 行侠仗义(方法)
class Hero:  #类名的首字母大写，命名规范
    def __init__(self,name,nickname,hobby):
        self.name = name
        self.nickname = nickname
        self.hobby = hobby

    def kill_tiger(self):
        print('%s-%s 在景阳冈打老虎' % (self.nickname,self.name))
        # print('%s %s在景阳冈打老虎' % (nickname,name)) #不写self 会报错

    def act_like_a_hero(self):
        print('%s-%s 行侠仗义' % (self.nickname, self.name))

wusong = Hero('武松','行者','喝酒')
wusong.kill_tiger() #行者-武松 在景阳冈打老虎
wusong.act_like_a_hero() #行者-武松 行侠仗义
print('------------------------------ 1')

# 2. 编写和尚类. ⾃己⾃由发挥和尚有哪些属性(名字，庙)和方法（念经，还俗-娶媳妇）.
class Monk:
    def __init__(self,name,temples):
        self.name = name
        self.temples = temples

    def chant(self): #方法1 动词-念经
        print('%s 在念经' % self.name)

    def marry(self,wife): #参数wife   #方法2 动词-还俗结婚
        print('%s 还俗，娶媳妇 %s' % (self.name,wife))   #
        # 注意点：这里wife不是构造方法中的属性，形参（需要在对象调方法的时候，传入实参），前面不带self

kulin = Monk('枯林','日本本能寺') #新建对象，自动调构造方法
kulin.chant()  #枯林 在念经
kulin.marry('人造人18号')  #枯林 还俗，娶媳妇 人造人18号
# 注意点，这里给类的方法传了实参
print('------------------------------ 2')

# 3. ⽤面向对象的思维来完成用户登录.
#把用户名和密码封装到账户这个类--封装
class Account:  #账户类
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):  #方法1 动作-登录
        if self.username == 'jack' and self.password == '123':
            print('登录成功')
            return True
        else:
            print('登录失败')
            return False

username1 = 'jack'
password1 = '123'
account1 = Account(username1,password1)  #创建新对象-账户1，自动调构造方法
account1.login() #对象调方法   #登录成功







