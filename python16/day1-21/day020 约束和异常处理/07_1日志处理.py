#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/16 8:04

import logging

#定义日志格式
logging.basicConfig(
    filename='app.log',    #日志文件名,会在当前目录生成这个文件
    datefmt='%Y-%m-%d %H:%M:%S',  #时间
    level=0,                #日志级别  大于等于这个值，才会输出  #如果是40，就知会输出critical和error
    #   这个level不写，默认是30
    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s'  #日志格式
    #2020-06-16 08:14:13-root-ERROR-07日志处理-我是error
    #asctime 时间  #这里的格式是datefmt定义的
    #name   root
    #levelname  ERROR   日志级别
    #module    模块-文件名
    #message   提示信息
)

#写日志
logging.critical('我是critical')
logging.error('我是error')
logging.warning('我是warning')
logging.info('我是info')
# logging.INFO('我是info')  #大写报错  TypeError: 'int' object is not callable
logging.debug('我是debug')

logging.log(2,'我是自定义')   #参数1是日志级别的数值，参数2是提示语

#关于日志级别
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0









































