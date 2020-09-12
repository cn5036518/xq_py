#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 5. 干掉主播. 现有如下主播收益信息, 按照要求, 完成相应操作:
zhubo = {"卢本伟":122000,"冯提莫":189999,"金老板":99999,"吴老板":25000000,"alex":126}
# 1、计算主播平均收益值
# print(zhubo.values())
li = zhubo.values()
print(li)
sum = 0
for i in li:
    sum = sum +i  #累加
print(sum)  #25412124
average = sum/len(zhubo)
print(average)  #5082424.8
print("---------------1")

#2、干掉收益小于平均值的主播
dic1 = {}
for i in zhubo:
    # print(i,zhubo[i])
    if zhubo[i] > average:
        dic1[i] = zhubo[i]  #添加键值对到新的空白字典
print(dic1)  #{'吴老板': 25000000}
print("---------------2")

#3、干掉卢本伟
zhubo = {"卢本伟":122000,"冯提莫":189999,"金老板":99999,"吴老板":25000000,"alex":126}
zhubo.pop("卢本伟")
print(zhubo)  #{'冯提莫': 189999, '金老板': 99999, '吴老板': 25000000, 'alex': 126}














