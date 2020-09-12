#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 14相关面试题（先从纸上写好答案，然后在运行）：
# 1，有函数定义如下：
# def calc(a,b,c,d=1,e=2):
# return (a+b)*(c-d)+e
# 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1,2,3,4,5))_____
# print(calc(1,2))____
# print(calc(e=4,c=5,a=2,b=3))___
# print(calc(1,2,3))_____
# print(calc(1,2,3,e=4))____
# print(calc(1,2,3,d=5,4))_____


def calc(a,b,c,d=1,e=2):
    return (a+b)*(c-d)+e

print(calc(1,2,3,4,5)) #2
print((1+2)*(3-4)+5) #2  d是4 e是5 都覆盖了默认值参数
print('--------------1')

# print(calc(1,2))
#TypeError: calc() missing 1 required positional argument: 'c'
#报错 c没有传值
print('--------------2')

print(calc(e=4,c=5,a=2,b=3)) #24
print((2+3)*(5-1)+4)  #24  d是1--取的默认值参数
print('--------------3')

print(calc(1,2,3))   #8
print((1+2)*(3-1)+2)  #8  d是1 e是2--都是默认值参数
print('--------------4')

print(calc(1,2,3,e=4)) #10
print((1+2)*(3-1)+4)  #10  d是1 e是4--d是默认值参数，e覆盖了默认值参数
print('--------------5')

# print(calc(1,2,3,d=5,4)) #报错
#SyntaxError: non-keyword arg after keyword arg
#报错
#关键字参数必须在位置参数之后，关键字参数必须在最后
print('--------------6')













