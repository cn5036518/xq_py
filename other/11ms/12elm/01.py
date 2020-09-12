#!/usr/bin/env python
#-*- coding:utf-8 -*-

li1= [('09:57:55', '1000'), ('19:57:55', '1000'),
      ('09:57:55', '1000'), ('09:57:55', '2000'), ('09:57:55', '2000'), ('09:57:55', '2000'), ('09:57:56', '3000'), ('09:57:56', '3000')]

dic1 = {}
for i in li1: #1 循环遍历列表
    t1 = i[0]  #时间
    service1  = i[1]  #服务编码

    if t1 not in dic1:
        dic2 = {}
        dic2[service1] = 1
        dic1[t1] = dic2
    else:
        # print(dic2)
        # if service1 not in dic2:
        if service1 not in dic1[t1]:  #这里必须用dic1[t1]，用dic2虽然不报错，但是不准确，有问题
            dic2[service1] = 1
        else:
            dic2[service1] += 1
print(dic1)


# if 0:
#     dic22 = {}
#     print(dic22)
# else:
#     if dic22 == {}:
#         print(dic22)










