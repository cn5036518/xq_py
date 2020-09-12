#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1 int
# a=4
# print(a.bit_length())  #计算数字（默认十进制）的二进制的长度(位数)  #"0b100"
# print(4.bit_length())  #SyntaxError: invalid syntax
# print("4".bit_length())  #AttributeError: 'str' object has no attribute 'bit_length'
print((4).bit_length())  #3   注意：这里的数字4必须加小括号，加引号就是字符串（会报错），不加小括号（会报错：语法错误）

#2 类型转换
"""
1 0是False 1是True
2 空的都是False，其余都是True
    0 "" [] () {} None都是False，其余都是True（空格，tab都是True）
    0 空字符串 空列表 空元组 空字典 None都是Fasle，其余都是True
"""

#3字符串的切片和回文
s1 = "afasfsadsjdjfafj"
# s2 = s1[start:end:step]
"""
#1 step的正负决定取值方向
    step是正数，取值方向是从左到右，默认是1
    step是负数，取值方向是从右到左
#2 star和end 是顾头不顾尾，左闭右开
"""
# print(s1[2:4])  #注意：切片的分隔符是冒号，range（）中的参数分隔符是逗号
# #取索引下标是2,3的数    #as
# print(s1[2:-1])  #-1
# #取索引下标是2到倒数第2个数  #asfsadsjdjfaf
# print(s1[2:])  #取到最后
# #取索引下标是2到倒数第1个数  #asfsadsjdjfafj
# print(s1[2:-1:2])  #步长是2
# #取索引下标是2到倒数第2个数这个范围中，每隔2个取一个  #afasdff
#
# print(s1[:4])  #从开头开始取
# #取索引下标是0到3的数（前面4位数）  #afas
# print(s1[:])  #取字符串的全部，复制字符串
# # afasfsadsjdjfafj
# print(s1[0:5:-1])  #空白
# #step是-1 取值方向是从右往左，所以取不到值
# print(s1[-1:-5:-1])  #jfaf
# #step是-1 取值方向是从右往左，取值范围是-1到-4
# print(s1[::-1])  #将字符串反转
# # step是-1，取值方向是从右往左，取值范围是整个字符串
#jfafjdjsdasfsafa

print(s1[-5::-3]) #step是-3 从右往左取值，取值范围是：从-5取到最开头（注意：这里的end是空是取到最开头）  # jssa
print(s1[-5::3]) #step是3 从左往右取值，取值范围是：从-5取到最末尾（注意：这里的end是空是取到最末尾）  #jf


#二 回文
s1 ="哈哈发哈哈"
if s1 == s1[::-1]:
    print("是回文")
else:
    print("不是回文")

# for i in range(-1,-4,-1): #-1到-3
#     print(i)

#类型转换
#一、字符串和整数互转
# 1 字符串转整数  int(str)
s1 = "10"  #这里的"10"是字符串
print(int(s1))  #10  这里的10是整数

# 2 整数转字符串  str(int)
num = 11  #这里的11是正合适
print(str(num)) #11 这里的"11"是字符串

#二、字符串和bool值互转
#1、字符串转bool值  bool(str)
s1 = ""
print(bool(s1)) #Fasle  空字符串的bool值是False
print(bool("    \r\n")) #空格、回车换行、tab的bool值都是True
#扩展：空的东西都是False,其余都是True
#    0 "" [] () {} None都是False，其余都是True（空格、tab、回车换行）
print("----------1")

#2 bool值转字符串 str(bool)
print(str(True))  #"True" 这里的True是字符串类型
print(str(False)) #“False” 这里的False是字符串类型

#三、整数和bool值的转换
#1 整数转换成bool
print(bool(0))  #0是False，其余的整数都是True
print(bool(1))  #1是True
print("----------2")

#2 bool值转换成整数
print(int(False))  #0  #False在内存中对应的是0
print(int(True))   #1  #True在内存中对应的是1

#4 字符串的常见操作







