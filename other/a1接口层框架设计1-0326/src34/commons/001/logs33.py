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
    logging
    os
    定义日志级别
1、新建父类日志对象
    设置父类的日志级别
2、新建文件handler日志对象
    设置文件handler的日志级别
3、新建控制台handler日志对象
    设置控制台handler的日志级别
4、定义日志的格式
    让父类日志格式生效--根据类的源代码复制过来（避免拼写错误）
    让文件handler日志格式生效
    让控制台handler日志格式生效
5、让文件handler添加到父类
    让控制台handler添加到父类--理解为汇报为大领导
6、自定义错误信息--日志格式中的message
"""

import logging
import os

#日志级别   大写字母 CRITICAL(FATAL)>ERROR>WARN(WARNING)>INFO>DEBUG
                    #       50    >40   >30           >20  >10
#注意：父类和文件handler、控制台都设置了日志级别的情况下
    #如果父类和子类设置的不一样，哪个日志级别严格（数值更大），就按照哪个


# 1、新建父类日志对象
#     设置父类的日志级别
logger1 = logging.getLogger()
logger1.setLevel(20)
# logger1.setLevel(logging.INFO)

# 2、新建文件handler日志对象
#     设置文件handler的日志级别
path1 = r"D:\xq_py\a1接口层框架设计1-0326\src34\logs\logs33.txt"
fh1 = logging.FileHandler(path1)
fh1.setLevel(20)

# 3、新建控制台handler日志对象
#     设置控制台handler的日志级别
sh1 = logging.StreamHandler()
sh1.setLevel(20)

# 4、定义日志的格式
#     让父类日志格式生效--根据类的源代码复制过来（避免拼写错误）
#     让文件handler日志格式生效
#     让控制台handler日志格式生效
# format1 = "%s || %s || %s || %s || %s"
# format1 = "%(时间)s || %(文件名)s || %(行号)s || %(日志级别)s || %(错误信息)s"
format1 = "%(asctime)s || %(filename)s || [line:%(lineno)s] || %(levelname)s || %(message)s"
# format1     = "%(asctime)s || %(filename)s || [line:%(lineno)s]    || %(levelname)s || %(message)s"

# 注意：[line:%(lineno)s] 这里的拼写错误
# log_format1 = "%(asctime)s || %(filename)s || [line:%(lineno)s]   || %(levelname)s || %(message)s"
formatter1 = logging.Formatter(format1)
# print(formatter1)  #<logging.Formatter object at 0x00000000026036D8>
# print(type(formatter1))  #<class 'logging.Formatter'>
fh1.setFormatter(formatter1)  #文件handler对象，调方法，传入参数
sh1.setFormatter(formatter1)

# 5、让文件handler添加到父类
#     让控制台handler添加到父类--理解为汇报为大领导
logger1.addHandler(fh1)
logger1.addHandler(sh1)

# 6、自定义错误信息--日志格式中的message
logging.error("打印日志错误-ERROR信息")
# logging.info("打印日志INFO信息")
# logging.debug("打印日志DEBUG信息")
# logging.warning("打印日志WARNING信息")
# logging.critical("打印日志CRITICAL信息")

























