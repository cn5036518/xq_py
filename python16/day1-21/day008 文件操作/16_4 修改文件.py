#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：将文件alex2.txt中的sb批量修改成good
"""
思路：
1、打开文件对象1-读，循环遍历对象1，将每一行-字符串replace，形成新字符串s2
2、打开文件对象2-写，循环遍历对象2，将s2依次写入

注意点：
步骤：
1、先完成文件1的副本 文件2的修改
2、然后完成删除文件1，将文件2重命名为文件1
"""

import os

path1 = r".\alex2.txt"
path2 = r".\alex3.txt"
with open(path1,mode="r",encoding="utf-8") as f1,\
    open(path2,mode="w",encoding="utf-8") as f2:   #这里的\表示换行，上下两行表示同一行代码
    for i in f1:
        i2 = i.replace("sb","good")  #字符串的内置方法对字符串本身没有任何修改  #批量修改-内存中
        # S.replace(old, new[, count]) -> str
        # Return a copy of S with all occurrences of substring
        # old replaced by new.  If the optional argument count is
        # given, only the first count occurrences are replaced.
        f2.write(i2)  #批量写入，一次只写入一行
os.remove(path1)  #删除文件1
os.rename(path2,path1)  #文件2重命名成文件1  参数1是文件2，参数2是文件1
# rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
#     Rename a file or directory.













