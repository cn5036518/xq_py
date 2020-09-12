#!/usr/bin/env python
#-*- coding:utf-8 -*-

# path1 = r"D:\xq_py\全栈16\day008 文件操作\ceshi4.png"
path2 = r".\ceshi4.png"
path3 = r".\ceshi5.png"
# path4 = r"https://f10.baidu.comit/u=4006599455,1715004216&fm=72"
#需求：把当前目录下的ceshi4.png拷贝到当前目录下，改名为ceshi5.png
#  不仅仅可以拷贝图片文件（rb wb），也可以用来拷贝文本文件（r w）-压缩文件（rb wb）等其他任何类型的文件
"""
思路：
1、把当前目录下的ceshi4.png文件打开，保存在f中，模式是rb（这个图片文件是已有的）
2、把当前目录下的ceshi5.png文件打开，保存在f2中，模式是wb（这个图片文件是新建的）
3、循环遍历对象f，过程中，往f2中write写入已有图片内容   f2.write(i)
4、从而实现图片文件的拷贝
"""

f = open(path2,mode="rb")  #rb 二进制只读（字节只读，而不是文本）的方式，打开已有图片（指定路径）
# f = open(path2,mode="r")  # r是错误的 必须是rb才行
# gbk utf-8编码方式都是针对文本的（r），针对图片（rb）是无效的  注意点1
# 一旦是rb带了b字节，就不用指定任何文本编码方式了

# b: bytes
# 这个时候处理文件的是字节
# 操作非文本文件的时候用带b的
f2 = open(path3,mode="wb") #wb 二进制写（字节写，而不是文本）的方式，打开空图片
# f2.write(f.read())   #注意点：这么写可以，但是缺点是f文件很大的时候，会出现内存溢出，内存爆了的情况

for i in f:  #3 循环遍历图片文件，已有图片  （文本文件等其他类型的文件，也可以通过这个方式来拷贝，f读取一行，f2写一行）
    f2.write(i) #4 往空图片中，写入已有图片   --关键点1 必须掌握
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0xd5 in position 23: illegal multibyte sequence
f.close() #关闭图片文件1
f2.flush() #刷新图片文件2
f2.close() #关闭图片文件2

"""
模式总结
一、文本操作
r 只读 只能读，不能写
w 写   只能写，不能读
a 追加 只能追加，不能读（追加也是写）

二、非文本操作（jpg、png图片，mp3音频、mp4-avi视频，压缩包等）
b: bytes
这个时候处理文件的是字节
操作非文本文件的时候用带b的

rb  二进制只读（字节只读）
wb  二进制写（字节写）
ab  二进制追加（字节追加）

"""












