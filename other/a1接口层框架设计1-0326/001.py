#!/usr/bin/env python
#-*- coding:utf-8 -*-


import re
#

#
# int1=0
# str2 = str(int1)
# print(str2)
#
# str1 ="0"
# print(str1)

# for i in range(2):
#     print(i)

import json

json_str1 = '{"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}'
dic1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace", "date": "2016-5-14"}
# dic1 = dict(str1)
# print(dic1)

# # JSON到字典转化：
dictinfo = json.loads(json_str1)
print(dictinfo)
print(type(dictinfo))

dic2 = {'error_code': "0",'reason': 'successed'}
if "error_code" in dic2:
    print("0k")

str2 =str(dic2)
print(type(str2))

str1 = '"error_code":"0"'

result = re.search(str1, str2).group()
print(result)



















