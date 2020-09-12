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

"""
学习方法：
1、方法或者代码即便是相同的，不要复制，用手敲来代替，锻炼熟悉度

一、http请求类伪代码
1、导包
    requests
    json
2、新建类
    两个方法分别是post和get，构造方法传入url params headers
3、注意将返回的r转换成字典return
    dic1 = r.json()
4、先单个类，测试通过

"""

# url="http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# headers1 = {}

import requests
import json

class Http_request:
    def __init__(self,url:"地址",params1,headers1)->"返回列表": #注释
        # 参数注释 url:"地址"   这里的地址就是前面url的注释，需要双引号
        # 方法返回注释 ->"返回列表"  这里的“返回列表”表示的方法返回
        """
        写这个方法主要是干什么的
        """
        self.url = url
        self.params1 = params1
        self.headers1 = headers1
    def post_request1(self):
        r = requests.post(self.url,params = self.params1,headers = self.headers1)
        dic1 = r.json()
        # print(dic1)
        return dic1
    def get_request1(self):
        r = requests.get(self.url,params= self.params1,headers = self.headers1)
        dic1 = r.json()
        # print(dic1)
        return dic1

# #新建对象，自动调用
# h1 = Http_request(url,params1,headers1)
#
# #对象调方法
# result1 = h1.post_request1()
# print(result1)
#
# result2 = h1.get_request1()
# print(result2)
























