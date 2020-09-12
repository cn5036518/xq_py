#!/usr/bin/env python
#-*- coding:utf-8 -*-


import json
import requests


# url = "http://v.juhe.cn/laohuangli/d"
# params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# headers1 = {}

class Http_request2:
    def __init__(self,url,params1,headers1):
        self.url = url
        self.params1 = params1
        self.headers1 = headers1

    def post_request1(self):
        r = requests.post(self.url,params=self.params1,headers= self.headers1)
        dic1 = r.json()
        # print(dic1)
        return dic1

    def get_request2(self):
        pass

# h1= Http_request1(url,params1,headers1)
# h1.post_request1()














