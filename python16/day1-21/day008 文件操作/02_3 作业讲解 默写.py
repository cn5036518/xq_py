#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 删除列表中姓周的人的信息
li1 = ["周芷若", "周伯通", "王重阳", "周葫芦娃"]

li2 = []
for i in li1:
    if i.startswith("周"):
        li2.append(i)
print(li2)  #['周芷若', '周伯通', '周葫芦娃']

for i in li2:
    li1.remove(i)
print(li1)  #['王重阳']

"""
思路：
如何实现循环过程中的删除？
1、找出列表1中符合条件的元素依次添加到列表2
2、循环遍历列表2，过程中，从列表1中删除元素
"""














