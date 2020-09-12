#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
8，写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。
例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
'''

def list_convert_dic(li):
    if type(li)!=list: #如果参数类型不是列表，就抛出异常  --排除法去判断
        print('抛出异常')
        return False
    else:  #如果是列表
        dic1 = {}
        for i in range(len(li)):  #获取列表的索引号和列表的元素（可以获得列表的索引号）--关键点
        # for i in li1:   #只能获取列表的元素，而无法获取列表的索引号
            dic1[i] = li[i]   #这里i是列表的索引号-下标，li1[i]根据列表的下标取列表的元素值  关键点
        return dic1

li1 = [11,22,33]
ret = list_convert_dic(li1)
print(ret)  #{0: 11, 1: 22, 2: 33}

'''
复习列表的根据下标取列表的元素值
'''

# print(2/0)  #ZeroDivisionError: division by zero
#抛出异常
# print(divmod(10,3))  #(3,1)  #求商和余数







