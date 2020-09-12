#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/30 8:57

import time

#1 时间戳 timestamp
print(time.time())  #1596070734.837221

#2 结构化时间 struct_time  主要用于计算时间差
print(time.localtime())
#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=30,
# tm_hour=9, tm_min=0, tm_sec=16,
#  tm_wday=3, tm_yday=212, tm_isdst=0)

#3 格式化时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))  #2020-07-30 09:03:22
print('-------------------------------------------')

'''
时间戳如何转换成格式化时间？
1、时间戳--结构化时间--格式化时间

'''

#1将当前时间戳转成格式化时间
timestamp1 = time.time()
print(timestamp1)  #1596071354.6619897   #单位是秒 10位  单位是毫秒  13位

# 01时间戳--结构化时间    localtime
struct_time1 = time.localtime(timestamp1)
print(struct_time1)
print('------------------------------')
#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=30, tm_hour=9, tm_min=12, tm_sec=20, tm_wday=3, tm_yday=212, tm_isdst=0)

# 02结构化时间--格式化时间  strftime
format_time1 = time.strftime('%Y-%m-%d %H:%M:%S', struct_time1)
print(format_time1)  #2020-07-30 09:14:20
print('-------------------------------------------1  当前时间戳转成格式化时间')

#2将指定时间戳转成格式化时间
# 01时间戳--结构化时间    localtime
struct_time2 = time.localtime(1350114528)
# struct_time2 = time.localtime(1596072062)
print(struct_time2)

# 02结构化时间--格式化时间  strftime
format_time2 = time.strftime('%Y-%m-%d %H:%M:%S', struct_time2)
print(format_time2)
print('-------------------------------------------2  指定时间戳转成格式化时间')

#2 将格式化时间转成时间戳
#01 格式化时间转成结构化时间   strptime  parse
format_time3 = '2020-07-30 09:25:00'
struct_time3 = time.strptime(format_time3,'%Y-%m-%d %H:%M:%S')
print(struct_time3)

#02  结构化时间转成格式化时间
timestamp3 = time.mktime(struct_time3)
print(timestamp3)  #1596072300.0















