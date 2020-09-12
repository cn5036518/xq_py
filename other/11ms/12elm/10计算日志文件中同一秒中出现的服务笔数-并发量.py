#!/usr/bin/env python
#-*- coding:utf-8 -*-

#需求：日志文件中，不同的服务，每调用一次，就记录一条  （日志的聚合计数）
# 请计算一天中，是哪一秒，调用的服务最多（即那1秒钟是一天中，服务调用量最大的）
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
4、得到字典后，如何计算字典中，哪一个时刻的，哪个服务的调用量最大--ok   冒泡排序

"""

f = open("log.txt")
dic1 = {}
for i in f:
    # print(i,end="")   #end默认是换行，文件本身有换行，所以有多余空行，end=""可以去掉换行
    a,b,c,d=i.split()
    print(c,d)

    if c not in dic1: #1 如果时间不在字典1中
        dic2 = {} #2 新建字典2
        dic2[d] = 1 # 3 将服务编码和1 分别作为key和value 添加到字典2
        dic1[c] = dic2 # 4 将时间和字典2 分别作为key和value 添加到字典1
    else: #2 如果时间在字典1中
        if d not in dic1[c]:  #5 如果服务编码不在字典2中  注意点：这里用dic1[c]来表示字典2
            dic2[d] = 1  # 6  将服务编码和1 分别作为key和value 添加到字典2
        else: # 7 如果服务编码在字典2中
            dic2[d] += 1 # 8 将字典2的value 自增1
print(dic1)  #{'09:57:56': {'3000': 4}, '09:57:55': {'1000': 3, '2000': 3}}
f.close()  #注意点：必须关闭文件
print("-------------1")

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

dic2 =  {'09:57:55': {'2000': 3, '1000': 3}, '09:57:56': {'3000': 4}}
#如何计算上述字典中，哪一个时刻，哪一个服务的调用量最大，打印出来--排序
# li1 = sorted(dic2.items(),key=lambda x:x[1],reverse=True)  #倒序
# print(li1)

li2 = []
for k,v in dic2.items():
    # print(k,v)
    if type(v) == dict:
        pass
        for k1,v1 in v.items():
            # print(k,k1,v1)
            li2.append((k,k1,v1))
print(li2)  #[('09:57:56', '3000', 4), ('09:57:55', '1000', 3), ('09:57:55', '2000', 3)]

# li2 = [('09:57:56', '3000', 4), ('09:57:55', '1000', 3), ('09:57:55', '2000', 3)]
#如何计算上述列表中，哪个元素的索引号是-1的数值最大？

#优化版的冒泡排序
for i in range(len(li2)):
    flag = False
    for j in range(len(li2)-1-i):
        if li2[j] > li2[j+1]:
            li2[j],li2[j + 1] = li2[j+1],li2[j]
            flag = True
    if flag == False:
        break
print(li2)  #[('09:57:55', '1000', 3), ('09:57:55', '2000', 3), ('09:57:56', '3000', 4)]
print("当天最大调用笔数发生在时间 %s，服务编码 %s，调用次数 %s" % (li2[-1][0],li2[-1][1],li2[-1][2]))
#时间 09:57:56，服务 3000，调用次数 4





