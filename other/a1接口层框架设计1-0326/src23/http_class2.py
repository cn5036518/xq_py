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
    1、导包
        json
        requests
    2、全局变量 url params1 headers1
    3、类
        构造方法-传入3个参数，成员变量，方法间使用
        post方法 参数url params= headers=
        get方法 参数url params= headers=
    4、新建对象，传入3个参数，自动调用构造方法
    5、对象调post方法
        对象调get方法

三、伪代码
四、注意点
    1、请求发送到服务端后，返回的r需要转换成python字典，dic1 = r.json()
    2、异常处理1

五、步骤
    1、先单个文件测试通过1
    2、然后封装起来1

六、扩展和优化
"""

import json
import requests

# #一、全局变量
# url = "http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# headers1 = {}

#二、类定义
class Http_request1:
    def __init__(self,url,params1,headers1):
        self.url = url  #成员变量，方法间使用
        self.params1 = params1
        self.headers1 = headers1

    def post_request1(self):
        try:
            r = requests.post(self.url,params=self.params1,headers=self.headers1)
            dic1 = r.json()
            print(dic1)
            return dic1
        except TypeError as e:
            print(str(e))
        except ConnectionError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def get_request2(self):
        try:
            r = requests.get(self.url, params=self.params1, headers=self.headers1)
            dic1 = r.json()
            # dic1 = r.text
            # dic1 = json.loads(dic1)
            print(dic1)
            return dic1
        except TypeError as e:
            print(str(e))
        except ConnectionError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

# #三、新建对象
# h1 = Http_request1(url,params1,headers1)
#
# #四、对象调方法
# # h1.post_request1()
# h1.get_request2()



















