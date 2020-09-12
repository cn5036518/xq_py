#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/8/18 17:58

import os

'''
一、目录操作  增删改查
#1 创建目录
   1创建单个目录
   2创建多级目录
#2 删除目录
#3 修改目录
   1切换目录
   2修改目录的名字
#4 查看目录
    1获取当前工作目录
    2查看指定目录的属性

二、文件操作
1、新增文件
2、删除文件
3、修改文件-重命名文件
4、查看文件属性

三、shell命令
1、直接执行shell命令
2、通过变量保存命令执行结果

四、文件路径的操作
1、返回绝对路径
2、将路径和文件名分开

'''

#1 创建目录
#1-1 创建单级目录
# os.mkdir('test1')  #当前目录新建一个文件夹'test1'

#1-2 创建多级目录
# os.makedirs(r'test1/test2') #一次创建多级目录  和shell的mkdir -p类似
# os.makedirs('test2/test2')

#2 删除目录
# os.rmdir('test1/test2')  #删除当前目录下的文件夹（目录）'test1'
# 目录下面不能有子目录或者子文件，否则删除失败

#3 修改目录
#3-1 切换目录
# os.chdir(r'E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\a')   #绝对路径
# os.chdir(r'..\a')   #相对路径   #E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\a
# os.chdir(r'..')   #相对路径  #E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time
#Change the current working directory to the specified path

#3-2 修改目录的名字
# os.rename('test1','test3')  #参数1是老目录的名字，参数2是新目录的名字

#4 查看目录
#4-1 获取当前工作目录
# print(os.getcwd())  #输出当前文件所在的目录的绝对路径
#Return a unicode string representing the current working directory
#E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\pdf

#4-2 获取指定目录的属性
# print(os.stat('test3'))
#os.stat_result(st_mode=16895, st_ino=28710447624581126, st_dev=3877199136, st_nlink=1, st_uid=0,
# st_gid=0, st_size=0, st_atime=1597748408, st_mtime=1597748408, st_ctime=1597748250)

# 二、文件操作
# 1、新增文件  open
# f = open('001',mode='w',encoding='utf-8')  #写的模式新建一个文件
# 2、删除文件
# os.remove('001')  #删除当前目录下的指定文件
#Remove a file (same as unlink())

# 3、修改文件-重命名文件
# os.rename('001','002')  #参数1是老文件名字，参数2是新文件名字
#Rename a file or directory.

# 4、查看文件属性
# print(os.stat('002'))
#os.stat_result(st_mode=33206, st_ino=4222124650755317, st_dev=3877199136,
# st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1597750387, st_mtime=1597750387, st_ctime=1597750299)
#Perform a stat system call on the given path

#三 执行shell命令
#1  直接执行shell命令
# os.system('mkdir test4')  #这里单引号之间，可以直接写shell命令
# os.system('more 001')  #122 直接在控制台输出命令执行结果，直接显示
# Execute the command in a subshell.

#2 执行shell命令，把结果保存到变量中
result = os.popen('more 002').read()  #将命令的输出结果，读取后，存到变量result中
print(result)

# 四、文件路径的操作
# 1、返回绝对路径
print(os.path.abspath('.'))
#E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\pdf
print(os.path.abspath('..'))
#E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time
print('------------------------------------------1返回绝对路径')

# 2、将路径和文件名分开
path1 = r'E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\pdf\1.py'
base,file = os.path.split(path1)
print(base) #E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\pdf  路程
print(file) #1.py  文件名
print('------------------------------------------2 一次返回路径和文件名的元组')

print(os.path.dirname(path1))
#E:\xq_py\全栈16\day22-40\day22 常用模块01 random collection time\pdf  文件的路径
print(os.path.basename(path1))
#1.py  文件名
print('------------------------------------------3 分别返回路径和文件名')









