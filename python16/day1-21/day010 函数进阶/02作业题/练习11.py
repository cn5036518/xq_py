#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 11,写函数，传入一个参数n，返回n的阶乘
# 例如:cal(7)  计算7*6*5*4*3*2*1

#方法1
def factorial(n):
    if n <0:
        print('负数没有阶乘')
    elif n==0:
        print('0的阶乘是1')
    else:
        factorial1 = 1  #初始值一般是0（加法-累加）或者1（乘法-累乘）
        for i in range(1,n+1): #左闭右开，所有是n+1  #注意点
            # print(i)
            factorial1 = factorial1 * i   #累乘  #关键点
            # print(factorial1)
    print('%s 的阶乘是 %s' % (n,factorial1))
factorial(4)
print('-----------------1')

#方法2
def factorial2(n):
    if type(n) == float:
        print('小数没有阶乘')
    elif type(n) != int:
        print('请输入正整数')
    elif n<0:
        print('负数没有阶乘')
    elif type(n) == int:
        try:
            n1 =1
            for i in range(n,0,-1):
                n1 *=i  #累计相乘--累乘
            print(n1)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(e)
factorial2(4)









