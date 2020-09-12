#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
@author: jack
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: cn5036520@163.com
@software: sign
@file: logs3.py
@time: 2019/4/4 5:58
@desc:
'''


"""
思路：
0、导包
    日志级别
1、新建对象-日志的父类
    设置日志父类对象的日志级别
2、新建对象-文件handler
    设置文件handler对象的日志级别
3、新建对象-控制台handler
    设置控制台handler对象的日志级别
4、设置日志格式
    日志格式生效
5、将文件handler和控制台handler会报给大领导-日志父类对象
6、定义日志的自定义消息--日志格式中的message
"""

import logging
import os

# 日志级别 CRITICAL(FATAL)>ERROR>WARN(WARNING)>INFO>DEBUG  #日志级别必须是大写字母
            #          50>40   >30          >20   >10

# 1、新建对象-日志的父类
#     设置日志父类对象的日志级别
# logger1 = logging.getLogger()
logger1 = logging.getLogger("my_logger1")
logger1.setLevel(20)
# logger1.setLevel(logging.INFO)

# 2、新建对象-文件handler
#     设置文件handler对象的日志级别
path1 = r"D:\PycharmProjects\xiaoqiang\base_181027\a1接口层框架设计1-0326\src34\logs\log32.txt"
fh1 = logging.FileHandler(path1)
fh1.setLevel(30)
# fh1.setLevel(logging.INFO)

# 3、新建对象-控制台handler
#     设置控制台handler对象的日志级别
sh1 = logging.StreamHandler()
sh1.setLevel(30)
# sh1.setLevel(logging.INFO)

# 4、设置日志格式
#     日志格式生效
# log_format1 = "%(asctime)s || %(filename)s || [lineno:%(lineno)s] || %(levername)s || %(message)s "
#  #注意：   levername拼写错误，应该是levelname   这里最好通过复制粘贴Formatter类源码的写法，避免拼写错误
# 报错 KeyError: 'levername'
# Logged from file logs32.py, line 73
log_format1 = "%(asctime)s || %(filename)s || [lineno:%(lineno)s] || %(levelname)s || %(message)s "
formatter1 = logging.Formatter(log_format1) #日志格式生效

fh1.setFormatter(formatter1)  #给文件handler设置日志格式
sh1.setFormatter(formatter1)    #给控制台handler设置日志格式

# 5、将文件handler和控制台handler会报给大领导-日志父类对象
logger1.addHandler(fh1)
logger1.addHandler(sh1)

# 6、定义日志的自定义消息--日志格式中的message
# logger1.error("打印详细错误信息")  #对应日志格式中的message
# logger1.error("打印具体的日志error错误信息")
# logger1.debug("打印具体的日志debug调试信息")
logger1.info("打印具体的日志info信息")
# logger1.warn("打印具体的日志warn信息")
# logger1.critical("打印具体的日志critical信息")

"""
总结：
1、关于日志级别，当父类的日志级别和子类（文件handler、控制台handler）不同的时候
    哪个日志级别严格（数字更大的为准），以哪个为准
    例如1：父类的日志级别是20--INFO
          子类-文件handler的日志级别设置是30-WARN
          此时，WARN级别的日志可以输出，而INFO级别的日志无法输出
     例如2：父类的日志级别是30--WARN
          子类-文件handler的日志级别设置是20-INFO
          此时，WARN级别的日志可以输出，而INFO级别的日志无法输出

"""























