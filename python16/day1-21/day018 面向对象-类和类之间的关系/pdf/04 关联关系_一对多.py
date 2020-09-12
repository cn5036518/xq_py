#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/18 6:54
#@author:wangtongpei
#@email: cn5036520@163.com

#学校和老师 就是一对多的关系
class School:
    def __init__(self,name,address):
        self.name = name
        self.address = address

class Teacher:
    def __init__(self,name,school=None): #把学校对象传入,传递给老师的学校这个成员变量
        # （用这个成员变量指代学校对象）
        self.name = name
        self.school = school

s1_bj = School('北京校区','沙河')

t1 = Teacher('jack',s1_bj)
t2 = Teacher('tom',s1_bj)
print(t1.name,t1.school.name)  #jack 北京校区
print(t2.name,t2.school.address) #tom 沙河
print('----------------------------1')



















