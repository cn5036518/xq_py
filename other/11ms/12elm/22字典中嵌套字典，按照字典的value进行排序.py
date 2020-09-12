#!/usr/bin/env python
#-*- coding:utf-8 -*-

dic2 =  {'09:57:55': {'2000': 3, '1000': 3}, '09:57:56': {'3000': 4}}
# #如何计算上述字典中，哪一个时刻，哪一个服务的调用量最大，打印出来--排序

li1 = []
for k,v in dic2.items():
    # print(k,v)
    if type(v) == dict:
        for k1,v1 in v.items():
            # print(k1,v1)
            li2 = [k,k1,v1]
            li1.append(li2)
print(li1)  #[['09:57:55', '1000', 3], ['09:57:55', '2000', 3], ['09:57:56', '3000', 4]]
# 通过sorted方法排序：
s = sorted(li1, key=lambda x: x[-1], reverse=True)
print(s)  #[['09:57:56', '3000', 4], ['09:57:55', '2000', 3], ['09:57:55', '1000', 3]]














