#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/30 6:32
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
11.	面向对象中为什么要有继承？
    继承的好处：
        1、避免重复的代码，
        2、更好的扩展（子类的方法可以覆盖父类，也可以扩展父类方法，青出于蓝而胜于蓝）
        有3个类，a b c，其中呢，b和c是属于a的
        那么a就是父类，b和c是子类
        父类中把b和c都有的属性和方法封装
        子类b和c就不需要定义父类中的属性和方法了，只需要定义父类中没有的属性和方法即可
        因为子类会继承父类的属性和方法

12.	Python多继承时，查找成员的顺序遵循什么规则？
    就近原则
    比如：子类c继承了父类a1和父类a2
    如果遇到方法名method1在父类a1和父类a2中都存在，那么会继承父类a1的，就近原则
'''
class Base1:
    def f1(self):
        print('base1.1')
    def f2(self):
        print('base1.f2')
    def f3(self):
        print('base2.f3')
        self.f1()

class Base2:
    def f1(self):
        print('base2.f1')

class Foo(Base1,Base2):
    def f0(self):
        print('foo.f0')
        self.f3()

f1 = Foo()
f1.f0()
# foo.f0
# base2.f3
# base1.1
print('----------------------- 13')

# 15.	补充代码实现：
#
# user_list = []
# while True:
#         user = input(“请输入用户名:”)
#         pwd = input(“请输入密码:”)
#         email = input(“请输入邮箱:”)
#
# 1.	while循环提示用户输入：用户名、密码、邮箱
# 2.	为每个用户创建一个对象，并添加到列表中。
# 3.	当列表中的添加了3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱

'''
步骤：
1、先写死
2、后换成input 交互式

'''

user_list = []
class Acount:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def output1(self):
        print(self.username,self.email)

user1 = Acount('jack','123','jack@163.com')
user2 = Acount('tom','456','tom@163.com')
user3 = Acount('bob','789','bob@163.com')

user1.output1()
user2.output1()
user3.output1()
print('--------------------15-1')

# user_list = []
# class Acount:
#     def __init__(self,username,password,email):
#         self.username = username
#         self.password = password
#         self.email = email
#
#     def output1(self):
#         print(self.username,self.email)
#
# user = input('请输入用户名:')
# pwd = input('请输入密码:')
# email = input('请输入邮箱:')
# user1 = Acount(user,pwd,email)
#
# user2 = input('请输入用户名:')
# pwd2 = input('请输入密码:')
# email2 = input('请输入邮箱:')
# user2 = Acount(user2,pwd2,email2)
#
# user3 = input('请输入用户名:')
# pwd3 = input('请输入密码:')
# email3 = input('请输入邮箱:')
# user3 = Acount(user3,pwd3,email3)
#
# user1.output1()
# user2.output1()
# user3.output1()

user_list = []
class Acount:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    def output1(self):
        print(self.username,self.email)

user1 = Acount('jack','123','jack@163.com')
user2 = Acount('tom','456','tom@163.com')
user3 = Acount('bob','789','bob@163.com')
user_list = [user1,user2,user3]

for i in user_list:
    user1.output1()

print('--------------------15-2')

class Acount:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    # def output1(self):
    #     print(self.username,self.email)

li1 = []
while 1:
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    email = input('请输入邮箱:')
    user1 = Acount(user,pwd,email)  #把输入的用户名、密码、邮箱封装到对象  #关键点1
    #列表的元素可以是 对象（对象中封装着用户名、密码、邮箱）
    li1.append(user1)  #3个对象添加到空列表
    if len(li1) == 3:  #添加3个对象后，跳出循环
        break

for i in li1:  #循环遍历列表，列表的元素是对象（对象中封装着用户名、密码、邮箱）
    # i.output1()  #对象调方法，打印用户名和邮箱名  #关键点2
    print(i.username,i.email) #这里直接用对象.属性即可
print('--------------------15-3')

class Acount:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
    # def output1(self):
    #     print(self.username,self.email)

li1 = []
for i in range(3):
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    email = input('请输入邮箱:')
    user1 = Acount(user,pwd,email)  #把输入的用户名、密码、邮箱封装到对象  #关键点1
    #列表的元素可以是 对象（对象中封装着用户名、密码、邮箱）
    li1.append(user1)  #3个对象添加到空列表
    # if len(li1) == 3:  #添加3个对象后，跳出循环
    #     break
else:
    for i in li1:  #循环遍历列表，列表的元素是对象（对象中封装着用户名、密码、邮箱）
        print(i.username,i.email)  #这里直接用对象.属性即可
print('--------------------15-4')

'''
15题 小结：
思路：
1、定义类
   构造方法，传入用户名、密码、邮箱
   普通方法，打印用户名和邮箱
2、定义空列表
3、while循环
    输入用户名、密码、邮箱
    新建对象，自动调构造方法，传入用户名、密码、邮箱
    把对象追加到空列表   --关键点1
    当列表的长度是3的时候，跳出整个循环
4、循环遍历列表
    列表的元素是对象   --关键点2
    对象调普通方法

步骤：
1、有input交互的
2、先把input交互后的变量写死

'''







