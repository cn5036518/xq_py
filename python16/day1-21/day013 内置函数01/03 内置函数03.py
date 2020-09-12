#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/15 8:40
#@author:wangtongpei

#反转
li1 = [1,2,3]
it1 = reversed(li1)  #返回的是迭代器
print(it1)  #<list_reverseiterator object at 0x0000008655299C48>
li2 = list(it1)  #把迭代器转换成列表
print(li2)  #[3, 2, 1]

for i in it1:  #迭代器可以直接循环遍历  （列表的循环，内部原理就是调用了迭代器）
    print(i)
print('-------------------1 反转')

#切片
li1 = [1,2,3]
#方法1  推荐 简洁
print(li1[0:2])  #[1, 2]

#方法2  不常见
s1 = slice(0,2)
# print(type(s1))  #<class 'slice'>
print(li1[s1])  #[1, 2]
print('-------------------2 切片')

#3格式化
#01 字符串格式化
s1 = 'test'
print(format(s1,'<20')) #一共是20个字符的位置，<左对齐，test后面是16个空格
print(format(s1,'>20')) #一共是20个字符的位置，>右对齐，test前面是16个空格
print(format(s1,'^20')) #一共是20个字符的位置，^居中对齐，test前面和后面格式8个空格
print('-------------------3-1 字符串格式化')

#02 数字
#001 进制转换 二进制、八进制、十六进制  参数是int，返回的是str
print(format(3,'b'))  #11  转换成二进制-b开头表示，返回的是str
# print(type(format(3,'b')))  #字符串类型
print(format(10,'o'))  #12 转换成八进制-o开头表示，返回的是str
print(format(31,'x'))  #1f 转换成十六进制-x开头表示-小写字母，返回的是str
print(format(31,'X'))  #1F 转换成十六进制-大写字母，返回的是str

#002 转换成十进制  参数是int，返回是str
print(format(33,'d'))  #33 转换成十进制，返回的是str
print(format(33,'n'))  #33 转换成十进制，返回的是str
print(format(33))  #33 转换成十进制，返回的是str
#将数字33转换成十进制的33--字符串格式

#003 转换成unicode（ascii），参数（输入）是int，返回（输出）的是str
print(format(97,'c'))  #a 转换成unicode（ascii），返回的是str
print('-------------------3-2 数字-进制格式化')

#03 小数-浮点数
#001 保留几位小数
print(format(0.1254564,'0.2f'))  #0.13 四舍五入，保留2位小数
print(format(0.1254564,'0.3f'))  #0.125 四舍五入，保留3位小数

#002 科学计数法e
print(format(125456789,'e'))  #1.254568e+08  默认保留6位小数，四舍五入
print(format(125456789,'0.2e'))  #1.25e+08  保留2位小数，四舍五入,e小写
print(format(125456789,'0.2E'))  #1.25E+08  保留2位小数，四舍五入，E大写

#003 无穷大
print(format(1.25e+1000,'f'))  #inf infinite--无穷大
print('-------------------3-3 小数格式化-保留几位小数')

#4 把字符串转换成字节bytes
s4 = '你好'
ret1 = s4.encode('utf-8') #一个汉字是3个字节
print(ret1) #b'\xe4\xbd\xa0\xe5\xa5\xbd'  #这里的b表示的是二进制的字节（1个字节8位）

ret2 = bytes(s4,'utf-8')
print(ret2) #b'\xe4\xbd\xa0\xe5\xa5\xbd'

s42 = 'alex'  #将英文字母转换成utf-8还是英文字母（前面加了b，表示字节），
# 因为英文字母是ascii，不管是unicode还是utf-8都会兼容ascii
print(s42.encode('utf-8')) #b'alex'

s43 = 'alex哈哈'  #转换成utf-8 英文字母不变，一个汉字是3个字节
print(s43.encode('utf-8'))  #b'alex\xe5\x93\x88\xe5\x93\x88'
print('-------------------4 把字符串转换成字节bytes')

#5 bytearray
s1 = 'aAex'
ret5 = bytearray(s1,encoding='utf-8')
print(ret5[0])  #97 把字符串'aAex'的第1个字符取出来，转换成ascii对应的数值 a就是97
print(ret5[1])  #108 把字符串'aAex'的第2个字符取出来，转换成ascii对应的数值 A就是65
print('-------------------5 把字符串的字符取出来，转换成ascii的数字')

#6 ord和chr
#01 ord()
print(ord('a'))  #97 把字符（字母或者汉字等）转换成数字-ascii或者字的编号
print(ord('王'))  #29579 把字符（字母或者汉字）转换成数字-ascii或者字的编号
print('-------------------6-1 把字符（字母或者汉字等）转换成数字-ascii或者字的编号')

#02 chr()
print(chr(65)) #A  把ascii数字转换成字母，或者把0-65535之间的数字转换成汉字或者其他字符
print(chr(20002))  #丢
print('-------------------6-2 把数字（0-65536之间 0-255是ascii）转成字符（字母或者汉字等')

# for i in range(65536):  #把编号是0-65525的字符都输出，前0-255都是ascill
#     print(chr(i),end=' ')

#7 判断是否是ascii中的
# ascii()
print(ascii('a'))  #'a'  如果是ascii表中的，就会返回本身
print(ascii('哈')) #'\u54c8'  如果不是ascii表中的，就会返回\u开头的
print('-------------------7 判断是否是ascii中的')

print('我是运动员')  #我是运动员  这里输出后，两端没有单引号
print(repr('我是运动员'))  #'我是运动员'  这里输出后，两端有单引号

#8字符串原封不动的输出（引号和转义字符都不起作用）
print('我是\运动员')  #我是\运动员 (反斜杠或者捺杠\ 本身是表示转义  \t \n等)
print('我是\\运动员')  #我是\运动员
# 第一个反斜杠表示转义，第二个反斜杠也是转义，负负得正，两个反斜杠表示\这个符号本身（而不是转义的意思）

print(repr('我是\运动员')) #'我是\\运动员'  就是原封不动的输出, 引号和转义字符都不起作用
print(repr('我是\\运动员')) #'我是\\运动员'
# print(type(repr('我是\\运动员'))) #'我是\\运动员'
print('-------------------8 字符串原封不动的输出（引号和转义字符都不起作用）')















