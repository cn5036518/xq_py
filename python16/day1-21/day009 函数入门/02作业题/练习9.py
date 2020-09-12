#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
9，写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
用户通过输入这四个内容，然后将这四个内容传入到函数中，
此函数接收到这四个内容，将内容追加到一个student_msg文件中。
'''

'''
思路：
步骤：
1、先不输入，先写死--用变量定义好，传入固定的值，然后追加到文件
2、然后把写死改成输入input
'''

#方法1
def stu_info(name,gender,age,education):
    f = open('student_msg.txt',mode='a',encoding='utf-8')
    f.write('%s|%s|%s|%s\n' % (name,gender,age,education)) #换行
    f.flush()
    f.close()

# name1 = 'jack'
# sex1 = 'male'
# age1 = 18
# education1 = 'Bachelor Degree'   #本科学士学位
name1 = input('请输入学生的姓名:')
gender1 = input('请输入学生的性别:')
age1 = input('请输入学生的年龄:')
education1 = input('请输入学生的学历:')

# stu_info(name1,gender1,age1,education1)

#方法2
def stu_info2(name,gender,age,education):
    with open('student_msg.txt',mode='a',encoding='utf-8') as f:  #推荐这个 打开文件
        #自带f.flush()和f.close()
        f.write('%s|%s|%s|%s\n' % (name,gender,age,education)) #换行

# name1 = 'jack'
# gender1 = 'male'
# age1 = 18
# education1 = 'Bachelor Degree'   #本科学士学位
name1 = input('请输入学生的姓名:')
gender1 = input('请输入学生的性别:')
age1 = input('请输入学生的年龄:')
education1 = input('请输入学生的学历:')

stu_info2(name1,gender1,age1,education1)











