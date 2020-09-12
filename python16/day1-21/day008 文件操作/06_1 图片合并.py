#!/usr/bin/env python
#-*- coding:utf-8 -*-

# path1 = r"D:\xq_py\全栈16\day008 文件操作\ceshi4.png"
path2 = r".\ceshi4.png"
path4 = r".\ceshi6.png"
path3 = r".\ceshi5.png"
#需求：把当前目录下的ceshi4.png和ceshi6.png合并到一个文件   拷贝到当前目录下，改名为ceshi5.png

f = open(path2,mode="rb")  #rb 二进制只读（字节只读，而不是文本）的方式，打开已有图片（指定路径）
f1 = open(path4,mode="rb")
# b: bytes
# 这个时候处理文件的是字节
# 操作非文本文件的时候用带b的
f2 = open(path3,mode="wb") #wb 二进制写（字节写，而不是文本）的方式，打开空图片
for i in f:  #3 循环遍历，已有图片
    f2.write(i) #4 往空图片中，写入已有图片
for i in f1:  #3 循环遍历，已有图片
    f2.write(i) #4 往空图片中，写入已有图片
f.close() #关闭图片文件1
f1.close() #关闭图片文件
f2.flush() #刷新图片文件2
f2.close() #关闭图片文件2

"""
问题：但从文件大小看，已经实现了合并
但是图片最后的效果还看不到合并的效果

"""
















