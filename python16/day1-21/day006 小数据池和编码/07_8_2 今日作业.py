#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 5. 干掉主播. 现有如下主播收益信息, 按照要求, 完成相应操作:
zhubo = {"卢本伟":122000,"冯提莫":18999999,"金老板":99999,"吴老板":25000000,"alex":126}
# 1、计算主播平均收益值
sum = 0
for i in zhubo.values():
    sum += i  #累加字典的value值
print(sum)  #25412124
average = sum/len(zhubo)
print(average)  #5082424.8

#2、干掉收益小于平均值的主播
# for k,v in zhubo.items():
#     if v< average:
#         zhubo.pop(k)  #RuntimeError: dictionary changed size during iteration
#         #字典在循环遍历的时候，是不能够删除元素（键值对的）
#          列表在循环遍历的时候，删除元素的时候，不会报错，会删除索引号是偶数的元素
# print(zhubo)

#方法1   思路：把大于平均值收益的键值对，添加到新的字典    推荐：简洁
dic2 = {}
for k,v in zhubo.items():
    if v >=average:
        dic2[k] = v   #将收益值大于平均数的键值对，添加到新的字典中
print(dic2)  #{'吴老板': 25000000, '冯提莫': 18999999}

#方法2  思路：把小于平均值收益的k1，找出来，存到一个空列表；然后从原字典中删除整个空列表中的
li1 = []
for k,v in zhubo.items():
    if v < average:
        li1.append(k)
print(li1)  #['金老板', '卢本伟', 'alex']

# del zhubo[li1]   #报错  TypeError: unhashable type: 'list'
# zhubo.pop(li1)   #报错  TypeError: unhashable type: 'list'
for i in li1:   #遍历循环列表
    zhubo.pop(i)  #依次从字典中删除单个的key,和下面的写法等效   #关键点：整个思想要掌握（从字典中删除多个key）
    # del zhubo[i]
print(zhubo)  #{'冯提莫': 18999999, '吴老板': 25000000}
print("-----------2")


#3、干掉卢本伟
zhubo = {"卢本伟":122000,"冯提莫":189999,"金老板":99999,"吴老板":25000000,"alex":126}
del zhubo["卢本伟"]
print(zhubo)  #{'冯提莫': 189999, '金老板': 99999, '吴老板': 25000000, 'alex': 126}
















