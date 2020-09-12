#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
11，写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。
"""

'''
目的：
读题，可以实现修改任何文件中的任何内容
即：win下，打开文本文件后，ctrl+h实现的功能

思路：
1、同时打开2个文件
   读取文件1的内容，修改文件1的内容后-relace，将修改后的内容写入到文件2
2、删除文件1
   将文件2的名字重命名成文件1
3、从而实现对文件1的修改
'''

import os
def modify(file_name,old,new):  #参数1是文件名，参数2是老的内容，参数3是新的内容
    with open(file_name,mode='r',encoding='utf-8') as f1,\
        open(file_name+'_副本',mode='w',encoding='utf-8') as f2:  #1同时打开两个文件，文件1读，文件2写
        for i in f1: #2 遍历循环文件1
            line1 = i.replace(old,new)  #3注意点 replcae不会修改字符串本身，会产生新的值，存入新的变量

            #4 把文件1中的每一行中的old（'hello'）修改成new('bye')
            f2.write(line1) #5把替换后的每行依次写入到文件2
    os.remove(file_name)  #6删除文件1
    os.rename(file_name+'_副本',file_name)  #7重命名文件2的名字，变成文件1

modify('001.txt','bye','bye2')
#把文件名是'001.txt'文件中的‘hello’修改成‘bye’
#即实现把指定文件中的指定内容‘hello’批量替换成‘bye’   #win下，打开文本文件后，ctrl+h实现的功能








