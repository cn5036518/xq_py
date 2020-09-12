#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 12:07

import logging
import traceback
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
# logger1.error('我是 %s' % '系统a1')  #格式化
    logger1.error('我是 %s' % system)  # 格式化

    for i in range(3):
        try:
            if i % 3 == 0:
                raise FileNotFoundError('文件不存在')
            elif i % 3 == 1:
                raise NameError('名字错误')
            elif i % 3 == 2:
                raise KeyError('key错误')
        except FileNotFoundError as e:
            print(e)
            val = traceback.format_exc()
            print(val)  #输出到控制台
            # logger1.error('我是 %s' % system)  #格式化
            # logger1.error(val)  #把报错日志-包含堆栈信息写入日志文件 #这里的堆栈信息写入到日志的message处
        except NameError as e:
            print(e)
            val = traceback.format_exc()
            print(val)
            # logger1.error(val)
        except KeyError as e:
            print(e)
            val = traceback.format_exc()
            print(val)
            # logger1.error(val)
        except Exception as e:
            print(e)
            val = traceback.format_exc()
            # print(val)
        logger1.error(val)


multi_system_log('e1.log','系统1')
multi_system_log('e2.log','系统2')
print('----------------------------------------1   函数 应用')


'''
小结：
1、pycharm 选中左上角的py文件，按ctrl+c后，可以复制出py文件名
   navicat 选中左侧的数据表文件，按ctrl+c后，可以复制出数据表文件名


'''















