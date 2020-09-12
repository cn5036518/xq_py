#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
9，写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
用户通过输入这四个内容，然后将这四个内容传入到函数中，
此函数接收到这四个内容，将内容追加到一个student_msg文件中。

10，对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
'''

def stu_info(name,age,education,gender='male'):
    #形参的默认参数（实参不传值的话，就取默认参数；实参传值的话，就覆盖默认参数）
    with open('student_msg.txt', mode='a', encoding='utf-8') as f:
        f.write('%s|%s|%s|%s\n' % (name, gender, age, education))
    # f.write('%s|%s\n' % (name,sex))

# #方法1
# n = 1
# for i in range(10):  # 允许输入10次
#     question1 = input("请输入第 %s 个学生的信息，输入q或者Q退出,输入enter继续：" % n)
#     n += 1
#     if question1.upper() == 'Q':   #先判断是退出还是继续输入
#         break
#
#     name1 = input('请输入学生的姓名:')
#     age1 = input('请输入学生的年龄:')
#     education1 = input('请输入学生的学历:')
#     gender1 = input('请输入学生的性别:')
#     # if (name1.upper() or education1.upper() or gender1.upper())== 'Q':
#     #     #注意点：==前面的内容必须加上小括号，否则优先级不对   --关键点
#     #     break
#     # stu_info(name1,age1,education1)  #取形参的默认参数
#
#     if gender1 == '':  #如果没有输入性别，空字符串
#         stu_info(name1,age1,education1)  #取形参的默认参数--male
#     else:  #如果输入了性别
#         stu_info(name1, age1, education1,gender1)  # 覆盖形参的默认参数

#方法2
n = 1
for i in range(10):  # 允许输入10次
    question1 = input("请输入第 %s 个学生的信息，输入q或者Q退出,输入其他任何内容继续：" % n)
    n += 1
    if question1.upper() == 'Q':   #先判断是退出还是继续输入
        break

    name1 = input('请输入学生的姓名:')
    age1 = input('请输入学生的年龄:')
    education1 = input('请输入学生的学历:')
    gender1 = input('请输入学生的性别:')

    gender1 = ('male' if gender1 == '' else 'female')   #三目运算
    #如果不输入，性别就取-male，如果输入其他，性别就取-female
    stu_info(name1, age1, education1,gender1)  # 覆盖形参的默认参数













