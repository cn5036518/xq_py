#!/usr/bin/env python
#-*- coding:utf-8 -*-

path1 = r".\ceshi4.txt"
f = open(path1,mode="r",encoding="utf-8")
print(f.tell())   #0  打印光标所在位置  0表示文件的开头
content1 = f.read(1) #读取一个字符（而不是字节），一个汉字字符是3个字节
print(content1)  #疙
print(f.tell())  #3  tell函数返回的是当前光标的位置，单位是字节，而不是字符--注意点
# 因为utf-8下，一个汉字字符是3个字节，read函数的参数1表示一个字符

f.close()

"""
字节和字符的总结：
1、read函数的参数，单位是字符
2、tell函数返回的，单位是字节（utf-8下，一个中文字符是3个字节）
    所以，文件内容全部是中文字符的情况下，tell函数返回的都是3的倍数
"""













