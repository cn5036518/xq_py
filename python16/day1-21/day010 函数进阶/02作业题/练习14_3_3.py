#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3, 写代码完成99乘法表.(升级题)
# 1 * 1 = 1
# 2 * 1 = 2 2 * 2 = 4
# 3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
# ......
# 8 * 1 = 8 8 * 2 = 16 8 * 3 = 24 8 * 4 = 32 8 * 5 = 40 8 * 6 = 48 8 * 7 = 56 8 * 8 = 64
# 9 * 1 = 9 9 * 2 = 18 9 * 3 = 27 9 * 4 = 36 9 * 5 = 45 9 * 6 = 54 9 * 7 = 63 9 * 8 = 72 9 * 9 = 81

# 一、打印乘法表
for i in range(1,10):
    # print(i)  #1 先打印9行  默认换行
    for j in range(1,i+1):  #注意点：拼写range不能缺少   第2行（从1数到2） 第3行（从1数到3）
        print('%s * %s = %s' % (i,j,i*j),end=' ')  #去掉换行   #乘法表
        # print('*',end=' ')  #去掉换行  #直角三角形 打印的是星*
        #把打印的东西换成*就是直角三角形  第一行1个* 第二行2个星*
    print()  #换行

# 4, 写代码完成(升级题)
# *
# **
# ***
# ****
# ....

for i in range(1,10):
    # print(i)  #1 先打印9行  默认换行
    for j in range(1,i+1):  #注意点：拼写range不能缺少   第2行（从1数到2） 第3行（从1数到3）
        print(j*'*',end=' ')  #去掉换行
    print()  #换行
'''
*
* **
* ** ***
* ** *** ****
'''
print('-------------------1')

#三、打印直角三角形
for i in range(1,10):
    # print(i)  #1 先打印9行  默认换行
    for j in range(1,i+1):  #注意点：拼写range不能缺少   第2行（从1数到2） 第3行（从1数到3）
        print('*',end=' ')  #去掉换行
    print()  #换行
'''
*
**
***
****
'''
print('-------------------2')


# 5, 写代码完成等腰三角形(倒着的等腰三角形、正的和倒着的等腰三角形拼接成的菱形)，第一行1个星 第二行3个星
'''
   *
  ***
 *****
*******
。。。
思路分析：
1、第一行是3个空格+1个星  4  关键点在空格和星的个数规律（行号和空格个数以及行号和星号个数的关系--关键）
2、第二行是2个空格+3个星  5
3、第三行是1个空格+5个星  6
4、第四行是0个空格+7个星  7

i=1 j=1,2,3

*******
 *****
  ***
   *


   *
  ***
 *****
*******
 *****
  ***
   *

*   *
 * *
  *
 * *
*   *

'''

# for i in range(1,5):  #1-4 一共是4行
#     for j in range(1,5-i):
#         print(' '*(j+2)+'*'*j)
#     print()









