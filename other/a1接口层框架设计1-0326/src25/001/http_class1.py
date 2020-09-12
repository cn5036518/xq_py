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
一、http请求类伪代码
0 导包
    import json
    import requests
1、新建类
    构造方法，成员变量，便于方法间使用
    参数是url,param,headers
    方法1，post请求方法
        通过requests.post(参数url,params,headers)，获取的返回是json字符串
        通过dic1 = r.json()转换成python字典（放入内存使用）
        返回return dic1
    方法2、get请求方法
        通过requests.get(参数url,params,headers)，获取的返回是json字符串
        通过dic1 = r.json()转换成python字典（放入内存使用）
        返回return dic1
2、先把url,param,headers作为全局变量写死，通过新建对象，调方法，测试http请求类本身（单元测试）-1
   测试通过后，将全局变量、新建对象和对象调方法注释
3、注意，捕捉异常 TypeError  Exception
"""

import requests
import json

# url="http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# headers1 = {}

class Http_request1:
    def __init__(self,url,param1,headers1):
        self.url = url
        self.param1 = param1
        self.headers1 = headers1

    def post_request1(self):
        try:
            r = requests.post(self.url,params=self.param1,headers = self.headers1)  #正确  推荐
            dic1 =r.json()  #推荐 简洁   3这里的r是http请求类的返回，不是json字符串类型
            return dic1
        except TypeError as e:
            print(str(e))
        except Exception as e:  #'Http_request1' object has no attribute 'ur1'
            print(str(e))

    def post_request2(self):
        try:
            r = requests.post(self.url, params=self.param1, headers=self.headers1)
            dic1 = json.loads(r.text)  #参数r.text是json字符串
            return dic1
        except TypeError as e:
            print(str(e))
        except Exception as e:  #
            print(str(e))

    def get_request1(self):
        try:
            r = requests.get(self.url,params=self.param1,headers = self.headers1)  #正确  推荐
            dic1 = r.json()
            return dic1
        except TypeError as e:
            print(str(e))
        except Exception as e:  #
            print(str(e))

# #新建对象,自动调构造方法，参数在新建对象的时候传入,后面的方法就不能传入了
# request1 = Http_request1(url,params1,headers1)
#
# #对象调方法
# result1 = request1.post_request1()  #参数在新建对象的时候传入，这里传入就会报错
# print(result1)
# print("==----------=1")
#
# result2 = request1.post_request2()
# print(result2)
# print("==----------=2")
#
# result3 = request1.get_request1()
# print(result3)
# print("==----------=3")

"""
学习方法：
1、方法或者代码即便是相同的，不要复制，用手敲来代替，锻炼熟悉度

"""

























