#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@author: jack
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: cn5036520@163.com
@software: sign
@file: 0319-1日志-输出到控制台.py
@time: 2018/12/23 6:46
@desc:
'''

import logging
import os
"""
日志级别等级 CRITICAL>ERRORS>WARNING>INFO>DEBUG
"""

#1 创建一个logger（父类）
logger = logging.getLogger("my_logger1")  #1创建父类，参数可以自定义
logger.setLevel(logging.INFO)  #2 设置父类日志级别

#2 创建一个文件handler，将log写入文件
log_file = os.path.join(os.getcwd(),"wlog3.log")
#1 先获取当前目录的绝对路径，拼接当前目录的绝对路径和文件名"wlog3.log",形成文件的全路径
fh1 = logging.FileHandler(log_file)
fh1.setLevel(logging.INFO)  #2 设置子类-文件handler日志级别

#3 创建一个控制台handle，将log输出到控制台
sh1 = logging.StreamHandler()
sh1.setLevel(logging.INFO) #1 设置子类-控制台handler日志级别

#4 设置输出格式
log_format = "%(asctime)s || %(filename)s || [line:%(lineno)s] || %(levelname)s || %(message)s"  #
# 1固定写法 日志输出格式定义，只是定义，但是并没有生效
formatter1 = logging.Formatter(log_format) #2 日志格式的生效
fh1.setFormatter(formatter1) #3 文件handler的日志格式生效
sh1.setFormatter(formatter1) #4 控制台handler的日志格式生效

#5 把handler添加到logger，理解为汇报给大领导
logger.addHandler(fh1)
logger.addHandler(sh1)

#6 定义日志的message
logger.error("雾霾啊")  #定义日志的message（ 对应%(message)s"）

"""
思路：
1、创建一个logger（父类）
2、创建一个文件handler，将log写入文件
3、创建一个控制台handler，将log输出到控制台
4、设置日志输出格式
5、把两个handler分别添加到logger（父类）--理解为汇报给大领导
6、定义日志的message

"""





























