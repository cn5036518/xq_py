#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 6,写函数,传入函数中多个实参(实参均为字典),将每个实参的键值对依次添加到函数的动态参数kwargs里面.
# 例如 传入函数两个参数{‘name’:’alex’} {‘age’:1000}最终kwargs为{‘name’:’alex’ ,‘age’:1000}

def func(**kwargs):
    print(kwargs)  #{'age': 1000, 'name': 'alex'}

dic1 = {'name':'alex'}
dic2 = {'age':1000}
dic1['age'] = dic2['age']  #把dic2的元素-键值对 添加到dic1中
print(dic1)  #{'name': 'alex', 'age': 1000}

func(**dic1)











