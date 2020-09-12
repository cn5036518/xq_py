#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
内存中是unicode
传输或者存储在硬盘是utf-8

ascii  8位-bit 1个字节  英文大小写字母、数字、特殊字符
gbk    16位-bit 2个字节  中文、日文、韩文、繁体中文，兼容ascii
unicode 32位-bit 4个字节  包含全世界所有国家的所有字符
utf-8  可变长度的unicode
    1、英文字符 8位 1个字节
    2、欧洲字符 16位 2个字节 （德文、法文、西班牙文、拉丁文）
    3、中文字符 24位 3个字节
"""

#1编码
#将unicode转成utf-8  str变成bytes类型  （编码-加密-压缩）
s1 = "祖国"  #看到的是unicode
b1 = s1.encode("utf-8")  #参数为空，默认是"utf-8"
print(b1)  #b'\xe7\xa5\x96\xe5\x9b\xbd'
#在utf-8下，一个汉字字符是3个字节 2个汉字，一共是6个字节

#2解码
#将utf-8转成unicode   bytes变成str类型  （解码-解密-解压）
b2 = b'\xe7\xa5\x96\xe5\x9b\xbd'
s2 = b2.decode("utf-8") #参数为空，默认是"utf-8"
print(s2) #祖国

#3编码
#将unicode转成gbk   str变成bytes类型  （编码-加密-压缩）
s3 = "祖国"  #看到的是unicode
b3 = s3.encode("gbk")  #参数为空，默认是"utf-8"，这里指定gbk
print(b3)  #b'\xd7\xe6\xb9\xfa'
#在gbk下，一个汉字字符是2个字节 2个汉字，一共是4个字节

#4解码
#将gbk转成unicode   bytes变成str类型  （解码-解密-解压）
b4 = b'\xd7\xe6\xb9\xfa'
s4 = b4.decode("gbk") #参数为空，默认是"utf-8" 这里指定是gbk，如果指定utf-8，就报错
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd7 in position 0: invalid continuation byte
print(s4) #祖国
print("---------------4")

#5将gbk转换成utf-8  无法直接转，key通过unicode中转
#01先把gbk转成unicode（解码）
b5 = b'\xd7\xe6\xb9\xfa'
s5 = b5.decode("gbk")  #参数不写默认是utf-8 这里指定 gbk
print(s5) #祖国
#在gbk下，一个汉字字符是2个字节，2个汉字，就是4个字节

#02 再把unicode转成utf-8（编码）
b6 = s5.encode("utf-8") #参数不写默认是utf-8
print(b6)  #b'\xe7\xa5\x96\xe5\x9b\xbd'
#在utf-8下，一个汉字字符是3个字节，2个汉字，就是6个字节


















