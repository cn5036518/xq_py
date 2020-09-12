#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
3，写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
'''

def greater5(arg):  #arg或者obj作为形参的名字
    if len(arg) >5:
        print('实参的长度大于5')
        return True
        # return len(arg) >5  #也可以
    else:
        print('实参的长度小于等于5')
        return False

s1 = 'jack'
greater5(s1)  #实参的长度小于等于5

li1 = ['jack','tom','bob']
greater5(li1)  #实参的长度小于等于5







