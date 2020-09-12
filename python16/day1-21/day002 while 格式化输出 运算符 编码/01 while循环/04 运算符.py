#!/usr/bin/env python
#-*- coding:utf-8 -*-


print(2 > 3 and 4 < 6) #False
print(False and False)  #False

print(10 < 6  or  9 > 7 or 5 > 8)  #True
print(False or True or False)  #True

print(not 5 > 6) #True
print(not False) #True

# 面试题
# 运算顺序 () => not => and => or
print(1 > 2 and 3 < 6 or 5 > 7 and 7 > 8 or 5 < 1 and 6 > 3)  #False
print(False and True or False and False or False and True) #False
print(False or False or False) #False
print("------1")

print(3 > 4 or 4<3 and 1 ==1)     # False
print(False or False and True) #False

print(1 < 2 and 3 < 4 or 1 > 2)  # True
print(True and True or False) #True

print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)    # False
print(True and False or False and False)  #False

print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)   # #False
print(False and False or False and True or False)  #False

print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     #  #False
print(False and True or False and True and True or False)  # False
print(False or False or False)  #False

print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)     # # False
print(not True and True or False and True and True or False)  # False
print(False or False or False)  # False
print("------2")

print(1 or 2 and 3) #1
print(1 or 3)  #1

# x or y 如果x为0 则返回y， 否则。 返回x
# and和or相反。
# True: 1
# False: 0

print(1 or 2 or 0 or 3 or 5) #1
print(1 or 0 or 3 or 5) #1
print(1 or 3 or 5) #1

print(0 or 0 or 5 or 3) #5
print(0 or 5 or 3) #5
print(5 or 3)   #5
print("------3")

print(0 or 1 and 2) #2
print(0 or 2)  #2

print(1 or 1 > 2 and 3 or 5 and 4 > 6)  #1
print(1 or False and 3 or 5 and False)  #1
print(1 or False or False)  #1
print("------4")


print(3 > 4 or 4<3 and 1 ==1)     # False
print(False or False and True) #False

print(1 < 2 and 3 < 4 or 1 > 2)  # True
print(True and True or False) #True
print("------5")

print(3>4 or 4<3 and 1==1)  #False
print(False or False and True)  #False

print(1 < 2 and 3 < 4 or 1>2)  #True
print(True and True or False)  #True

print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)  #True
print(True and True or False and False)  #True

print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8) #False
print(False and True or False and True or False) #False
print(False or False or False)  #False

print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  #False
print(False and True or False and True and True or False)  #False
print(False or False or False)  #False

print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)#False
print(not True and True or False and True and True or False)  #False
print(False or False or False)  #False
print("------6")

print(8 or 4) #8
print(0 and 3) #0
print(0 or 4 and 3 or 7 or 9 and 6) #3
# print(0 or 3 or 7 or 6)
# print(3 or 7 or 6)  #3


"""
总结
1  0是False--其余数字都是True
2  1是True 2也是True

3、or的话
    1、第一个是True，就是True，取第一个的值
    2、第一个是False，就取第二个的值

4、and的话
    1、第一个是False，就是Flase，取第一个的值
    2、第一个是True，就取第二个的值

5、运算顺序
    小括号>not>and>or


"""












