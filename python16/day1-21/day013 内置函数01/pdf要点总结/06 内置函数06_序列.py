#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/31 16:44
#@author:wangtongpei

#list()
s1 = 'jack'  #将字符串等可迭代对象-iterable转换成列表
print(list(s1)) #['j', 'a', 'c', 'k']
print('----------------------1 list()')

#2 tuple()
s1 = 'jack'  #将字符串等可迭代对象-iterable转换成元组
print(tuple(s1)) #('j', 'a', 'c', 'k')
print('----------------------2 tuple()')

#3 reversed()
#1 将列表反转
li1 = [1,3,2]
it1 = reversed(li1)  #将可迭代对象-iterable的元素进行反转（注意：反转不是倒序）
print(it1)  #<list_reverseiterator object at 0x000000A953FBB408>
print(list(it1))  #[2, 3, 1]  #迭代器转换成列表
print('----------------------3-1 reversed()')

#2 将字符串反转
s1 = 'jack'
it1 = reversed(s1)  #将可迭代对象-iterable的元素进行反转（注意：反转不是倒序）
print(it1)  #<list_reverseiterator object at 0x000000A953FBB408>
li3 = list(it1)  #['k', 'c', 'a', 'j']  #迭代器转换成列表
print(li3)
s3 = ''.join(li3)
print(s3)  #kcaj
print('----------------------3-2 reversed()')

#4 切片
s1 = 'jacktom'
print(s1[1:5:2])  #ak
print(s1[::-1])  #print(s1[::-1])  字符串反转

li1 = [1,2,3,4,5,6]
print(li1[1:5:2])  #[2, 4]
print(li1[::-1])  #[6, 5, 4, 3, 2, 1]  列表进行反转
print('----------------------4 切片')

'''
字符串或者列表反转
方法1：  最简洁
s1[::-1]
li1[::-1]

方法2：
reversed(li1)
reversed(s1)
'''

#5 str()
dic1 = {'name':'jack','age':18}
print(str(dic1))  #{'name': 'jack', 'age': 18}  将字典转换成字符串形式--json字符串
print(type(str(dic1)))  #<class 'str'>
print('----------------------5 str()')

#6 format（）
#01 字符串
print(format('jack','<20')) #字符串左对齐，一共是20个字符
print(format('jack','>20')) #字符串右对齐，一共是20个字符
print(format('jack','^20')) #字符串居中对齐，一共是20个字符，jack左右各8个字符
print('----------------------6-1 format() 字符串')

#02 数值--进制转换
print(format(3,'b'))  #11 十进制数字3转换成二进制数字11的字符串形式
print(type(format(3,'b'))) #<class 'str'>
print(format(8,'o'))  #10 十进制数字8转换成八进制数字10的字符串形式
print(format(16,'x')) #10 十进制数字16转换成十六进制数字10的字符串形式
print(format(15,'X')) #F 十进制数字15转换成十六进制数字F（大写的）
print(format(97,'c')) #a  十进制数字97转换成ascii码表（ascii属于unicode）中的字母
print('----------------------6-2 format() 进制转换')

#03 浮点数--小数
print(format(1.2354,'0.2f'))  #1.24  保留2位小数，四舍五入
print(type(format(1.2354,'0.2f')))  #<class 'str'>
print(format(12345678,'e'))  #1.234568e+07 科学计数法（默认保留6位小数）
print(format(1235567,'0.2e'))  #1.24e+06 科学计数法（保留2位小数，e小写）
print(format(1235567,'0.2E'))  #1.24E+06 科学计数法（保留2位小数，e大写）
print('----------------------6-3 format() 小数')

#bytes()
#把字符串转换成字节(utf-8编码)
s1 = '你好'
s2 = 'jack'
li1 = [1,2,3]
print(bytes(s1,encoding='utf-8'))  #b'\xe4\xbd\xa0\xe5\xa5\xbd' b开头表示字节
#一个汉字（中文字符）是3个字节--utf-8中
print(bytes(s2,encoding='utf-8')) #b'jack'
#一个英文字母是一个字节--utf-8中
print(bytes(li1))  #b'\x01\x02\x03'
print('----------------------7-1 bytes()')

b1 = s1.encode()  #这里参数不写，默认是'utf-8'
print(b1)  #b'\xe4\xbd\xa0\xe5\xa5\xbd'
#将中文字符串转换（编码-压缩-加密）成字节（utf-8)
#中文字符串就是明文，字节就是密文

s11 = b1.decode() #这里参数不写，默认是'utf-8'
print(s11)  #你好
#将字节(utf-8)转换（解码-解压缩-解密）成中文字符串
print('----------------------7-2 bytes()')

#bytesarray()函数
s1 = '你好'
ret = bytearray(s1,encoding='utf-8')
print(ret)  #bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd')
print('----------------------8 bytesarray()')

#9 memoryview()函数
#查询字符串对应的字节（utf-8）在内存的地址
s1 = 'jack'
print(memoryview(s1.encode('utf-8')))
# print(memoryview(s1)) #报错 TypeError: memoryview: a bytes-like object is required, not 'str'
#<memory at 0x0000003D28B881C8>
print('----------------------9 memoryview()')

#10 ord()函数
print(ord('a')) #97  #字母a的ascii是97
print(ord('一')) #19968  #中文字符‘一’对应的utf-8的字符编码的位置是19968
# print(ord('一期')) #报错 TypeError: ord() expected a character, but string of length 2 found
print('----------------------10 ord()')

#11 chr()函数
print(chr(65))  #A  ascii中65对应的字符是'A'
print(chr(19968))  #一 字符编码位置是19968对应的字符是'一'
print('----------------------11 chr()')

#12 ascii()函数
#参数是ascii表中的字符，就返回参数本身；参数不是ascii表中的字符，就返回\u开头
print(ascii('a'))  #'a'
print(ascii('ab'))  #'ab'
print(ascii('一')) #'\u4e00'
print('----------------------12 ascii()')

#13 repr函数
s1 = '祖国'
print('我爱%s' % s1)  #我爱祖国  占位符
print('我爱%r' % s1) #我爱'祖国' 原封不动的输出

print('大家好,\n \t 我是jack')
# 大家好,
#  	 我是jack
print(repr('大家好,\n \t 我是jack'))
#'大家好,\n \t 我是jack'   原封不动的输出，引号和转义符都原样输出
print('----------------------13-1 repr()')

s1 ='jack'   #字符串
print(s1) #jack  不带引号
print(type(s1))  #<class 'str'>
print(repr(s1)) #'jack'  带引号
print(type(repr(s1)))  #<class 'str'>
print('----------------------13-2 repr()')



















