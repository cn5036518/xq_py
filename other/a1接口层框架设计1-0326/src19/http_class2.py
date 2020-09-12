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
一、整体思路
二、整体结构
    一、http请求类结构
        1、构造方法
        2、post方法
        3、get方法
三、伪代码
    1、导包
        json
        requests
    2、全局变量  url params1 headers1
    3、类名
        构造方法,成员变量，方便方法间使用
        方法1：post方法
                将返回r转换成字典 r.json()
                return 字典
        方法2：get方法
                将返回r转换成字典 r.json()
                return 字典
        加上异常处理
四、注意点
    1、异常处理
    2、返回的是响应数据r是特殊类型（不是json字符串），转换成python字典，return
五、步骤
    1、单个类先测试通过
    2、然后再封装好，用来给其他文件调用
"""

import json
import requests

# url = "http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# headers1 ={}

class Http_request1:
    def __init__(self,url,params1,headers1):
        self.url = url
        self.params1 = params1
        self.headers1 =headers1
    def post_request1(self):
        try:
            r = requests.post(self.url,params=self.params1,headers = self.headers1)
            dic1 = r.json()
            # print(dic1)
            return dic1
        except TypeError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    def get_request2(self):
        r = requests.get(self.url,params=self.params1,headers = self.headers1)
        dic1 = r.json()
        # print(dic1)
        return dic1

# #新建对象，自动调构造方法，传入参数
# h1 = Http_request1(url,params1,headers1)
# ret1 = h1.post_request1()
# print(ret1)
#
# h2 = Http_request1(url,params1,headers1)
# ret2 = h2.get_request2()
# print(ret2)






















