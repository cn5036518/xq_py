#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/25 19:45

from collections import defaultdict

dd1 = defaultdict(list)
print(dd1['哈哈'])  #[]   #当key不存在的适合，返回空列表-list类型

dd2 = defaultdict(tuple)
print(dd2['哈哈'])  #()

dd3 = defaultdict(None)
print(dd3['哈哈'])
















