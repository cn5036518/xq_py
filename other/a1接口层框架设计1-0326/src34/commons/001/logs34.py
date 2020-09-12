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
    定义日志级别 全大写字母
1、新建父类日志对象
    设置父类的日志级别
2、新建文件handler日志对象
    设置文件handler的日志级别
3、新建控制台handler日志对象
    设置控制台handler的日志级别
4、设置日志格式
    父类日志格式生效
    子类-文件handler日志格式生效
    子类-控制台handler日志格式生效--对象掉方法，传入参数
5、文件handler对象添加到父类
    把控制台handler对象添加到父类--汇报给大领导
6、自定义错误信息--对应日志格式的message

注意点：
1、日志格式的拼写要注意
2、日志格式的优先级
    父类日志级别和子类文件handler、控制台handler日志级别不一致的话
    哪个更严格（数值更大），取哪个
"""

import logging
import os #获取当前路径使用

#日志级别 全部大写字母 CRITICAL(FATAL)>ERROR>WARN(WARNING)>INFO>DEBUG
#                               50 >40   >30           >20  >10

# 1、新建父类日志对象
#     设置父类的日志级别
logger1 = logging.getLogger()
logger1.setLevel(20)
# logger1.setLevel(logging.INFO)

# 2、新建文件handler日志对象
#     设置文件handler的日志级别
path1 = r"D:\xq_py\a1接口层框架设计1-0326\src34\logs\logs34.txt"  #指定日志文件的绝对路径
fh1 = logging.FileHandler(path1)   #日志路径必须是绝对路径
fh1.setLevel(20)

# 3、新建控制台handler日志对象
#     设置控制台handler的日志级别
sh1 = logging.StreamHandler()
sh1.setLevel(20)

# 4、设置日志格式
#     父类日志格式生效
#     子类-文件handler日志格式生效
#     子类-控制台handler日志格式生效--对象掉方法，传入参数
# format1 = "%(时间)s || %(时间)s || %(时间)s || %(时间)s || %(时间)s"
# format1 = "%(时间)s || %(文件名)s || %(行号)s || %(日志级别)s || %(日志错误信息)s"
# format1 = "%(asctime)s || %(filename)s || %(lineno)s || %(levelname)s || %(message)s"
format1 = "%(asctime)s || %(filename)s || [line:%(lineno)s] || %(levelname)s || %(message)s"
formatter1 = logging.Formatter(format1)   #这个方法要注意
fh1.setFormatter(formatter1)
sh1.setFormatter(formatter1)  #对象调方法，传入参数   #这个方法要注意

# 5、文件handler对象添加到父类
#     把控制台handler对象添加到父类--汇报给大领导
logger1.addHandler(fh1)
logger1.addHandler(sh1)

# 6、自定义错误信息--对应日志格式的message
logging.error("打印错误ERROR信息")
# logging.warning("打印错误WARNING信息")
# logging.info("打印错误INFO信息")
# logging.debug("打印错误DEBUG信息")
# logging.critical("打印错误CRITICAL信息")





























