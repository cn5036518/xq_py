#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
5，写函数，计算传入函数的字符串中, 数字、字母、空格 以及 其他内容的个数，并返回结果。
"""

def nums(s):  #形参用s命名，表示要传入字符串
    count_int = 0
    count_letter = 0
    count_space = 0
    count_other = 0
    for i in s:
        if i.isdigit():  #判断字符串中的字符是否是数字
            #如果输入i.后没有输入提示，就给形参改成s='',再次输入i.就有方法提示了   #注意点
            #最后要把s=''改成s
            count_int += 1
        elif i.isalpha(): #判断是否是字母
            count_letter += 1
        elif i.isspace(): #判断是否是空格
            count_space += 1
        else:   #判断其他
            count_other += 1
    print("数字的个数是 %s" % count_int)
    print("字母的个数是 %s" % count_letter)
    print("空格的个数是 %s" % count_space)
    print("其他内容的个数是 %s" % count_other)
    return count_int,count_letter,count_space,count_other

s1 = 'jack 123&*'
ret = nums(s1)
print(ret)  #(3, 4, 1, 2)
print('数字 %s,字母 %s,空格 %s,其他 %s' % (ret[0],ret[1],ret[2],ret[-1]))  #数字 3,字母 4,空格 1,其他 2
# 数字的个数是 3
# 字母的个数是 4
# 空格的个数是 1
# 其他内容的个数是 2
# (3, 4, 1, 2)
# 数字 3,字母 4,空格 1,其他 2




























