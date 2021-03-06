#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：日志文件中，不同的服务，每调用依次，就记录一条
# 请计算一天中，是哪一秒，调用的服务最多（即那1秒钟是一天中，服务调用两最大的）
"""
思路：
1、读取文件
2、遍历循环文件的每一行，每一行都是一个字符串
3、对字符串做拆分，空格作为拆分符号，将时间这个子字符串，依次添加到列表
   注意：这里用拆分更通用，不能用索引号切片取值，除非服务编码都是位数相同，比如：5位
4、计算列表中，那个时间，出现的次数最多
   注意：不论述字符串的每个字符，出现的次数，可以用count；计算列表中每个元素出现的次数，也可以用count
   用算法实现

注意点：
步骤：
1、先计算一天中，哪一秒，调用的服务量最大
2、在计算一天中，哪一秒，那个服务的调用量最大
"""

f = open("log.txt")
li1 = []
for i in f:
    print(i,end="")   #end默认是换行，文件本身有换行，所以有多余空行，end=""可以去掉换行
    a,b,c,d=i.split()
    li1.append(c)
print() #换行
print(li1)  #['09:57:55', '09:57:55', '09:57:55',
# '09:57:55', '09:57:55', '09:57:55', '09:57:56', '09:57:56', '09:57:56', '09:57:56']

# dic1 = {}
# for i in li1:
#     dic1[i]= li1.count(i)  #count函数是统计列表中每个元素出现的次数  #内置函数
# print(dic1)  #{'09:57:55': 6, '09:57:56': 4}

#如何计算count函数的算法？
dic1 = {}
for i in li1: #1 循环遍历列表
    if i not in dic1: #2如果i不在字典中，给与初始值1
        dic1[i] = 1
    else: #3如果i在字典中，就给value自增1（value有2种表示方法，方法1是1-写死的  方法2是dic1[i]用key来表示-活的）
        dic1[i] = dic1[i] + 1
print(dic1)  #{'09:57:55': 6, '09:57:56': 4}
#意思是一天中，09:57:55这个时刻，有6笔服务调用量；09:57:56这个时刻，有4笔服务调用量
# 可见 09:57:55这个时刻的并发量最大









