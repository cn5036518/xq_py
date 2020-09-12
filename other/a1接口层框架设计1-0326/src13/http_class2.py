#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@author: jack
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: cn5036520@163.com
@software: sign
@file: 0319-4课上作业.py
@time: 2019/1/13 6:43
@desc:
'''

"""
在一个py文件中，将上述get和post请求分别封装成类，并且加上异常处理
"""

import requests
import json

#1 定义请求类，加上异常处理
class Requests_Post1():
    def __init__(self,url,params1,headers1):
        self.url = url
        self.params1 = params1
        self.headers1 = headers1

    def requests_post2(self):
        try:
            r = requests.post(self.url,data=self.params1,headers=self.headers1)  #1调post请求   第二个参数是data
            dic1 = r.json()  #返回的是json类型，将json类型转换成python的字典类型
            # print("post请求获取响应结果（python-字典类型）=",dic1)
            return dic1
        except TypeError as e:
            print(str(e))

class Requests_Get1():
    def __init__(self, url, params1, headers1):
        self.url = url
        self.params1 = params1
        self.headers1 = headers1

    def requests_get2(self):
        try:
            r = requests.get(self.url, data=self.params1, headers=self.headers1)  # 1调post请求   第二个参数是data
            dic1 = r.json()  # 返回的是json类型，将json类型转换成python的字典类型
            # print("post请求获取响应结果（python-字典类型）=",dic1)
            return dic1
        except TypeError as e:
            print(str(e))























