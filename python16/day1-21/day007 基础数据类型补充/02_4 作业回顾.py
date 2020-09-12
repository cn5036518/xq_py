#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 5. 干掉主播. 现有如下主播收益信息, 按照要求, 完成相应操作:
zhubo = {"卢本伟":122000,"冯提莫":18999999,"金老板":99999,"吴老板":25000000,"alex":126}
# 1、计算主播平均收益值
sum = 0
for i in zhubo:
    sum = sum + zhubo[i]  #累加计算和
print(sum)  #44222124
averge = sum/len(zhubo)
print(averge)  #8844424.8

#2、干掉收益小于平均值的主播--删除
# dic2 = {}
# for i in zhubo:
#     if zhubo[i] < averge:
#         zhubo.pop(i)  #报错  RuntimeError: dictionary changed size during iteration
# print(dic2)   #字典在循环遍历的过程中，是不能删除元素的，也不能增加元素，可以修改元素

#方法1  将小于平均值的键值对，添加到另外一个字典2
    #循环遍历字典2，过程中删除字典1中小于平均值的-传入参数是i
dic2 = {}
for i in zhubo:
    if zhubo[i] < averge:
        dic2[i] = zhubo[i]
print(dic2)  #{'金老板': 99999, 'alex': 126, '卢本伟': 122000}

for i in dic2:
    zhubo.pop(i) #遍历循环过程中，依次删除i   #关键点  这个思路必须要掌握
print(zhubo)  #{'冯提莫': 18999999, '吴老板': 25000000}
print("--------------1")

zhubo = {"卢本伟":122000,"冯提莫":18999999,"金老板":99999,"吴老板":25000000,"alex":126}
#方法2 将大于等于平均值的键值对，添加到另外一个字典2
dic2 = {}
for i in zhubo:
    if zhubo[i] >= averge:  #1 如果原字典中收益大于等于平均值
        dic2[i] = zhubo[i] #2将原字典中的姓名作为k1，收益作为v1，添加到字典2中
print(dic2)  #{'吴老板': 25000000, '冯提莫': 18999999}

#3 干掉卢本伟-删除
# zhubo.remove("卢本伟")  #报错  AttributeError: 'dict' object has no attribute 'remove'
zhubo.pop("卢本伟")  #字典删除单个键值对，只能用pop，而不能是remove
print(zhubo)  #{'冯提莫': 18999999, 'alex': 126, '吴老板': 25000000, '金老板': 99999}















