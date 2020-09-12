#!/usr/bin/env python
#-*- coding:utf-8 -*-


#1 int 整数
# 计算整数4的二进制的位数(二进制表示的长度),注意:4必须引用小括号括起才行,否则报错
# print((1).bit_length()) #1   0000 0001
# print((2).bit_length()) #2   0000 0010
# print((4).bit_length())#3    0000 0100
# # print(4.bit_length())#报错 #SyntaxError: invalid syntax
#
# a=4
# print(a.bit_length())  #3   0000 0100
# print(bin(a))  #0b100  0b表示二进制的标识 bin()函数,参数是整数int,将整数(默认十进制)转换成二进制   内置函数

#2 类型的转换
#1 把字符串转换成数字int
a = "10"  #字符串类型
print(int(a))  #10   整数

#2 把整数int转换成字符串
a = 10  #整数int
print(str(a))  #"10" 字符串类型
# print(type(str(a))) #<class 'str'>

#3 把整数10转换成布尔类型
a = 10
print(bool(a))  #True

#4  把布尔值True转换成字符串
b1 = True
print(str(b1))  #"True"
print(type(str(b1)))  #<class 'str'>
print("--------1")

#5  把布尔值True转换成整数int    1是True
b1 = True
print(int(b1))  #1
print(type(int(b1)))  #<class 'int'>
print("--------2")

#6  把布尔值False转换成整数int   0是False
b1 = False
print(int(b1))  #0
print(type(int(b1)))  #<class 'int'>
print("--------3")

#结论1:把xxx转换成yyy类型的方法  yyy(xxx)
#结论2:True是1  False是0
      # "" [] () {} None  (0 空字符串\空列表\空字典\None)  除此之外,其余都是True
      #1 0之外的数字都是True
      #2 0\空字符串\空列表\空元组\空字典\None(即所有的空的东西)之外的都是True
#结论3:所有空的东西都是False   0 "" [] () {} None  (0\空字符串\空列表\空元组\空字典\None)
    #  所有非空的东西都是True

print(bool(0))  #False   0是False
print(bool("")) #False   ""空字符串是False
print(bool([])) #False   []空列表是False
print(bool({})) #False   {}空字典是False
print(bool(())) #False   ()空元组是False
print(bool(None)) #False None是False
print(None)  #None
print("--------4")
print(bool(" "))  #True   " "空格是True
print(bool("    ")) #True   tab制表符 是True
print(bool("False")) #True   字符串"False"是True
print(bool("False")) #True   字符串"False"是True
print(bool(False))  #False    False本身的布尔值是False
print("--------5")

#空列表的3种形式
print([])    #[] #1标准的空列表[]
print([   ]) #[] #2中括号中有多个空格[    ]也是空列表
print([         ])  #[]   #3中括号中有多个空格或者tab[       ]是空列表
#None 如果函数没有明确写return,默认是返回None   #空气\水\阳光

# while 1:   #对比1和True 1的效率要高于True(效率高一点点)
# 因为计算机是二进制,只认识0或者1,这里1就就可以直接识别,True还需要经过处理转换成1后,才能被识别
# while True:
#     print("hi")



