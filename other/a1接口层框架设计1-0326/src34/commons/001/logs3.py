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
1、创建一个父类logger
2、创建一个文件handler，将日志写入文件
3、创建一个控制台handler，将日志写入控制台
4、设置日志的输出格式
5、将文件和控制台两个handler分别添加到父类logger--理解为会报给大领导
6、定义日志的message
"""

import logging
import os   #路径相关

#日志的级别等级  CRITICAL(FATAL)>ERROR>WARNING(WARN)>INFO>DEBUG   必须大写
#                           50>40>  30             >20 >10

# 1、新建父类对象，传入构造方法参数
logger1 = logging.getLogger("my_logger1")  #新建父类对象logger1，参数可以自定义
# logger1 = logging.getLogger()  #新建父类对象logger1，参数可以为空
#这里logging是包名，getLogger是类名，logger1是对象名，"my_logger1"是类的构造方法的参数
#和新建对象，i1 = Interface1()传入参数，是一样的
#  1-2对象调方法，方法中传入参数
logger1.setLevel(logging.INFO)  #设置父类日志级别INFO   注意INFO后面没有小括号-属性
# logger1.setLevel(20)  #设置日志级别   20和logging.INFO等效

# 2、新建文件handler对象--将日志写入文件
path1 = r"D:\PycharmProjects\xiaoqiang\base_181027\a1接口层框架设计1-0326\src34\logs\logs1.txt"
#定义日志输出文件的绝对路径
path2 = os.path.join(os.getcwd(),"logs2.txt")  #拼接当前工作路径+自定义存在日志的日志文件名字，形成全路径
#在当前目录，定义日志输出文件
# 2-2 新建对象，传入构造方法参数
fh1 = logging.FileHandler(path1)  #这里的参数要求是绝对路径，不能是相对路径;
#新建文件handler的对象fh1，参数可以自定义
# (这里FileHandler是类名，logging是包名，fh1是对象名，path1是类的构造方法的参数)
#和新建对象，i1 = Interface1()传入参数，是一样的
#2 -3  对象调方法，传入普通方法的参数
fh1.setLevel(logging.INFO)   #设置对象--文件handler的日志级别
# fh1.setLevel(20)

# 3、新建控制台handler对象--将日志写入控制台
#3-1 新建对象（控制台handler-StreamHandler ）
sh1 = logging.StreamHandler()
#sh1是对象名，logging是包名，StreamHandler类名，构造方法参数不是必须的
sh1.setLevel(logging.INFO)  ##设置对象--控制台handler的日志级别
# sh1.setLevel(20)

# 4、设置日志的输出格式
# log_format1 = "时间，文件名，行号，日志级别，自定义错误信息"
# log_format1 = "时间，文件名，行号，日志级别，自定义错误信息"
# log_format1 = "%(时间)s || %(文件名)s || %(行号)s || %(日志级别)s || %(自定义错误信息)s"
log_format1 = "%(asctime)s || %(filename)s || [line:%(lineno)s] || %(levelname)s || %(message)s"
# asctime --时间   filename-文件名  lineno-行号  levelname-日志级别  messaage-自定义错误信息
# 上述字段和格式是固定写法，记下来  只是定义类日志输出格式，还没有生效
formatter1 = logging.Formatter(log_format1)  #新建对象，日志输出格式生效
#这里logging是包名，Formatter是类名，formatter1是对象名，log_format1是类的构造方法的参数

#文件handler对象，调方法，传入参数是-日志格式对象
fh1.setFormatter(formatter1)

#控制台handler对象，调方法，传入参数-日志格式对象
sh1.setFormatter(formatter1)

# 5、将文件和控制台两个handler分别添加到父类logger--理解为会报给大领导
logger1.addHandler(fh1)
logger1.addHandler(sh1)
#通过父类的对象，调方法，传入子类对象（文件handler和控制台handler）

# 6、定义日志的message
logger1.error("打印具体的日志错误信息") #和日志输出格式中  %(message)s 对应，日志输出格式的这个字段显示这个信息























