#!/usr/bin/env python
#-*- coding:utf-8 -*-

#相对路径  用的更多（绝对路径只能在自己电脑运行，一旦发给别人，绝对路径就无法运行了，但是相对路径是通用的）
# 绝对路径 --路径是写死的
# 相对路径 --路径没有写死，可以通用
path1 = r"..\002\003.txt"  #这里的..\表示的当前目录的上一级目录，前面带r不转义就是\，如果不带r就是/
path2 = r"..\..\day005 字典\01 今日内容大纲.py"
##这里的..\..\表示的当前目录的上2级目录

# f = open(path1,mode="r",encoding="utf-8")
f = open(path2,mode="r",encoding="utf-8")
#pycharm中新建的txt文件的默认编码方式是：utf-8
ret1 = f.read()
print(ret1)  #haha 哈哈











