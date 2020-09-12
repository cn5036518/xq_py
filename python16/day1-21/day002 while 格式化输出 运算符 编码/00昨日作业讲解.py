#!/usr/bin/env python
#-*- coding:utf-8 -*-

# month = input("请输入月份:") # 1月
# if month == '1月':
#     print("卤煮")
# if month == '2月':
#     print("卤煮火烧")
# if month == '3月':
#     print("卤煮不要饼")

month = input("请输入月份:") # 1月
if month == '1月':
    print("卤煮")
elif month == '2月':
    print("卤煮火烧")
elif month == '3月':
    print("卤煮不要饼")

#上述3个if和1个if 2个elif的效率是不一样的，后者的效率要高
"""
3个if 每次都要判断3次
1个if 2个elif 也许只需要判断1次即可，下面的效率要高

"""
















