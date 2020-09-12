#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 5:46
#@author:wangtongpei

''''''
'''
函数名的应用
1、函数名的内存地址
2、函数名可以作为参数传递
3、函数名可以作为容器（例如：list等）的元素--批量执行
4、把函数名当做一个变量单次或者连续赋值给其他变量
5、函数名可以函数的返回值

1、函数名的命名规则和变量名是一样的
'''

# 1、函数名的内存地址,函数名后面加小括号就是执行
def func1():
    print('我是函数')
print(func1)  #<function func1 at 0x0000000001D06730>
print('----------------1')

# 2、函数名可以作为参数传递
#2-1 代理设计模式
def panpan():
    print('我是panpan')
def ximen():
    print('我是大官人')

def wangpo(female,male):  #核心业务逻辑，不变的，执行不同的场景，只需要传递不同的参数-函数名即可
    female()
    male()

wangpo(panpan,ximen)  #函数名作为了参数进行了传递
# 我是panpan
# 我是大官人
print('----------------2-1 代理设计模式')

#2-2
def func21():
    print('我是第一个函数')

def func22(args):#形参，函数名
    print('我是第二个函数')
    args()  #
    print('我是第二个函数')

func22(func21)  #实参：函数1的函数名
print('----------------2-2 函数名可以作为参数传递')

# 3、函数名可以作为容器（例如：list等）的元素--批量执行
#应用场景：如果想要批量执行多个函数，将多个函数名添加到列表，循环遍历列表后，元素后面加小括号即可
def func31():
    print('我是函数31')
def func32():
    print('我是函数32')
li1 = [func31,func32]
for i in li1:
    i()
print('----------------3')

# 4、把函数名当做一个变量单次或者连续赋值给其他变量
def func4():
    print('函数名为变量赋值')
a = func4 #把函数名当做一个变量单次或者连续赋值给其他变量
b = a
c = b
c()  #函数名为变量赋值
print(c.__name__)  #func4  通过__name__属性可以找到原始的函数名
print('----------------4')

# 5、函数名可以函数的返回值
def outer():
    a = 10
    def inner():
        print(a)
        return a
    return inner
ret = outer()
print(ret)  #<function outer.<locals>.inner at 0x00000000025C21E0>
#这里的ret就是inner函数的内存地址
ret()  #10  这里等效于inner()函数的执行
print('----------------5')










