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
    定义日志级别  全部大写字母
1、新建父类日志对象
    给父类对象设置日志级别
2、新建子类-文件handler对象
    给文件handler对象设置日志级别
3、新建子类-控制台handler对象
    给控制台handler对象设置日志级别
4、设置日志的打印格式
    日志格式在父类生效--方法
    日志格式在子类-文件handler生效--方法
    日志格式在子类-控制台handler生效
5、将子类-文件handler对象添加到父类对象
   将子类-控制台handler对象添加到父类对象
6、自定义错误信息--对应日志格式的message

注意点：
1、日志格式的设置，注意拼写
2、日志级别的优先级
    当父类对象和子类对象-文件handler和控制台handler不一样的时间
    哪个严格（日志级别数值更大的），就用哪个
"""

import logging
import os

#日志级别 大写字母 CRITICAL(FATAL) > ERROR > WARN(WARNING) > INFO > DEBUG
#                       50       > 40    > 30            > 20   > 10


# 1、新建父类日志对象
#     给父类对象设置日志级别
logger1 = logging.getLogger()
logger1.setLevel(20)
# logger1.setLevel(logging.INFO)

# 2、新建子类-文件handler对象
#     给文件handler对象设置日志级别
path1 = r"D:\xq_py\a1接口层框架设计1-0326\src34\logs\logs35.txt"  #定义日志文件的绝对路径
fh1 = logging.FileHandler(path1)
fh1.setLevel(20)

# 3、新建子类-控制台handler对象
#     给控制台handler对象设置日志级别
sh1 = logging.StreamHandler()
sh1.setLevel(20)

# 4、设置日志的打印格式
#     日志格式在父类生效--方法
#     日志格式在子类-文件handler生效--方法
#     日志格式在子类-控制台handler生效
# format1 = "%(时间)s || %(时间)s || %(时间)s || %(时间)s || %(时间)s"
# format1 = "%(asctime)s || %(filename)s || %(lineno)s || %(levelname)s || %(message)s"
format1 = "%(asctime)s || %(filename)s || [line:%(lineno)s] || %(levelname)s || %(message)s"
formater1 = logging.Formatter(format1)
fh1.setFormatter(formater1)
sh1.setFormatter(formater1)

# 5、将子类-文件handler对象添加到父类对象
#    将子类-控制台handler对象添加到父类对象
logger1.addHandler(fh1)
logger1.addHandler(sh1)

# 6、自定义错误信息--对应日志格式的message
logging.error("打印自定义错误ERROR信息")
# logging.warning("打印自定义WARNING信息")
# logging.info("打印自定义INFO信息")
# logging.debug("打印自定义DEBUG信息")
# logging.critical("打印自定义CRITICAL信息")






























