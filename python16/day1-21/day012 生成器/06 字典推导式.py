#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/7 6:48
#@author:wangtongpei

dic1 = {'张无忌':'九阳神功','乔峰':'降龙十八掌'}

for k in dic1:
    print(k)  #循环字典的key
# 张无忌
# 乔峰

#题目1：实现将字典的key和value对调
dic2 = { dic1[k]:k for k in dic1}
print(dic2)  #{'九阳神功': '张无忌', '降龙十八掌': '乔峰'}
print('---------------1 实现将字典的key和value对调')

'''
字典推导式的步骤
1、创建空字典  {}
2、for循环
3、结果写在for循环前面--key:value形式
4、将字典推导式用变量保存

字典推导式和列表推导式的格式
dic2 = {结果 for循环 if筛选}
li2 = [结果 for循环 if筛选]
'''

#题目2：实现将列表1的元素作为字典的key，列表2同位置的元素作为字典的value
li1 = ['北京','上海']
li2 = ['烤鸭','城隍庙小吃']
#题目分析，涉及到2个列表的同位置，就需要range(len(li1))通过索引来取值

dic2 = {li1[i]:li2[i] for i in range(len(li1))}
print(dic2)  #{'上海': '城隍庙小吃', '北京': '烤鸭'}
print('---------------2 实现将列表1的元素作为字典的key，列表2同位置的元素作为字典的value')









