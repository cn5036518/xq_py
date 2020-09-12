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
一、调用关系
    1、http请求类单独一个文件
    2、接口类和读取execel在同一个文件
    3、接口类会调用http请求类（前提：把请求类导入）
    4、读取excel中，会调用接口类
二、http请求类伪代码
    1、类分为两个方法post和get-1
    2、导入json和requests包--1
    3、调用post请求，返回json字符串-1
    4、将json字符串转换成python 字典   r.json()  -1
    5、捕捉异常-先用Exception--1
        再用TypeError

    步骤：1先将url param写死--1
            通过构造方法掺入，转换成成员变量，方便方法间使用-1
          2然后才是写活--从excel中读取
"""

import requests
import json

# url="http://v.juhe.cn/laohuangli/d"    #老黄历聚合网站  #这个从excel中读取  先写死
# param1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}   #key和value #这个从excel中读取
# headers1 = {}

class Http_request1:
    def __init__(self,url,param1,headers1):
        self.url = url
        self.param1 = param1
        self.headers1 = headers1

    def post_method1(self):
        try:
            r = requests.post(self.url, data=self.param1, headers=self.headers1) #1核心代码
            dic1 = r.json()  #2将返回的json字符串，转换成python的字典
            return dic1
        # except Exception as e:
        except TypeError as e:
            print(str(e))

    def get_method2(self):
        try:
            r = requests.get(self.url, data=self.param1, headers=self.headers1)
            dic1 = r.json()
            return dic1
        except TypeError as e:
            print(str(e))

# #新建对象
# request1 = Http_request1(url,param1,headers1)  #自动调构造方法
#
# #对象调方法
# dic1 = request1.post_method1()
# print(dic1)
# print(type(dic1))
#
# dic2 = request1.get_method2()
# print(dic2)  #当前的老黄历接口不支持get方法，只支持post方法
# print(type(dic2))




















