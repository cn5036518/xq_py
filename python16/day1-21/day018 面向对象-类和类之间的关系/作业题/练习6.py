#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/1/4 6:46
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
class Student:
    def __init__(self,id,name,address):
        self.id = id
        self.name = name
        self.address = address
        self.course_list = []

    def select_course(self,course):  #参数是课程对象
        self.course_list.append(course)  #一对多，一个学生可以选多门课

    def display(self):
        for i in self.course_list:
            print(i.course_name)  #打印课程列表

class Course:
    def __init__(self,courseid,course_name):
        self.courseid = courseid
        self.course_name = course_name
        # self.teacher = teacher

    def assign_teacher(self,teacher): #参数是老师对象，一对一 （一个课程一般对应一个老师）
        self.teacher = teacher  #self.teacher后面接上老师的成员变量

class Teacher:
    def __init__(self, teacherid, teacher_name, phone):
        self.teacherid = teacherid
        self.teacher_name = teacher_name
        self.phone = phone

# 请完成以上三个类. 创建6个课程, 6个老师. 给课程安排好老师. 然后创建30个学生.
# 每个学生随机被分配3个课程. 最终显示出这三十个学生的选课情况以及任课老师的电话
c1 = Course('c001','语文')
c2 = Course('c002','数学')
c3 = Course('c003','英语')
c4 = Course('c004','物理')
c5 = Course('c005','化学')
c6 = Course('c006','生物')

t1 = Teacher('t001','jack',10001)
t2 = Teacher('t002','tom',10002)
t3 = Teacher('t003','bob',10003)
t4 = Teacher('t004','james',10004)
t5 = Teacher('t005','keven',10005)
t6 = Teacher('t006','lucy',10006)

s1 = Student('s001','小强','朝阳')
s2 = Student('s002','小明','海淀')
s3 = Student('s003','小花','东城')

#学生1选3门课程
s1.select_course(c1)
s1.select_course(c2)
s1.select_course(c3)

#学生2选3门课程
s2.select_course(c1)
s2.select_course(c2)
s2.select_course(c4)

#学生3选3门课程
s3.select_course(c4)
s3.select_course(c5)
s3.select_course(c6)

#给6门课程分别指定老师
c1.assign_teacher(t1)
c2.assign_teacher(t2)
c3.assign_teacher(t3)
c4.assign_teacher(t4)
c5.assign_teacher(t5)
c6.assign_teacher(t6)

#最终显示出这三十个学生的选课情况以及任课老师的电话
print('---------学生1的选课情况：')
print(s1.display())
print(c1.teacher.phone)  #这里的c1.teacher就指代老师对象
print(c2.teacher.phone)
print(c3.teacher.phone)

print('---------学生2的选课情况：')
print(s2.display())
print(c1.teacher.phone)
print(c2.teacher.phone)
print(c4.teacher.phone)

print('---------学生3的选课情况：')
print(s3.display())
print(c4.teacher.phone)
print(c5.teacher.phone)
print(c6.teacher.phone)

'''
一个学生可以选择多门课程  一对多（学生和课程）
一个课程对应一个老师      一对一（课程和老师）
遗留问题：
1、学生和课程的一对多，可以打印学生选择的3门课程的名字
2、课程和老师的一对一，可以打印每个课程对应的老师的电话
如何直接打印学生所选3门课程的3个老师的电话？
'''






