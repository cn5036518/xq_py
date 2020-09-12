#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/7 8:21
#@author:wangtongpei

''''''
'''
#集合的特点：无序，去重复，可哈希
#集合的本质：只有key，没有value的字典

列表推导式格式 [结果      for循环 if筛选]
字典推导式格式 {key:value for循环 if筛选}
集合推导式格式 {key       for循环 if筛选}

集合推导式编写步骤
1、创建空集合 {}
2、for循环
3、结果-key  (字典推导式结果是key:value)
4、变量保存集合推导式
'''


li1 = ['jack','tom','bob','jack']
set1 = set(li1)#把列表转换成集合
print(set1)  #{'tom', 'bob', 'jack'}

#集合推导式
#将列表转换成集合，用集合推导式
li1 = ['jack','tom','bob','jack']
set2 = {i for i in li1}
print(set2)  #{'bob', 'tom', 'jack'}













