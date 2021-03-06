#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/5 17:53
#@author:wangtongpei

''''''
'''
递归
1、递归的概念
    函数自己调用自己，就叫递归
2、递归的深度
    递归的深度最多是998
3、递归的本质
   找到不断在变的东西，递归就写出来了
    比如：每次递归调用都会新生产一个列表（列表的长度是之前的一半）
    比如：每次递归调用，列表的左右边界位置都在变化（两者之差在减半）
'''

def func():
    print('我要递归了')
    func() #递归入口 不带参数
# func() #报错
#RecursionError: maximum recursion depth exceeded while calling a Python object

def func1(n):
    print(n)
    n += 1
    func1(n)   #递归入口，带参数，变动的是n
# func1(0) #报错
#RecursionError: maximum recursion depth exceeded while calling a Python object

#1 递归遍历文件夹
# 将指定文件夹的子文件夹及其子目录都列出来
'''
递归遍历文件夹，伪代码思路
1、定义指定文件夹的相对路径（相对路径便于移植，在其他电脑上运行）
    定义函数，参数是指定文件夹路径
2、列出指定文件夹下的一级子文件夹（不包含二级子文件夹和二级子文件）和一级子文件
3、遍历循环上述步骤2的列表
4、拼接一级子文件夹和一级子文件的全路径（相对路径）
5、判断全路径是否是文件夹
    1、是文件夹，递归调用自己，传入参数全路径
    2、不是文件夹，就是文件，打印文件的全路径

步骤：
1、先实现功能
2、再优化不同层级文件夹的缩进--注意点：每次递归调用一次，层级就+1

小结：
递归的本质和原理
1、递归的本质：不断在变的是子文件夹的全路径和层级
2、递归的本质就是要找出不断在变-每次都在变的是什么
3、递归的入口，递归就是函数内自己调用自己
    形参是一样的，但是每次传递进来的实参是不一样的
    （发现并找到每次传递进来的实参-不同的子文件夹全路径--就是递归的本质）
4、递归入口的参数2：每次递归调用一次，层级就+1
   （也说明了文件夹层级每次递归都不一样）
'''
import os

def recursion_folder(path1,n):
    #参数1：指定文件夹的相对路径
    #参数2：文件夹的层级
    subfolder_li1 = os.listdir(path1) #['002', '003.py', '005.py', '__init__.py']
    #1 列出指定文件夹的一级子文件夹（不包含其二级子文件夹和子文件）和一级子文件，返回列表
    for i in subfolder_li1: #2 遍历循环列表
        full_path = os.path.join(path1,i) #3 拼接一级子文件夹和一级子文件的全路径(相对路径，路径+文件(夹)名字)
        # print(full_path)
        if os.path.isdir(full_path):#4 判断全路径是否是文件夹
            print('\t'*n+i) #5 是的话，打印文件夹名字（非全路径）
            # 文件夹名字（非全路径）前面加上\t制表符-缩进
            #指定文件夹下一级子文件夹前面缩进是0-不缩进-顶格打印
            #指定文件夹下二级子文件夹前面缩进是1，依次类推。。。
            recursion_folder(full_path,n+1) #6 递归入口 函数内自己调用函数自己
            #递归函数参数1：一级子文件夹的全路径（路径前缀+一级子文件夹名字）
            #递归参数2：文件夹层级+1（每次递归调用一次，层级就+1）
            #递归函数：不断在变的是子文件夹的全路径和缩进层级（递归的本质就是要找出不断在变的是什么）--关键点
        else: #5 如果全路径不是文件夹，就是文件
            print('\t'*n+i)#6 打印文件名字（非全路径）
            # 文件名字（非全路径）前面加上\t制表符-缩进
            # 指定文件夹下一级子文件前面缩进是0-不缩进-顶格打印
            # 指定文件夹下二级子文件前面缩进是1，依次类推。。。
            # 注意点：这里隐含一个return  递归的出口

# path1 = r'D:\Program\JetBrains\PycharmProjects\xq_py\全栈16\001'
path1 = r'..\..\001'   #指定文件夹的相对路径
#.\当前目录  ..\上级目录 ..\..\上上级目录  推荐相对目录
n=0 #定义缩进层级
recursion_folder(path1,n)  #调函数

#指定文件夹的目录结构和层级打印
# 002
# 	003
# 		004.py
# 		__init__.py
# 	003.py
# 	__init__.py
# 003.py
# 005.py
# __init__.py










