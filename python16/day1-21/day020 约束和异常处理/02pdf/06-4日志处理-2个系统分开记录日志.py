#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 11:37

''''''
'''
需求：如何在2个不同的日志文件中，分贝记录2个子系统的日志

思路：
1、basicConfig是不能实现的，需要借助于FileHandler来实现
2、创建一个操作日志的文件助手对象，依赖FileHandler
3、设置日志格式
4、将日志格式添加到日志对象
5、设置日志级别，返回到操作日志的对象
6、操作日志的对象添加文件助手对象
7、日志对象调error写入提示信息
8、系统2,按照上述步骤复制一份
'''

import logging

# 2、创建一个操作日志的文件助手对象，依赖FileHandler
file_handler1 = logging.FileHandler('c1.log', mode='a', encoding='utf-8')

# 3、设置日志格式
formatter1 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s')

# 4、将日志格式添加到文件助手对象
file_handler1.setFormatter(formatter1)

# 5、设置日志级别，返回到操作日志的对象
logger1 = logging.Logger('系统a', level=40)

# 6、操作日志的对象添加文件助手对象
logger1.addHandler(file_handler1)

# 7、日志对象调error写入提示信息
logger1.error('我是系统a')
print('----------------------------------------1  系统a')

# 2、创建一个操作日志的文件助手对象，依赖FileHandler
file_handler2 = logging.FileHandler('c2.log', mode='a', encoding='utf-8')

# 3、设置日志格式
formatter2 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s')

# 4、将日志格式添加到文件助手对象
file_handler2.setFormatter(formatter2)

# 5、设置日志级别，返回到操作日志的对象
logger2 = logging.Logger('系统b', level=40)

# 6、操作日志的对象添加文件助手对象
logger2.addHandler(file_handler2)

# 7、日志对象调error写入提示信息
logger2.error('我是系统b')
print('----------------------------------------2  系统b')
















