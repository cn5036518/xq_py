#!/usr/bin/env python
#-*- coding:utf-8 -*-

#思路5 列表中0-9的数字，添加的时候，就从int转换成str字符串类型
import random
def generate_verifycode2(len=6):  #默认参数
    li1 = []
    for i in range(0, 10):  # 添加数字
        li1.append(str(i))  #将数字转换成str字符串类型  对应23行 （如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(65, 91):  # 添加大写字母
        li1.append(chr(i))  # chr(65) 是将数字65，转换成阿斯克码-ascii是65的字母“A”
    # print(li1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C'
    for i in range(97, 122):  # 添加小写字母
        li1.append(chr(i))
    # print(li1)
    # import random  # 导入内置库-包random-随机函数包
    li2 = random.sample(li1, len)
    # print(li2)  # [8, 'Y', 'r', 6, 'T', 'W']
    # li3 = [str(i) for i in li2]  # 将列表的元素全部转换成字符串  #前面第10行已经将数字转换成了字符串
    # print(li3)  # ['8', 'Y', 'r', '6', 'T', 'W']
    str1 = "".join(li2)  # 通过空白连接符，连接列表中的元素转成字符串（将list转换成str字符串）
        # （如果列表中有数字，需要将数字转换成字符串才能连接,否则报错）
    # print(str1)
    return str1  #将6位验证码的字符串返回

#调函数
str3=generate_verifycode2(5)  #产生5位验证码，如果不传参数，默认产生6位验证码
print(str3)
print("-----==------==------")

str2="abc"
li2=list(str2)  #字符串转换成列表，用list
print(li2) #['a', 'b', 'c']

total=0  #全局变量

def sum1(arg1,arg2):
    total=arg1+arg2  #这里的total是局部变量
    print("函数内局部变量",total)  #30
    return total

total =sum1(10,20) #这里的total是全局变量
print("函数外全局变量",total)  #30
















