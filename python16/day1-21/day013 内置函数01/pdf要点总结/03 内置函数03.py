#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/26 7:55
#@author:wangtongpei

#数据类型
#1 bool() 函数
print(bool('\r'))  #True
print(issubclass(bool,int))  #True  boolshi int的子类
print(bool(False)) #False
print(bool(True)) #True
print('-----------------1 bool()函数 ')

#2 int()参数
print(int(3.6))  #3  #将小数转换成int，会直接取整，而不是四舍五入
print(int('12'))  #12 #将字符串形式的数字，转换成数字
# print(int('a'))  #报错 ValueError: invalid literal for int() with base 10: 'a'
print(int())  #0 不传入参数，返回的是0
print(int('10',base=8))  #8 默认是base=10，按照十进制进行转换
print(int('0xa',base=16))  #10 默认是base=10，按照十六进制进行转换
print('-----------------2 int()函数 ')

#3 float()参数
print(float(3))   #3.0 将int转换成小数
print(float('3.7')) #3.7 将字符串形式的小数转换成小数
print(float())  #0.0  参数不写，返回0.0
print('-----------------3 float()函数 ')

#4 complex()函数
print(complex(1)) #(1+0j) #参数1是实部
print(complex(1,2)) #(1+2j) #参数1是实部，参数2是虚部
# print(complex('1 + 2j'))  #报错  ValueError: complex() arg is a malformed string
# 注意 加号两边不能有空格
print(complex('1+2j')) #(1+2j)
print(complex())  #0j  参数不写，返回0j
print('-----------------4 complex()函数 ')

#5-1 bin()函数
print(bin(5))  #0b101  这里0b开头表示二进制
print(type(bin(5)))  #<class 'str'>
# print(bin(5.5))  #报错 TypeError: 'float' object cannot be interpreted as an integer
# print(bin('5'))  #报错 TypeError: 'str' object cannot be interpreted as an integer
print('-----------------5-1 bin()函数 ')

#5-2 oct()函数
print(oct(8))  #0o10  这里0o开头表示八进制
print('-----------------5-2 oct()函数 ')

#5-3 hex()函数
print(hex(16))  #0x10  这里0x开头表示十六进制
print('-----------------5-3 hex()函数 ')

#6-1 abs()函数
print(abs(-1))  #1
print(abs(-1.1))  #1.1
print(type(abs(-1.1)))  #<class 'float'>
print('-----------------6-1 abs()函数 ')

#6-2 divmod()函数
print(divmod(10,3))  #(3, 1)  #返回商和余数的元组
print('-----------------6-2 divmod()函数 ')

#6-3 round()函数
print(round(1.235,2))  #1.24 保留2位小数，保留的时候，做四舍五入
print('-----------------6-3 round()函数 ')

#6-4 pow()函数
print(pow(3,2))  #9
print(3**2)      #9
print('-----------------6-4 pow()函数 ')

#6-5 sum()函数
# print(sum(1,2))  #报错 TypeError: 'int' object is not iterable
li1 = [1,2]
print(sum(li1))  #3 参数1是Iterable  参数2不写默认是0
print(sum(li1,2))  #5
# str1 = '12'
# print(sum(str1))  # 报错TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('-----------------6-5 sum()函数 ')

#6-6 min()函数
li1 = [1,2]  #1
print(min(li1))  #返回列表中多个元素的最小值
print(min(2.1,3,4))  #2.1  #返回多个参数中的最小值
print('-----------------6-6 min()函数 ')

#6-7 max()函数
li1 = [1,2]  #1
print(max(li1))  #2 返回列表中多个元素的最大值
print(max(2.1,3,4))  #4  #返回多个参数中的最大值
print('-----------------6-7 max()函数 ')












