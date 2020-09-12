#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/9 16:21
#@author:wangtongpei
#@email: cn5036520@163.com

#bit_length是int的内置方法
# 用来计算十进制数字转换成二进制后的位数
i = 3
print(i.bit_length())  #2  #3转换成二进制是11 是2位

i2 = 7
print(i2.bit_length())  #3 #7转换成二进制是421 是3位

#字符串的切片
s1 = 'james'
print(s1[1:4:2])  #ae  步长是2
print(s1[::-1])  #semaj 反转

#常见的字符串的内置方法
li1 = ['jack','tom']
print('_'.join(li1))  #jack_tom
#Concatenate any number of strings.

li2 = [1,2]
# print('_'.join(li2))  #报错 TypeError: sequence item 0: expected str instance, int found
#这里join的参数是iterable，iterable的元素必须是字符串，而不能是数字

s1 ='12'
print(s1.isdigit()) #True  '12'字符串是数字形式，就返True
s1 ='12b'
print(s1.isdigit()) #False

#bool
# content1 = input('请输入你的名字:')  #输入的是字符串
# if content1:  #判断空  如果不输入内容，直接回车，就提示-你没有名字 注意点：和下面行的结果不一样
# # if content1 == '':  #如果不输入内容，直接回车，就打印-你的名字是
#     print('你的名字是 ',content1)
# else: #如果你什么都没有输入，这个content1就是空字符串
#     print('你没有名字')

li1 = [1,2,3]
if li1:  #这里就是在判断列表是否为空， 和下面行等效
# if li1 == []:
    print(li1)
else: #
    print('空列表')







