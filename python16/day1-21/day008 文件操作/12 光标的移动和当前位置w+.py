#!/usr/bin/env python
#-*- coding:utf-8 -*-

path1 = r".\ceshi4.txt"
f = open(path1,mode="w+",encoding="utf-8")
print(f.tell())   #0  打印光标所在位置  0表示文件的开头
f.write("我要多写一点内容")
f.seek(0)
content1 = f.read(1) #   读取一个字符（而不是字节），一个汉字字符是3个字节
print(content1)  #我
print(f.tell())   #3
# f.seek(0)
f.write("呵呵")
f.close()

"""
写读模式下 w+下
1、读取后，当光标回到文件开头的时候，写入2个中文字符，就会把原文件的前2个中文字符覆盖掉--（正常逻辑）
2、读取后，当光标不回到文件开头的时候，写入2个中文字符，就不会出现把原文件的前2个中文字符覆盖掉
   而是在文件最后追加--（注意点）

"""













