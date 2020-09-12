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

# 定义类，加上异常处理
class Requests_Post1():
    def __init__(self,url,params1,headers1):
        self.url = url
        self.params1 = params1
        self.headers1 = headers1

    def requests_post2(self):
        try:
            r = requests.post(self.url,data=self.params1,headers=self.headers1)  #1调post请求   第二个参数是data
            # r = requests.post(url,data=self.params1,headers=self.headers1)  #1调post请求   第二个参数是data
            # 注意：参数1必须是self.url，而不是url（url会报错）

            dic1 = r.json()  #返回的是json类型，将json类型转换成python的字典类型
            # print("post请求获取响应结果（python-字典类型）=",dic1)
            return dic1
        except TypeError as e:
            print(str(e))

#   # 2定义参数
# url = "http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace",
#            "date": "2016-5-14"}  # 拼写错误，date而不是data  这个key是固定的，申请好的
# headers1 = {}


#
# #3新建对象
# requests1 = Requests_Post1(url,params1,headers1)  #传入实际参数
#
# # r = requests.post(url, data1=params1, headers=headers1)  # 1调post请求   第二个参数是data
# # dic1 = r.json()
#
# #4通过对象调方法
# result1 =requests1.requests_post2()
#
# print("post请求获取响应结果（python-字典类型）=",result1)  #5输出整个返回内容（字典类型）
# print("错误码error_code是：",result1["error_code"])  #6输出错误码error_code





















