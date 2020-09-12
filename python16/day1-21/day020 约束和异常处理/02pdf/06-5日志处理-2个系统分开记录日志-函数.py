#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 12:07

import logging
def multi_system_log(filename,system):
    # 2、创建一个操作日志的文件助手对象，依赖FileHandler
    file_handler1 = logging.FileHandler(filename, mode='a', encoding='utf-8')

    # 3、设置日志格式
    formatter1 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s')

    # 4、将日志格式添加到文件助手对象
    file_handler1.setFormatter(formatter1)

    # 5、设置日志级别，返回到操作日志的对象
    logger1 = logging.Logger(system, level=40)

    # 6、操作日志的对象添加文件助手对象
    logger1.addHandler(file_handler1)

    # 7、日志对象调error写入提示信息
    logger1.error('我是 %s' % system)  #格式化

multi_system_log('e1.log','系统1')
multi_system_log('e2.log','系统2')
print('----------------------------------------1   函数1')


















