#!/usr/bin/env python
#-*- coding:utf-8 -*-

path1 = r".\ceshi2.txt"
path2 = r"D:\xq_py\全栈16\day008 文件操作\01 今日内容大纲"   #绝对路径

f = open(path1,mode="w",encoding="utf-8")   #覆盖写  #注意点1  写的模式，只能写，不能读read,读的时候会报错
# f = open(path1,mode="w",encoding="gbk")
"""
这里是encoding="utf-8"，新建的一个文件，打开当前目录下文件ceshi2.txt的时候，也需要用utf-8的方式打开
如果用别的方式，比如gbk，就会显示乱码（notepad++是utf-8，这个可以自己设置）

这里如果是encoding="gbk"，新建的一个文件，打开当前目录下文件ceshi2.txt的时候，也需要用gbk的方式打开
如果用别的方式，比如utf-8，就会显示乱码（自带记事本是gbk，和中文操作系统保持一致）
"""
# f = open(path1,mode="w",encoding="gbk")
# 'w'       open for writing, truncating the file first
# Other common values are 'w' for writing (truncating the file if
#     it already exists)
f.write("哈哈哈\n")  #参数是字符串，往文件中写入字符串   写入多行  换行符是\n
f.write("娃哈哈\n")  #参数是字符串，往文件中写入字符串（
# 每次写入字符串的时候，如果文件已经存在，就会把之前的文件内容完全覆盖--就是先清空，后写入新的内容  w w+ wb都适用覆盖）
f.flush() #刷新
# 类比：往文件写内容就好比，把文件当做一个容器-杯子，写内容就是给杯子插根管子倒水进去
# 内容写入完毕了就是水倒完了，但是管子里还会残留一点水，这个flush就是把管子里面残留的水，都全部推入杯子中
f.close() #关闭文件













