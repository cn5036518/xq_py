#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1. 判断一个数是否是水仙花数, 水仙花数是一个三位数, 三位数的每一位的三次方的和还等于这个数.
# 那这个数就是一个水仙花数, 例如: 153 = 1**3 + 5**3 + 3**3

# s1 = "153"
while 1:
    s1 = input("请输入一个三位数,输入q退出：")
    if s1.upper() == "Q":
        print("退出")
        break
    elif len(s1) == 3:
        if s1.isdigit():
            sum1 = int(s1[0]) ** 3 + int(s1[1]) ** 3 + int(s1[2]) ** 3
            # 注意点：字符串需要转换成int，才能计算，否则报错
            # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
            num1 = int(s1)
            if num1 == sum1:
                print("%s 是水仙花数"% s1)
            else:
                print("%s 不是水仙花数" % s1)
        else:
            print("您输入的不是数字，请输入数字")
    else:
        print("您输入的不是三位数，请重新输入")
"""
步骤：
1 可以先写死这个数，
2 然后再变成用户输入，
3 最后增加循环
注意点：
1、字符串不能计算，计算前需要转换成int
2、判断位数长度，判断输入的字符串是个是数字类型

"""











