#!/usr/bin/env python
#-*- coding:utf-8 -*-


# n=3
# for i in range(n - 1):
#     print('+' * i + 'X' + "+" * (2 * (n - i) - 3) + 'X' + '+' * i)

# print('X'.center(2 * n - 1, '+'))
#
# for j in range(n-2,-1,-1):
#     print('+' * j + 'X' + "+" * (2 * (n - j) - 3) + 'X' + '+' * j)

# 题目1：输出5*5的对角线  这里的5*5是写死的
for i in range(2): #0-1  换行2次，限定范围就是0-1    #前面2行
    print(" " * i + '*' + " " * (3-2*i)+ '*' + " " * i)
 # i=0  空格是3; 中间1
#  i=1  空格是1 中间2
# 最左边 i=0 空格是0
# 最左边 i=1 空格是1
print("*".center(5," ")) #中间是$，一共5个的字符，两边用空格补全   #中间行

for i in range(2): #0-1  换行2次，限定范围就是0-1   #最后2行
    print(" " * (1-i) + '*' + " " * (1+2*i)+ '*' + " " * (1-i))
 # i=0  空格是1;中间
#  i=1  空格是3  中间2
# 最左边 i=0 空格是1
# 最左边 i=1 空格是0

"""
1、先输出第一二行
2、在输出第三行
3、最后输出第四五行
"""





