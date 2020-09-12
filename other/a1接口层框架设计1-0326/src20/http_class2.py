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
一、思路
二、结构
    1、导包1
        json
        requests
    2、全局变量1 url params1 headers1
    3、类
        1、构造方法（传入参数）
        2、post方法
        3、get方法
    4、新建对象
    5、对象调方法

三、伪代码
四、注意点
    1、发送请求到服务器后，返回的类型是特殊的类型r（不是json字符串）
        r.text是json字符串（已经验证）
        将r通过r.json()转换成python的字典 return
    2、post和get方法的参数（url，params=，headers=）

五、步骤
    1、先单个文件类测试通过
    2、再封装起来
"""

#一、导包
import requests
import json

# #一、全局变量
# url = "http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# headers1 = {}

#二、类
class Http_request:
    def __init__(self,url,params1,headers1):
        self.url = url  # 成员变量，方法间使用
        self.params1 = params1
        self.headers1 = headers1

    def post_request1(self):
        r = requests.post(self.url,params=self.params1,headers=self.headers1)
        # print(r)  #<Response [200]>
        # print(type(r))  #<class 'requests.models.Response'>
        dic1 = r.json()
        # print(dic1)
        return dic1

    def get_request2(self):
        r = requests.get(self.url, params=self.params1, headers=self.headers1)
        r = r.text
        # print(type(r))  #<class 'str'>   json字符串
        dic1 = json.loads(r)
        # dic1 = r.json()
        print(dic1)
        # print(type(dic1))
        return dic1

# #三新建对象，传入参数，自动调构造方法
# h1 = Http_request(url,params1,headers1)
#
# #四对象调方法
# h1.post_request1()
# h1.get_request2()



















