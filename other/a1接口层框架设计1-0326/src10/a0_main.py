#!/usr/bin/env python
#-*- coding:utf-8 -*-

from a2_forcase import Forcase
from a1_interface import  Interface_test

#1新建对象
forcase1 = Forcase()
#2对象调方法
ret1 = forcase1.forcase()
# print(ret1)

#2新建对象
# test1 = Interface_test(url, params1, headers1, check_point1, method1, data_type1,yes_no1,i+2)  # 自动执行构造方法，传入参数
for i in ret1:
    # print(i)
    test1 = Interface_test(*i)  # 自动执行构造方法，传入参数
    #注意：这里的行号必须是i+2 而不是i或者i+1  i+2的话，第一次循环是2，第二次循环是3，for只循环2次
    #     方法论的关键是 将i+2的值打印出来，可见不跳步骤，一步一步打印的重要性+耐心
    # #对象调方法
    test1.test()

"""
总结：结构+知识点+依次迭代
一、结构
1、请求类
    目的：实现requests的post或者get请求，得到响应数据
    知识点：请求返回的是json类型，将json类型转换成python的字典类型 dic1 = r.json()
            并且加上异常处理
二、遍历case类
    目的：读取excel中的内容，将读取后的内容返回给接口类作为入参
    方式：通过for循环遍历case
    知识点：对于入参报文和检查点的读取，从excel中读取的是json字符串，必须要先将json转换成python的字典来使用
         params1 = json.loads(params1)
         2、将读取的多个字段，作为元组，元组整体作为元素依次添加到空列表
            返回的列表，包含2个元组（2行数据），元组的没有元素分别是读取的字段





"""























