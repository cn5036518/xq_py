#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/8/1 8:52

''''''
'''
需求：
计算指定时间2010-09-01 10:28:34到2030-10-01 00:00:00的时间差

思路：
1、计算指定时间的时间戳
2、计算另外一个指定时间的时间戳
    1、格式化时间转成结构化时间
    2、结构化时间转成时间戳
3、上述2个时间戳做减法
4、将第3步的差值转换成结构化时间
5、将结构化时间减去1970-01-01

'''
import time

# 1、计算指定时间的时间戳
     #1将格式化时间转成结构化时间
format_time1 = '2010-09-01 10:28:34'

def format_convert_timestamp(format_time1):
    struct_time1 = time.strptime(format_time1,'%Y-%m-%d %H:%M:%S')
    # print(struct_time1)
    #time.struct_time(tm_year=2010, tm_mon=9, tm_mday=1, tm_hour=10, tm_min=28, tm_sec=34, tm_wday=2, tm_yday=244, tm_isdst=-1)

         #2将结构化时间转成时间戳
    timestamp1 = time.mktime(struct_time1)
    print(timestamp1)  #1283308114.0
    return timestamp1


timestamp1 = format_convert_timestamp(format_time1)

# 2、计算另外一个指定时间的时间戳
#     1、格式化时间转成结构化时间
#     2、结构化时间转成时间戳
format_time2 = '2030-10-01 00:00:00'
timestamp2 = format_convert_timestamp(format_time2)

# 3、上述2个时间戳做减法
time_interval = timestamp2 - timestamp1
print(time_interval)  #633706286.0

# 4、将第3步的差值(时间戳)转换成结构化时间  localtime
struct_time = time.localtime(time_interval)
print(struct_time)
#time.struct_time(tm_year=1990, tm_mon=1, tm_mday=30, tm_hour=21, tm_min=31, tm_sec=26, tm_wday=1, tm_yday=30, tm_isdst=0)

# 5、将结构化时间减去1970-01-01
print('上述2个指定时间的时间差是 %s年 %s月 %s日 %s小时 %s分钟 %s秒' %
      (struct_time.tm_year-1970,struct_time.tm_mon-1, struct_time.tm_mday-1,struct_time.tm_hour,struct_time.tm_min,struct_time.tm_sec))
#上述2个指定时间的时间差是 20年 0月 29日 21小时 31分钟 26秒


'''
小结
一、时间转换
    1、时间戳转换成格式化时间
        1、先转换成结构化时间
            time.localtime(timestamp)
        2、再转换成格式化时间
            time.strftime('%Y-%m-%d %H:%M:%S',struct_time)

    2、格式化时间转换成时间戳
        1、先转换成结构化时间
            time.strptime(format_time,'%Y-%m-%d %H:%M:%S')
        2、再转换成时间戳
            time.mktime(struct_time)
二、计算时间差
    1、计算指定时间a的时间戳
       01格式化时间转成结构化时间
       02结构化时间转成时间戳
       封装成函数
    2、计算指定时间b的时间戳
    3、计算上述两个时间戳的差值
    4、将差值转成结构化时间
    5、结构化时间减去1970-1-1
'''


















