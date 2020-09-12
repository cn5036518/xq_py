#!/usr/bin/env python
#-*- coding:utf-8 -*-

# # 15输⼊⼀个数. 判断这个数是⼏位数(⽤算法实现)(升级题)
# result = input("请输入一个数")
# print(len(result))  #待完善--nok   #下面的len()函数的实现

def len1(num):
    count=0
    for i in num:
        # print(i)
        count+=1
    print("这个数的位数是%s位" % count)
num= 245
num = str(num)  #将整数转换成字符串,字符串可以for循环,int整数无法for循环,报错是
# TypeError: 'int' object is not iterable
len1(num)  #3位

# 13 用户输入一个数.  判断这个数是否是一个质数(素数)(升级题).

"""
质数或者素数的定义:
1 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数
    2,3 5,7,11,13
2 基本判断思路
在一般领域，对正整数n，如果用2到根号√n之间的所有整数去除，均无法整除，则n为质数。
质数大于等于2 不能被它本身和1以外的数整除
"""

from math import sqrt   #导入根号
print(sqrt(5))  #2.23  4的平方根是2  4开二次方是2--2**2=4
print(type(sqrt(4)))  #float
# print(int(sqrt(5)))  #向下取整 2
# #计算1-10范围内的质数
# print(int(2.9))  #向下取整 2

# for i in range(2,12):#0-10
#     # print(i)
#     for j in range(2,int(sqrt(i))+1):  #2,3
#         if i%j ==0:  #一旦余数是0,就是能整除,说明不是质数,跳出内层循环,回到外层循环
#             break  #必须是break 不能是continue
#     else:  #这个else是内层for循环的条件不满足的时候,才执行的,一旦有break的话,else不会执行
#         print(i)
"""
思路:
1 当i=9的时候,j=2的时候 9%2的余数是1,于是就继续循环内层for
  当i=9的时候,j=3的时候 9%2的余数是0,于是就break,跳出内层循环,后面的else是不执行的,9是不会打印出来的,
  继续外层的for循环,当i=10,j=2,10%2的是余数是0,于是就break,跳出内层循环,后面的else是不执行的,10是不会打印出来的,
    继续外层的for循环,当i=11,j=2,11%2的余数是1,继续循环内层for
    继续外层的for循环,当i=11,j=3,11%3的余数是2,继续循环内层for
    此时,内层的for循环都不满足条件了,range(2,4)的取值是2,3,此时执行else,就会打印11--关键点

总结:
1 输出质数,先弄清楚质数的概念,除了1和自身之外,不能被其他的数整除
2 换算成程序思路
    在一般领域，对正整数n，如果用2到√n--根号n (而不是2到n-1,因为2到n-1虽然对,但是效率要低一些,内循环多循环了一些数)
    之间的所有整数去除，
    均无法整除，则n为质数。
    质数大于等于2,且不能被它本身和1以外的数整除
3 关键点  内层for循环后面平级的else,和break后,后面平级的else是不执行的
          例如:9被3整除了,就break,跳出内层for循环,后面平级的else就不执行,不会打印9
              10被2整除了,就break,跳出内层for循环,后面平级的else就不执行,不会打印10
              11不被2或者3整除,没有break,range(2,4)的取值就是2,3,此时内层for循环的条件不满足了
                 就要执行内层for循环后面平级的else,就会打印11
"""
#题目1:请输出13以内的质数
def zhishu(num):  #这里的num是限定多少范围内的质数
    for i in range(2,num+1):#0-10
        # print(i)
        for j in range(2,int(sqrt(i))+1):  #2,3   #这里的sqrt需要先导入,int(sqrt(i))是向下取整
            if i%j ==0:  #一旦余数是0,就是能整除,说明不是质数,跳出内层循环,回到外层循环
                break  #必须是break 不能是continue
        else:  #这个else是内层for循环的条件不满足的时候,才执行的,一旦有break的话,else不会执行
            print(i)
num = 13
zhishu(num)  #输出质数,传入的参数是多少以内的质数
#比如:输出2-13之间的质数,参数传入13即可
print("----------------1")

def prime1(num):  #这里的num是限定多少范围内的质数   #prime是质数的含义
    for i in range(2,num+1):#0-10
        # print(i)
        for j in range(2,i):  #2,3   #这里2,i 效率要低于2,int(sqrt(i))+1
            if i%j ==0:  #一旦余数是0,就是能整除,说明不是质数,跳出内层循环,回到外层循环
                break  #必须是break 不能是continue
        else:  #这个else是内层for循环的条件不满足的时候,才执行的,一旦有break的话,else不会执行
            print(i)
num = 13
prime1(num)  #输出质数,传入的参数是多少以内的质数
#比如:输出2-13之间的质数,参数传入13即可
print("----------------2")

# #题目2,请判断一个数是否是质数
# def zhishu_is(i):  #
#     for j in range(2,int(sqrt(i))+1):  #2,3
#         if i%j ==0:  #一旦余数是0,就是能正常,说明不是质数,跳出内层循环,回到外层循环
#             print("%s不是质数" % i)
#             break  #必须是break 不能是continue
#     else:  #这个else是内层for循环的条件不满足的时候,才执行的,一旦有break的话,else不会执行
#         print("%s是质数" % i)
#
# i=6  #写死
# # i = input("请输入一个数,判断是否是质数")  #用户输入的
# # i = int(i)
# zhishu_is(i)
# print("----------------3")

















