#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/15 11:29
#@author:wangtongpei
#@email: cn5036520@163.com

""""""
'''
关联关系的分类：
一对一关系：男朋友和女朋友
一对多关系：学校和老师
            你，订单，明细，商品
'''

class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.__techer_list = []  #老师名单-私有变量  关键点1

    def recruit(self,t):  #招聘-成员方法  参数t是老师对象
        self.__techer_list.append(t)  #把老师对象加入老师名单  这里是一对多  关键点2
        #注意点： self.__techer_list必须先在构造方法中定义，否则会报错

    def display(self):  #显示老师名单
        for i in self.__techer_list:  #这里的i是老师对象
            print(i.name)  #i.name表示的是老师的名字   注意点1

class Teacher:
    def __init__(self,name,gender,salary,hobby,school):  #最后一个形式参数是学校对象
        # 这个学校参数不是必须的 可以不传  注意点2
    # def __init__(self,name,gender,salary,hobby):  #
        self.name = name
        self.gender = gender
        self.salary = salary
        self.hobby = hobby
        self.school = school  #老师都归属一个学校  这里的school是学校对象  关键点2

#新建3个学校对象（也可以只新建一个校区）
oldboy_bj = School('北京校区','沙河')  #自动调构造方法
oldboy_sh = School('上海校区','浦东')
oldboy_sz = School('深圳校区','南山')

#新建3个老师对象  自动调构造方法
t1 = Teacher('jack','男',1000,'run',oldboy_bj)  #最后一个参数是 学校对象  关键点1
t4 = Teacher('james','男',1000,'run',oldboy_bj)  #最后一个参数是 学校对象  关键点1
t2 = Teacher('tom','男',1000,'read',oldboy_sh)
t3 = Teacher('bob','男',1000,'run',oldboy_sz)

# t1 = Teacher('jack','男',1000,'run')  #最后一个参数是 学校对象  关键点1
# t2 = Teacher('tom','男',1000,'read')
# t3 = Teacher('bob','男',1000,'run')

#学校对象调成员方法--招聘
oldboy_bj.recruit(t1)  #1北京校区招聘了一名老师t1
oldboy_bj.recruit(t4)  #1北京校区招聘了一名老师t4
oldboy_sh.recruit(t2)  #2上海校区招聘了一名老师t2

#学校对象调成员方法--显示老师名单
oldboy_bj.display()  #jack james
oldboy_sh.display()  #tom

'''
小结：
关联关系中一对一和一对多的区别

一、写法不同
1、前者
    男孩类的成员方法
        def meet(self,girl):  #参数是女孩对象  女孩对象传递给男孩的女朋友这个成员变量
            self.girl_friend = girl  #关键点
            #男孩对象的成员变量-girl_friend就是女孩对象

2、后者
    学校类的构造方法
        self.__techer_list = []
    学校类的成员方法
        def recruit(self,t):  #招聘-成员方法  参数t是老师对象
            self.__techer_list.append(t)

二、例子不同
1、前者的例子是男女朋友
2、后者的例子是学校和老师

扩展：
组合关系、聚合关系和关联关系的写法是类似的，但是含义不同
1、聚合和组合关系都是关联关系的特例
2、类比列子
    关联关系：
        1、一对一：男女朋友
        2、一对多：学校和老师

    聚合关系：
        1、电脑和电脑组件
            电脑由cpu、内存、硬盘等构成
            电脑挂了，cpu还是好的

    组合关系：
        1、人和人的器官
            人体由大脑、心脏、各个器官组成
            人挂了，器官就都挂了（一损俱损，强关联）

'''















