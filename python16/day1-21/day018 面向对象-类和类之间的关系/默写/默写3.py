#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/1/7 6:59
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
3. 用面向对象的嵌套表示：学生、班级、老师的关系，并创建相关对象进行嵌套【根据自己的理解编写】；
   这里的嵌套，我的理解是一对一和一对多关系

班级和学生  一对多，一个班级有多个学生
老师和学生  一对多，一个老师有多个学生
班级和老师  一对多，一个班级有多个班级
'''

class Class:
    number_students = 0   #类变量 共享的
    number_teachers = 0   #类变量2 共享的
    def __init__(self,grade,classno):
        self.grade = grade
        self.classno = classno
        self.student_li1 = []
        self.teacher_li2 = []

    def register(self,s1): #s1是学生对象，新同学   班级分配新同学
        self.student_li1.append(s1)
        Class.number_students += 1  #班级学生人数
        Class.number_teachers += 1  #班级老师人数

    def recruit(self,t1):  #t1是老师对象，新老师   班级安排新老师
        self.teacher_li2.append(t1)

    #新同学和新老师能否用一个方法  多态  判断

    def display(self):  #打印班级中学生的姓名名单
        for i in self.student_li1:
            print(i.name)

    def display_teacher(self):  # 打印班级中老师的名单
        for i in self.teacher_li2:
            print(i.name)

    #打印学生名单和打印老师名单能否用一个方法  多态 判断
    # def display(self,li1):  # 打印班级中学生的姓名名单
    #     for i in li1:
    #         print(i.name)

class Student:
    def __init__(self, name, gender,age,class1):
        self.name = name
        self.gender = gender
        self.age = age
        self.class1 = class1  #这个是班级对象

class Teacher:
    def __init__(self, name, gender, age, hobby,class1):
        self.name = name
        self.gender = gender
        self.age = age
        self.hobby = hobby
        self.class1 = class1   #这个是班级对象
        self.student_list1 = []

    def recruit_students(self,s1):  #s1是学生对象  老师招收学生
        self.student_list1.append(s1)

    def display(self):  #打印学生的名单
        for i in self.student_list1:
            print(i.name)


    #新建2个班级，4个学生，每个班级2个学生
#新建2个班级
c1 = Class('grade 1','class 3')  #一年级三班
c2 = Class('grade 2','class 1')  #二年级一班

#新建4个学生
s1 = Student('jack','boy',7,c1)
s2 = Student('tom','boy',7,c1)
s3 = Student('lucy','girl',8,c2)
s4 = Student('lily','girl',8,c2)

c1.register(s1)
c1.register(s2)
c2.register(s3)
c2.register(s4)

c1.display() #显示班级1的学生名单
# jack
# tom
print(Class.number_students)   #学生总人数是4人   类变量，共享的
print(len(c1.student_li1))  #班级1的学生人数是2人

c2.display()  #显示班级2的学生名单
# lucy
# lily
print(len(c2.student_li1))  #班级2的学生人数是2人
print('-----------------1 班级和学生 一对多')

#2  新建4个老师
t1 = Teacher('bob','male',27,'run',c1)
t2 = Teacher('james','male',28,'read',c1)
t3 = Teacher('kate','female',29,'sing',c2)
t4 = Teacher('rose','female',26,'dance',c2)

c1.recruit(t1)
c1.recruit(t2)
c2.recruit(t3)
c2.recruit(t4)

c1.display_teacher()
c2.display_teacher()

print(Class.number_teachers)   #老师总人数是4人   类变量，共享的
print(len(c1.teacher_li2))  #班级1的老师人数是2人
print(len(c2.teacher_li2))  #班级1的老师人数是2人

print('-----------------2 班级和老师 一对多')
t1.recruit_students(s1)
t1.recruit_students(s2)
t2.recruit_students(s3)
t2.recruit_students(s4)

t1.display()
# jack
# tom
t2.display()
# lucy
# lily
print('-----------------3 老师和学生 一对多')












