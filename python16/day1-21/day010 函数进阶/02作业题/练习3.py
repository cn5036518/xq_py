#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# 	a=10
# 	b=20
# 	def test5(a,b):
#      	print(a,b)
# 	c = test5(b,a)
# 	print(c)

a=10
b=20
def test5(a,b):  #这里的a和b是形参
    print(a,b) #20,10
c = test5(b,a)  #这里的a和b是实参  等价于 c = test5(20,10)
print(c) #None  #没有return，默认返回值是None

'''
小结：
1、形参的变量名和实参的变量名，最好分开，不一样，否则，可能会出现混淆
2、实参的值和形参的名字是没有关系的，独立的

'''

















