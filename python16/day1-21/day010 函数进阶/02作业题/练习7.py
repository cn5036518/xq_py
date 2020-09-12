#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 7, 下面代码成立么?如果不成立为什么报错?怎么解决?
# 7.1
# 	a = 2
# 	def wrapper():
#     	    print(a)
# 	wrapper()
#
# 7.2
# 	a = 2
# 	def wrapper():
#             	a += 1
#     		print(a)
# 	wrapper()
# 7.3
# def wrapper():
#     		a = 1
#     		def inner():
#         		print(a)
#     		inner()
# 	wrapper()
# 7.4
# def wrapper():
#     		a = 1
#     		def inner():
#         		a += 1
#         		print(a)
#     		inner()
# 	wrapper()

a = 2
def wrapper():
    print(a) #取值顺序：局部名称空间>全局名称空间>内置名称空间
wrapper() #2
print('-----------------1')

# a = 2
# def wrapper():
#     # global a
#     a += 1  #取值顺序是：局部名称空间>全局名称空间 但是只能是取值-读，不能修改-写  a+=1做了修改
# 想要不报错，需要在a=1上面加一行 global a才行（把全局变量引入到当前位置，访问和修改全局变量）
#     print(a)
# wrapper()
# UnboundLocalError: local variable 'a' referenced before assignment
print('-----------------2')

def wrapper():
    a = 1
    def inner():
        print(a) #1  #这里的a只是取值，并没有修改，是允许的
        #如果除了读取，还需要修改的话，就会报错；需要在a=1上面加一行 nonlocal a才行
    inner()
wrapper()
print('-----------------3')

# def wrapper():
#     a = 1
#     def inner():
#         a += 1
#         print(a)  ## a只能是取值-读，不能修改-写  a+=1做了修改
#            想要不报错，需要在a=1上面加一行 nonlocal a才行（把父级的局部变量引入到当前位置，访问和修改父级的局部变量）
#     inner()
# wrapper()
#UnboundLocalError: local variable 'a' referenced before assignment
# 局部变量在赋值之前，已经引用了
print('-----------------4')









