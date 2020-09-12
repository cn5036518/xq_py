#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/16 9:11

''''''
'''
需求：
1、系统a的错误日志写到文件a，系统b的错误日志写到文件b
2、系统a的错误类型1写到文件a1，
   系统a的错误类型2写到文件a2，
   系统b的错误类型1写到文件b1，
   系统a的错误类型2写到文件b2

思路
1、创建一个操作日志的对象logger（依赖FileHandler）
2、设置日志文件的显示格式
3、写日志
'''

import logging


#一、系统a的日志
# 1、创建一个操作日志的对象logger（依赖FileHandler）
file_handler = logging.FileHandler('a.log',mode='a',encoding='utf-8')

# 2、设置日志文件的显示格式
formatter = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s')
# 2020-06-18 08:17:09,356-a-ERROR-07_3日志处理3_多文件-我是a系统
file_handler.setFormatter(formatter) #将日志格式关联到日志对象

#设置系统a的日志级别
logger1 = logging.Logger('a',level=40)
logger1.addHandler(file_handler)  #将日志对象关联到日志级别

# 3、写日志
logger1.error('我是a系统')

#二、系统b的日志
# 1、创建一个操作日志的对象logger（依赖FileHandler）
file_handler2 = logging.FileHandler('b.log',mode='a',encoding='utf-8')

# 2、设置日志文件的显示格式
formatter2 = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s')
# 2020-06-18 08:17:09,356-a-ERROR-07_3日志处理3_多文件-我是a系统
file_handler2.setFormatter(formatter2) #将日志格式关联到日志对象

#设置系统a的日志级别
logger2 = logging.Logger('b',level=40)
logger2.addHandler(file_handler2)  #将日志对象关联到日志级别

# 3、写日志
logger2.error('我是b系统')







































