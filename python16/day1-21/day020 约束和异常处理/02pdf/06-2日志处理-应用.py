#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 10:46

''''''
'''
需求：如果报错了，把报错信息打印出来

思路：
1、先配置日志
   0、定义日志文件  #日志是往这个文件追加的
   1、定义日志的格式
    时间-名字-日志级别-文件名字-错误信息
   2、定义日志时间的格式
   3、定义日志级别
      大于等于日志级别才会打印
      自定义日志级别
2、定义一个异常报错的场景，调用日志，把报错信息打印出来到控制台
'''

import logging
import traceback

# 1、先配置日志
#    0、定义日志文件   #日志是往这个文件追加的
#    1、定义日志的格式
#     时间-名字-日志级别-文件名字-错误信息
#    2、定义日志时间的格式
#    3、定义日志级别
#       大于等于日志级别才会打印
#       自定义日志级别

logging.basicConfig(filename='a2.log',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level = 40)   #大于等于40，才会写入

'''
日志级别需要大写
CRITICAL = 50
FATAL =50
ERROR =40
WARNING =30
WARN = 30
INFO = 20
DENGBU = 10
NOTSET = 0
'''
# logging.critical('我是critical')
# logging.error('我是error')
# logging.warning('我是warning')
# logging.info('我是info')
# logging.debug('我是debug')
# logging.log(2,'我是自定义log')


class Custom_error(Exception):
    pass

for i in range(3):
    try:
        if i % 3 == 0:
            raise FileNotFoundError('文件不存在')
        elif i % 3 == 1:
            raise NameError('名字错误')
        elif i % 3 == 2:
            raise Custom_error('自定义异常')
    except FileNotFoundError as e:
        print(e)
        val = traceback.format_exc()
        print(val)  #输出到控制台
        logging.error(val)  #把报错日志-包含堆栈信息写入日志文件 #这里的堆栈信息写入到日志的message处
    except NameError as e:
        print(e)
        val = traceback.format_exc()
        print(val)
        logging.error(val)
    except Custom_error as e:
        print(e)
        val = traceback.format_exc()
        print(val)
        logging.error(val)
    except Exception as e:
        print(e)
        val = traceback.format_exc()
        print(val)
        logging.error(val)





































