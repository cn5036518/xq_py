#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/8/20 15:42

''''''
'''
1、回顾文件递归遍历. 默写一遍.
 入口在：  当文件是个文件夹的时候
 出口在： 文件是一个文件

2、写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。

3、计算时间差(用户输入起始时间和结束时间. 计算时间差(小时), 
 		例如, 用户输入2018-10-08 12:00:00   2018-10-08 14:30:00 输出2小时30分

3、使用random.random()来计算[m,n]以内的随机整数


5、使用os模块创建如下目录结构
# glance
# ├── __init__.py
# ├── api
# │   ├── __init__.py
# │   ├── policy.py
# │   └── versions.py
# ├── cmd
# │   ├── __init__.py
# │   └── manage.py
# └── db
#      ├── __init__.py
#      └── models.py

 6. 写一个用户注册登陆的程序，每一个用户的注册都要把用户名和密码用字典的格式写入文件userinfo。在登陆的时候，再从文件中读取信息进行验证。




明日默写内容:

1. 时间戳转换成格式化时间
2. 格式化时间转换成时间戳

'''

# 2、写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个参数是目标位置，将源文件copy到目标位置。

# 3、计算时间差(用户输入起始时间和结束时间. 计算时间差(小时),
#  		例如, 用户输入2018-10-08 12:00:00   2018-10-08 14:30:00 输出2小时30分
import time

'''
计算时间差的思路：
1、把第一个格式化时间转成时间戳  
2、把第二个格式化时间转成时间戳
    1、格式化时间转成结构化时间          struct_time = time.strptime(format_time,'%Y-%m-%d %H:%M:%S')
    2、结构化时间转成时间戳              time_stamp = time.mktime(struct_time)
3、两个时间戳做减法
4、将第3步的差值(时间戳)转成结构化时间   struct_time = time.localtime(time_interval)
5、将第4步的结构化时间减去19700101       struct_time.tm_year-1970
'''

# 1、把第一个格式化时间转成时间戳
format_time1 = '2018-10-08 12:00:00'
struct_time1 = time.strptime(format_time1,'%Y-%m-%d %H:%M:%S')
print(struct_time1)
#time.struct_time(tm_year=2018, tm_mon=10, tm_mday=8, tm_hour=12,
# tm_min=0, tm_sec=0, tm_wday=0, tm_yday=281, tm_isdst=-1)

# 2、把第二个格式化时间转成时间戳
#     1、格式化时间转成结构化时间
format_time2 = '2018-10-08 14:30:00'
struct_time2 = time.strptime(format_time2,'%Y-%m-%d %H:%M:%S')
print(struct_time2)
# t1 = tuple(struct_time2)
# print(type(t1))
#time.struct_time(tm_year=2018, tm_mon=10, tm_mday=8, tm_hour=14,
# tm_min=30, tm_sec=0, tm_wday=0, tm_yday=281, tm_isdst=-1)

#     2、结构化时间转成时间戳
time_stamp1 = time.mktime(struct_time1)
print(time_stamp1)  #1538971200.0
#Convert a time tuple in local time to seconds since the Epoch.

time_stamp2 = time.mktime(struct_time2)
print(time_stamp2) #1538980200.0

# 3、两个时间戳做减法
time_difference = time_stamp2 - time_stamp1
print(time_difference) #9000.0

# 4、将第3步的差值转成结构化时间
     #即时间戳转成结构化时间
struct_time3 = time.localtime(time_difference)
print(struct_time3)
#time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=10, tm_min=30, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
#这里的9000秒应该是2.5小时才对，怎么转成结构化时间是10.5小时？---疑问

# 5、将第4步的结构化时间减去19700101
print('两个指定的格式化时间的时间间隔是 %s年 %s月 %s日 %s小时 %s分 %s秒' %
      (struct_time3.tm_year-1970,struct_time3.tm_mon-1,struct_time3.tm_mday-1,
       struct_time3.tm_hour,struct_time3.tm_min,struct_time3.tm_sec))
#两个指定的格式化时间的时间间隔是 0年 0月 0日 10小时 30分 0秒   这里应该是2小时30分的时间差

'''
小结：
计算时间差
1、格式化时间转成结构化时间  struct_time = time.strptime(format_time,'%Y-%m-%d %H:%M:%S')
2、结构化时间转成时间戳      time_stamp = time.mktime(struct_time)
3、时间戳的差转成结构化时间  struct_time = time.localtime(time_interval)
'''









