#!/usr/bin/env python
#-*- coding:utf-8 -*-

path1 = r".\ceshi3.txt"
path2 = r"D:\xq_py\全栈16\day008 文件操作\01 今日内容大纲"   #绝对路径

f = open(path1,mode="a",encoding="utf-8")  #追加模式  #追加也是只能追加的模式，不能读read 读的时候回报错
# 'a'       open for writing, appending to the end of the file if it exists
# 每次打开文件写入的时候，不会全部清空，而是每次都往文件末尾追加新的内容（适合写日志文件）
f.write("第一行\n")  #追加写
f.write("第二行\n")
f.flush()
f.close()

"""
模式总结
r 只读 只能读，不能写
w 写   只能写，不能读
a 追加 只能追加，不能读（追加也是写）

"""















