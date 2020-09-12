#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1. 判断一个数是否是水仙花数, 水仙花数是一个三位数,
# 三位数的每一位的三次方的和还等于这个数. 那这个数就是一个水仙花数, 例如: 153 = 1**3 + 5**3 + 3**3

#方法1
num = 154   #这是写死的，也可以用户输入input
num1 = num//100   #通过地板除 获取百位数字  #关键点是如何获取到百位、十位、个位的数字（通过地板除//来获取）
num2 = (num-num1*100)//10  #获取十位数字
num3 = num-num1*100-num2*10 #获取个位数字
if num1**3 + num2**3 + num3**3 == num:
    print("%s 是水仙花数" % num)
else:
    print("%s 不是水仙花数" % num)
print("----------1")

#方法2  老师
while 1:
    num = input("请输入三位数,输入q退出:")  #输入的是字符串
    if num.upper() == "Q":
        break
    elif len(num) == 3: #1 先判断是否是3位
        if num.isdigit():  #2 判断输入的字符串是否是数字形式
           num1 = int(num[0])  #获取百位后，字符串转换成int，方便后面计算
           num2 = int(num[1]) #获取十位后，字符串转换成int，方便后面计算
           num3 = int(num[2]) #获取个位后，字符串转换成int，方便后面计算
           num = int(num)  #字符串转换成int，为了后面计算
           result = num1**3 + num2**3 + num3**3
           if result == num:  # 3 最后判断是否符合水仙花数的标准
               #注意：这里是num之前是字符串，所以可以通过索引号取出百位、十位、个位的字符串
               print("%s 是水仙花数" % num)
           else:
               print("%s 不是水仙花数" % num)
        else:
            print("您输入的不合法，请输入数字")
    else:
        print("您输入的不是三位，请重新输入")












