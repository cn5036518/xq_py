#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1、判断下列逻辑语句的True,False.
# 1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) #True
print(False or True or False and True and True or False) #True
print(False or True or False or False) #True

print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6) #False
print(not True and True or False and True and True or False) #False
print(False and True or False or False)  #False
print("-------------1")

# 2、求出下列逻辑语句的值。
# 1),8 or 3 and 4 or 2 and 0 or 9 and 7
# 2),0 or 2 and 3 and 4 or 6 and 0 or 3
print(8 or 3 and 4 or 2 and 0 or 9 and 7) #8
print(8 or 4 or 0 or 7) #8
print(8 or 0 or 7) #8

print(0 or 2 and 3 and 4 or 6 and 0 or 3)  # 4
print(0 or 4 or 0 or 3)  # 4
print(4 or 0 or 3)  #4
print("-------------2")

# 下列列结果是什什么？
# 1)、6 or 2 > 1
# 2)、3 or 2 > 1
# 3)、0 or 5 < 4
# 4)、5 < 4 or 3
# 5)、2 > 1 or 6
# 6)、3 and 2 > 1
# 7)、0 and 3 > 1
# 8)、2 > 1 and 3
# 9)、3 > 1 and 0
# 10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
print(6 or 2 > 1) #6
print(6 or True)  #6

print(3 or 2 > 1) #3
print(3 or True)  #3

print(0 or 5 < 4) #False
print(0 or False)  #False

print(5 < 4 or 3) #3
print(False or 3) #3

print(2 > 1 or 6) #True
print(True or 6)  #True

print(3 and 2 > 1) #True
print(3 and True)  #True

print(0 and 3 > 1) #0
print(0 and True)  #0

print(2 > 1 and 3) #3
print(True and 3)  #3

print(3 > 1 and 0) #0
print(True and 0)  #0

print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2) #2
print(True and 2 or True and 3 and 4 or True) #2
print(2 or 4 or True) #2
print("-------------3")















