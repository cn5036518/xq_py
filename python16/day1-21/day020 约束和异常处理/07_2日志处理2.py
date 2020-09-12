#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/16 8:49

import traceback
import logging

#定义日志格式
logging.basicConfig(
    filename='app2.log',    #日志文件名,会在当前目录生成这个文件
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

#关于日志级别
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0

#报错就写日志  #重点
for i in range(3):
    try:
        if i % 3 == 0:
            raise FileNotFoundError('文件没有找到哈')#主动抛出异常
        elif i % 3 == 1:
            raise FileExistsError()
        elif i % 3 == 2:
            raise StopIteration()
    except FileNotFoundError as e:
        val = traceback.format_exc()   #记录报错的堆栈信息，错误在哪一行
        logging.error(val)
    except FileExistsError as e:
        val = traceback.format_exc()
        logging.error(val)
    except StopIteration as e:
        val = traceback.format_exc()
        logging.error(val)
    except Exception as e:
        val = traceback.format_exc()
        logging.error(val)





















