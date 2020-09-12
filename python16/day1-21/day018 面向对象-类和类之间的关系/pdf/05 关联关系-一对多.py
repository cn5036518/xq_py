#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/18 7:04
#@author:wangtongpei
#@email: cn5036520@163.com

class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.teacher_list = []  #老师名单
    def recruit(self,teacher):   #参数是老师对象
        #把另外一个类的对象，作为当前类的属性来传递和保存
        self.teacher_list.append(teacher)
    def dispay(self):  #打印老师的姓名
        for i in self.teacher_list:
            print(i.name)  #这里的i是老师对象

class Teacher:
    def __init__(self,name,school):  #这里的school对象表示学校对象
        #把另外一个类的对象，作为当前类的属性来传递和保存
        self.name = name
        self.school = school

s1_bj = School('北京校区','沙河')

t1 = Teacher('jack',s1_bj)
t2 = Teacher('tom',s1_bj)

s1_bj.recruit(t1)   #学校陆续招聘了2名老师
s1_bj.recruit(t2)

# print(s1_bj.teacher_list)  #老师列表中，保存的是老师对象（是对象，而不是老师的姓名）

# for i in s1_bj.teacher_list:
#     print(i.name) #打印老师对象的名字

s1_bj.dispay()   #显示老师的姓名

'''
关联关系-一对多
例子1：学校和老师（公司和员工）
1、老师类的构造方法中传入学校对象
   每个老师都属于一个学校
2、学校类的构造方法中定义一个老师名单空列表
    每个学校都有老师名单
3、学校类的成员方法-招聘的参数是老师对象
    成员方法-招聘的方法体是：空列表追加老师对象
    注意点：
        列表中存放的是老师对象，而不是老师的姓名

例子2：消费者和订单（一对多）
1、订单类的构造方法中传入消费者对象
   每个订单都属于一个消费者
2、消费者类的构造方法中定义一个订单空列表
    每个消费者都有一个订单列表
3、消费者的成员方法-下订单的参数是订单对象
    成员方法-下订单的方法体是：空列表追加订单对象
    注意点：
        列表中存放的是订单对象，而不是订单的名字

例子3：订单和商品sku（一对多）
1、商品类的构造方法中传入订单对象
    每个商品都属于一个订单类
2、订单类的构造方法中定义一个所购商品空列表
    每个订单都有一个商品列表
3、订单类的成员方法-选商品的参数是商品对象
   成员方法选商品的方法体是：商品空列表追加商品对象
   注意点：
        列表中存放的是商品对象，而不是商品的名字

例子4：商品sku和商品ssu（一对多）
    例子：土豆就是sku，3斤装一包的土豆和5斤装一包的土豆就是不同的ssu
1、ssu类的构造方法中传入sku对象
    每个ssu都属于一个sku类
2、sku类的构造方法中定义一个ssu空列表
   每个sku都有一个ssu列表
3、sku类的成员方法-选ssu的参数是ssu对象
   成员方法选ssu的方法体是：ssu空列表追加ssu对象
   注意点：
       列表存放的是ssu对象，而不是ssu的名字

小结：
关联关系的本质：
把另外一个类的对象，作为当前类的属性来传递和保存


'''





