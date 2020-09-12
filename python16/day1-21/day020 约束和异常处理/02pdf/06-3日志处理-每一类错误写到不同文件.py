#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/20 11:04

''''''
'''
需求：每一类的堆栈保存信息写入到不同的文件（不是错误日志）





'''

import traceback

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
        # val = traceback.format_exc()
        # print(val)  #输出到控制台
        traceback.print_exc(file=open('b1.txt','a+'))
    except NameError as e:
        traceback.print_exc(file=open('b2.txt', 'a+'))
    except KeyError as e:
        traceback.print_exc(file=open('b3.txt', 'a+'))
    except Exception as e:
        traceback.print_exc(file=open('b4.txt', 'a+'))
















