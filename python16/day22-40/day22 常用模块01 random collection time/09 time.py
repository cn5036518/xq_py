#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/14 9:23

import time

#1 时间戳
print(time.time())  #1594689851.1467674  时间戳：单位秒  打印当前时间的时间戳
#从1970年1月1日0点开始计算，到当前的时间，经过的秒数
#给计算机用的

#2 格式化时间  年月日-时分秒
print(time.strftime('%Y-%m-%d %H:%M:%S'))    #2020-07-14 09:26:47  #打印当前时间的格式化时间
#strf= str format  字符串格式化
#给人看的

#3 结构化时间
print(time.localtime())
#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=23, tm_hour=7, tm_min=12, tm_sec=15, tm_wday=3, tm_yday=205, tm_isdst=0)
#用于计算
print('======================================================================')

'''
需求1：
1、将时间戳转换成格式化时间？

思路：
1、先把时间戳转换成结构化时间
2、然后将结构化时间转换成格式化时间
'''

# 1、先把时间戳转换成结构化时间
timestamp1 = 18812345678   #时间戳11位，单位是秒；14位，单位是毫秒
struct_time1 = time.localtime(timestamp1)   #参数是时间戳
print(struct_time1)
#time.struct_time(tm_year=2566, tm_mon=2, tm_mday=20, tm_hour=19, tm_min=34, tm_sec=38, tm_wday=3, tm_yday=51, tm_isdst=0)

# 2、然后将结构化时间转换成格式化时间
format_time1 = time.strftime('%Y-%m-%d %H:%M:%S',struct_time1)  #参数1是格式 参数2是结构化时间
print(format_time1)  #2566-02-20 19:34:38
print('------------------------------------将时间戳转成格式化时间')

'''
需求2：
1、将格式化时间转换成时间戳
   数据库保存的都是时间戳

思路：
1、将格式化时间转成结构化时间
2、将结构化时间转成时间戳

'''

# 1、将格式化时间转成结构化时间
format_time1 = '2020-07-23 07:36:55'
struct_time1 = time.strptime(format_time1,'%Y-%m-%d %H:%M:%S')  #参数1是格式化时间，参数2是格式
#strp = str parse  解析
print(struct_time1)

# 2、将结构化时间转成时间戳
time_stamp1 = time.mktime(struct_time1)  #参数是结构化时间
print(time_stamp1) #1595461015.0
print('------------------------------------将格式化时间转成时间戳')

'''
小结
1、时间戳转成格式化时间
    1、通过结构化时间中转
    2、先把时间戳转成结构化时间        time.localtime()
    3、再将结构化时间转成格式化时间    time.strftime()


2、格式化时间转成时间戳
    1、通过结构化时间中转
    2、先将格式化时间转成结构化时间  time.strptime()
    3、然后将结构化时间转成时间戳    time.mktime()


'''

















