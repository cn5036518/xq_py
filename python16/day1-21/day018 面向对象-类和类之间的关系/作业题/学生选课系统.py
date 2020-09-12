#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/1/27 17:35
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
1. 完成学生选课系统. (升级题)
学生选课.
    学生:
        信息: 学号, 姓名, 住址. 选的课程列表,
        功能:
            查看: 查看该学生所有课程信息.
            添加课程: 把选好的课程添加到课程列表中 (传参)
    课程:
        信息: 课程编号, 课程名称. 老师.
        功能:
            查看: 查看该课程的全部信息
            设置老师: 给当前课程设置一个老师. (传参)
    老师:
        信息: 老师编号, 老师名称. 电话
            功能: 无

请完成以上三个类. 创建6个课程, 6个老师. 给课程安排好老师. 然后创建30个学生.
每个学生随机被分配3个课程. 最终显示出这三十个学生的选课情况以及任课老师的电话
'''

import random

class Student:
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address
        self.course_list = []  #每个学生自己所选择的课程列表（比如：3门不同的课程）

    def select_course(self,course):  #参数是课程对象
        self.course_list.append(course)  #一对多，一个学生可以选多门课

    def display(self):#查看该学生所有的课程信息
        print('该学生的姓名是: ', self.name)
        # for i in self.course_list:
        for i in range(len(self.course_list)):  #列表的索引号
            # print('该学生选择的课程是: ', i.course_name)  # 打印课程列表
            print('该学生选择的第%s门课程是: %s' % (i+1,self.course_list[i].course_name))  # 打印课程列表
            # if i.teacher:  # 如果老师存在   i.teacher表示课程对象对应的老师
            if self.course_list[i].teacher:  # 如果老师存在   i.teacher表示课程对象对应的老师
                # print('该课程老师的姓名是: %s' % i.teacher.teacher_name)
                print('该课程老师的姓名是: %s' % self.course_list[i].teacher.teacher_name)
                # print('该课程老师的电话是: %s' % i.teacher.phone)
                print('该课程老师的电话是: %s' % self.course_list[i].teacher.phone)
            else:  # 如果老师不存在
                print('该课程还没有老师')
            print('--------------------------')
            #注意点：i指代的是课程对象，课程对象是有老师的   --关键点

    def __str__(self):#打印学生对象的时候，不打印对象的内存地址，而是打印对象的姓名，所选的3门课程名称
        print('该学生的姓名是: ', self.name)
        for i in self.course_list:
            print('该学生选择的课程是: ',i.course_name)  #打印课程列表
        return '=================='   #必须return字符串，不写或者返回的不是字符串，会报错
            #TypeError: __str__ returned non-string (type NoneType)

    # 注意点： __str__() 方法的返回值的类型必须是字符串，而不能是元组，也不能返回None，否则会报错

class Course:
    def __init__(self,courseid,course_name,teacher=None):
        # if teacher != None and type(teacher) == Teacher:  #只能是Teacher类，不能是Teacher类的子类
        if teacher != None and isinstance(teacher,Teacher):  #可以是Teacher类及其子类
            #限定传入的teacher对象，必须是老师类(及其子类)的对象，才允许传入
            self.courseid = courseid
            self.course_name = course_name
            self.teacher = teacher   #这门课程的初始老师（每个课程默认有一个老师,默认没有老师-None）
        else:
            pass

    def assign_teacher(self,teacher): #参数是老师对象，一对一 （一个课程一般对应一个老师）
        #重新分配老师，换老师
        self.teacher = teacher  #self.teacher后面接上老师的成员变量

    def show(self):#查看该课程的全部信息，比如：该课程的名称，该课程的授课老师
        if self.teacher:#如果老师存在
            print('该课程的名称是 %s' % self.course_name)
            print('该课程的老师是 %s' % self.teacher.teacher_name)
            #self.teacher指代老师对象
        else: #如果老师不存在
            print('该课程的名称是 %s' % self.course_name)
            print('该课程的老师是 %s' % '无')
        #注意点：如果不写这个if，当老师默认是None的时候，会报错


class Teacher:
    def __init__(self, teacherid, teacher_name, phone):
        self.teacherid = teacherid
        self.teacher_name = teacher_name
        self.phone = phone

#1 创建6门课程
c1 = Course(1,'语文')
c2 = Course(2,'数学')
c3 = Course(3,'英语')
c4 = Course(4,'历史')
c5 = Course(5,'经济')
c6 = Course(6,'金融')

#2 创建6个老师
t1 = Teacher(1,'泉灵',10086)
t2 = Teacher(2,'吴军',10087)
t3 = Teacher(3,'笑来',10088)
t4 = Teacher(4,'施展',10089)
t5 = Teacher(5,'薛兆丰',10081)
t6 = Teacher(6,'香帅',10082)

#3 给课程安排老师
c1.assign_teacher(t1)  #语文老师是泉灵
c2.assign_teacher(t2)
c3.assign_teacher(t3)
c4.assign_teacher(t4)
c5.assign_teacher(t5)
c6.assign_teacher(t6)

#4 定义一个总的课程列表--总结
course_li1 = [c1,c2,c3,c4,c5,c6]   #6门课程组成的列表，一共是6门课程-总集，每个学生从中选择3门不同的课程--子集
#从列表中随机选出3个元素

student_li1 = []   #定义学生空列表

#5 创建30个学生
for i in range(30):
    stu = Student(i,'Stu%s' % i,'沙河')   #学号，姓名，地址

    # 5-2 每个学生随机选3门不同的课程
    selected_courses = random.sample(course_li1,3)   #从6门课程中随机选择3门不同的课程，组成新的列表
    # print(selected_courses) #随机选择的3门课程,3门课程组成的列表

    for j in selected_courses:
        stu.select_course(j)   #学生选课，每个学生选择3门不同的课程

    student_li1.append(stu)   #把30个学生对象，依次添加到学生空列表

# print(student_li1)  #学生对象的内存地址的列表

#6打印30个学生，每个学生的姓名，以及每个学生所选的3门课程
for i in student_li1:
    # print(i)  #方式1：__str__（）
    i.display() #方式2

#7打印30个学生所选的3门课程对应的老师的电话--nok
































