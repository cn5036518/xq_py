#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：如何把文件1中的内容good批量替换成sb

"""
思路：
1、打开一个文件对象1，只读
   打开一个文件对象2，只写（副本文件）
2、循环遍历对象1
3、过程中，替换每一行字符串中的good，改成sb---replace方法
4、将产生的新字符串，逐行写入新的文件--文件write方法
步骤：
1、先实现文件1中读取，读取到的每一行字符串，进行替换，替换后，写入新的文件2--ok
2、再实现，文件1删除，将文件2重命名成文件1-ok

"""

import os
import time

path1 = r".\alex.txt"
path2 = r".\alex2.txt"
# f = open(path1,mode="r",encoding="utf-8")
# f.flush()
# f.close()

with open(path1,mode="r",encoding="utf-8") as f1,\
    open(path2,mode="w",encoding="utf-8") as f2:  #打开两个对象，对象1用于读，对象2用于写
    #with 打开文件，关闭前，会自动flash。自动关闭
    for i in f1: #0 遍历对象1
        # print(i)
        i2 = i.replace("good","sb")  #1 替换每一行，返回新字符串 关键点1  必须掌握
        # 参数1是old 参数2是new，参数3不写，默认替换old左边第一次出现的时候
        #  S.replace(old, new[, count]) -> str
        #
        # Return a copy of S with all occurrences of substring
        # old replaced by new.  If the optional argument count is
        # given, only the first count occurrences are replaced.
        f2.write(i2)  # 对象2中写入新的字符串（一行就是一个新的字符串）

time.sleep(5)  #注意：文件1的删除和文件2的重命名在pycharm是看不到这个过程中，
# 但是可以在路径 D:\xq_py\全栈16\day008 文件操作  看到这个删除和重命名过程
os.remove(path1)   #1 删除文件1(alex.txt)
# remove(path, *, dir_fd=None)
#     Remove a file
time.sleep(5)
os.rename(path2,path1)  # 2 重命名  将文件2(alex2.txt) 重命名 为文件1（alex.txt）
# rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
#     Rename a file or directory.











