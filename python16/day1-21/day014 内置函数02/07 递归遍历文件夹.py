#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/2 17:09
#@author:wangtongpei

#需求 遍历文件夹中所有的子文件夹及子文件--用递归实现

''''''
'''
伪代码
1、遍历根目录--listdir  for
   得到第一级子文件夹（不包含子文件夹的子文件）和文件
2、判断是文件还是文件夹
    如果是文件，就直接打印文件名
    如果是文件夹（全路径才行），就自己调用自己（递归）

步骤：
1、先实现功能
2、然后进行优化--每一级目录的缩进打印
'''
import os

# path1 = r'D:\Program\JetBrains\PycharmProjects\xq_py\全栈16\001'  #绝对路径
path1 = r'..\001'  #相对路径，..\表示当前目录的上一级目录  .\表示当前目录   #推荐

def for_file(path1,n): #参数1是文件夹路径的根目录，参数2是用于调整层级缩进的
    li1 = os.listdir(path1) #1 列出根目录下第一层级的文件夹（不包含其子文件夹和子文件）和文件，返回列表
    # print(li1)  #['002', '003.py', '005.py', '__init__.py']
    for i in li1: # 2遍历循环列表，打印第一次层级的文件夹和文件
        full_path1 = os.path.join(path1,i) #3 拼接第一层级的文件夹的全路径
        # print(full_path1)
        if os.path.isdir(full_path1): #4判断全路径是否是文件夹
            print('\t'*n+i) # 4-2 全路径是文件夹的话，打印文件夹的名字（文件夹的名字打印不需要全路径）
            for_file(full_path1,n+1)  #自己调自己  #5全路径是文件夹的话，自己调用自己--递归
            #把第一层级的文件夹当做根目录，
            #注意：1递归的时候，文件夹必须是全路径，而不能是文件夹名字
                  #2 这个递归的出口，在for循环结束后，默认return的None
            #参数2 n+1表示每次递归的时候，缩进都会增加1
        else: #6 全路径不是文件夹的话，就是文件，打印文件的名字即可（文件的名字打印不需要全路径）
            print('\t'*n+i) #6-2 '\t'表示tab制表符-4个空格的缩进
            #这里的i是文件名字，应用场景，如果存在病毒攻击，open这个i后，写入一个数字1，就会把所有的文件都清空，然后写入1
            #批量修改文件的一个方式，强烈不推荐，等同于病毒攻击（清空并且篡改文件）
            #专业数据恢复，一个文件2元钱

for_file(path1,1) #7 调用函数，参数1是文件夹根目录的全路径（可以是绝对路径，也可以是相对路径-推荐）
#参数2是用于调整层级缩进的
#根目录下的文件夹（包含其子文件夹和子文件）和文件的层级缩进图
	# 002
	# 	003
	# 		004.py
	# 		__init__.py
	# 	003.py
	# 	__init__.py
	# 003.py
	# 005.py
	# __init__.py













