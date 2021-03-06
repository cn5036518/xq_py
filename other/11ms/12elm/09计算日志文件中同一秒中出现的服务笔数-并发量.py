#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：日志文件中，不同的服务，每调用依次，就记录一条
# 请计算一天中，是哪一秒，调用的服务最多（即那1秒钟是一天中，服务调用两最大的）
"""
思路：
1、读取文件
2、循环遍历文件对象
3、通过拆分每一行的字符串，得到日志级别a、日期b、时间c、服务编码d
4、循环外新建字典1
5、如果时间c不在字典1中
    01 新建字典2
    02 将服务编码和1 分别作为key和value 添加到字典2
    03 将时间c和字典2 分别作为key和value 添加到字典1
6、如果时间c在字典1中
    01 如果服务编码不在字典2中 （字典2用dic1[c]来表示）
       将服务编码和1 分别作为key和value 添加到字典2
    02 如果服务编码在字典2中
        将字典2的value自增1  （字典2的value用字典2的key来表示）


注意点：
步骤：
1、先计算一天中，哪一秒，调用的服务量最大--ok
2、在计算一天中，哪一秒，那个服务的调用量最大--ok
3、把第三列和第四列，作为元组，元组作为元素添加到列表中，当有几亿亿行数据的时候，
   列表占用内存太大，需要优化  --ok

"""

f = open("log.txt")
dic1 = {}
for i in f:
    # print(i,end="")   #end默认是换行，文件本身有换行，所以有多余空行，end=""可以去掉换行
    a,b,c,d=i.split()
    print(c,d)

    if c not in dic1:
        dic2 = {}
        dic2[d] = 1
        dic1[c] = dic2
    else:
        if d not in dic1[c]:
            dic2[d] = 1
        else:
            dic2[d] += 1
print(dic1)  #{'09:57:56': {'3000': 4}, '09:57:55': {'1000': 3, '2000': 3}}

"""
过程分析：
('09:57:55', '1000')  {'09:57:55':{"1000":1}}  1
 ('09:57:55', '1000') {'09:57:55':{"1000":2}}  2
  ('09:57:55', '1000') {'09:57:55':{"1000":3}} 3
   ('09:57:55', '2000') {'09:57:55':{"1000":3,"2000":1}} 4
   ('09:57:55', '2000') {'09:57:55':{"1000":3,"2000":2}} 5
   ('09:57:55', '2000') {'09:57:55':{"1000":3,"2000":3}} 6
   ('09:57:56', '3000') {'09:57:56':{"3000":1}}
   ('09:57:56', '3000') {'09:57:56':{"3000":2}}
"""












