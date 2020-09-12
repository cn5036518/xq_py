#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 4,读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# 	a=10
# 	b=20
# 	def test5(a,b):
# 		a=3
# 		b=5
#      	print(a,b)
# 	c = test5(b,a)
# 	print(c)
# 	print(a,b)

a=10
b=20
def test5(a,b):
    a=3
    b=5
    print(a,b) #3 5  #取的是局部变量（局部变量的取值优先级 高于参数传递进来的）
    # #因为名称空间的取值顺序：局部名称空间（局部变量）>全局名称空间（全局变量
# c = test5(b,a)
c = test5(20,10) #取的是全局变量  函数执行完毕后，函数的内存空间就回收饿了
print(c)  #None  #没有return 默认返回None
print(a,b) #10 20  #取的是全局变量

'''
名称空间的加载顺序：内置名称空间>           全局名称空间            >局部名称空间
名称空间的取值顺序：局部名称空间（局部变量）>全局名称空间（全局变量）>内置名称空间



'''














