#!/usr/bin/env python
#-*- coding:utf-8 -*-


s1 = "12,45,g,fg"
#如何输出s2 = "fg,g,45,12"
li1 = s1.split(",") #1逗号作为分隔符，将字符串拆分成小字符串，小字符串作为列表的元素依次添加到列表
print(li1)  #['12', '45', 'g', 'fg']

li1.reverse() #2对列表本身进行反转
print(li1)  #['fg', 'g', '45', '12']

s2 = ",".join(li1)  #3以逗号作为连接符，把列表中的元素连接成一个大的字符串
print(s2)  #fg,g,45,12






