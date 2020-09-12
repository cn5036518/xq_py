#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/8/1 8:19

''''''
'''
需求：
计算当前时间到2030-10-01 00:00:00的时间差

思路：
1、计算当前时间的时间戳
2、计算另外一个指定时间的时间戳
    1、格式化时间转成结构化时间
    2、结构化时间转成时间戳
3、上述2个时间戳做减法
4、将第3步的差值转换成结构化时间

需求2：
计算指定时间2010-09-01 10:28:34到2030-10-01 00:00:00的时间差

'''

import time

# 1、计算当前时间的时间戳
stamptime_now = time.time()
print(stamptime_now)  #1596241662.9743204

# 2、计算另外一个指定时间的时间戳
# 1、格式化时间转成结构化时间
format_time2 = '2030-10-01 00:00:00'
struct_time2 = time.strptime(format_time2,'%Y-%m-%d %H:%M:%S')
print(struct_time2)
#time.struct_time(tm_year=2030, tm_mon=10, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=274, tm_isdst=-1)

# 2、结构化时间转成时间戳
stamptime_fix = time.mktime(struct_time2)
print(stamptime_fix)  #1917014400.0

# 3、上述2个时间戳做减法
time_interval = stamptime_fix - stamptime_now
print(time_interval)  #320772054.495167

# 4、将第3步的差值转换成结构化时间   localtime
struct_interval = time.localtime(time_interval)
print(struct_interval)
#time.struct_time(tm_year=1980, tm_mon=3, tm_mday=1, tm_hour=23, tm_min=17, tm_sec=30, tm_wday=5, tm_yday=61, tm_isdst=0)

# 5、将第4步减去1970-01-01
print('上述2个时间的差值是 %s年 %s月 %s日 %s小时 %s分钟 %s秒 ' %
      (struct_interval.tm_year-1970,struct_interval.tm_mon-1,struct_interval.tm_mday-1
       ,struct_interval.tm_hour,struct_interval.tm_min,struct_interval.tm_sec))
# 注意点：月份和天都需要减去1
















