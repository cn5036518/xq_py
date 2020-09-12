#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/14 7:49

dic1 = {'name':'jack','age':18}
print(dic1)  #{'name': 'jack', 'age': 18}
'''
字典是无序的，py3.6版本及以上，在打印的时候，按照定义的顺序进行显示；
字段查询很快，hash的空间比较打，空间换时间  py3.6采用的是pypy  节约20-30%的空间

'''

from collections import OrderedDict   #继承dict类
dic1 = {'name':'jack','age':18}
od1 = OrderedDict(dic1)
print(od1)   #OrderedDict([('name', 'jack'), ('age', 18)])   #按照字典定义的顺序进行显示
print('--------------------------1  OrderedDict')

from collections import defaultdict
dic2 = defaultdict(list)  #这里的参数必须是callable
# dic2 = defaultdict()  #这里的参数必须是callable
dic2['name'] = 'tom'
print(dic2)  #defaultdict(<class 'list'>, {'name': 'tom'})
print(dic2['name'])  #tom
print(dic2['jack'])  #[]
# 当key不存在的时候，返回默认值，取参数list加上小括号 list（）就是[]
print('--------------------------2  defaultdict 1')

dic3 = defaultdict(None)
print(dic3)  #defaultdict(None, {})
print(type(dic3))  #<class 'collections.defaultdict'>
dic3['name'] = 'jack'
print(dic3)  #defaultdict(None, {'name': 'jack'})
print(dic3['name'])  #jack
# print(dic3['age'])  #KeyError: 'age'
print('--------------------------3  defaultdict 2')
















