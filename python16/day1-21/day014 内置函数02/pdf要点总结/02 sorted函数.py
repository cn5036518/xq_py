#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/5 16:10
#@author:wangtongpei

''''''
'''
sorted（）函数
写法：sorted（iterable,key=func,reverse=False）
原理：把iterable中的每一个元素，依次作为参数，传递给自定义函数，返回值是数字-int，然后进行排序（默认升序）
    比如：列表中是int，字符串等元素
          列表中是字典--学生信息（按照学生的年龄进行排序）
          列表中是元组--字典的value进行排序  dic.items()

sort（）和sorted()的区别
1、前者是列表的内置函数，排序后，将列表本身修改了
    写法：li1.sort()
2、后者可以用于iterable，排序后，产生一个新的排序后的列表，原列表本身没有修改
    写法：li2 = sorted(li1)
'''

#1列表的排序
li1 = [1,3,2]
li2 = sorted(li1)
# li2 = sorted(li1,key=None,reverse=False)  #和上面行等效
print(li2)  #[1, 2, 3]
print('----------------------1 列表的排序')

#2字典的排序
#01 按照字典的key进行排序
dic1 = {'1':'jack','3':'jack3','2':'jack2'}
dic2 = sorted(dic1)  #将字典的key进行排序
print(dic2)  #['1', '2', '3']
print('----------------------2-1 字典的排序 字典的key排序')

#02 按照字典的value进行排序
dic1 = {'1':'jack','3':'jack2','2':'jack3'}
print(dic1.items())  #dict_items([('1', 'jack'), ('3', 'jack3'), ('2', 'jack2')])
#将字典通过items()转换成列表嵌套元组的形式，将元组作为整体传递到自定义函数的参数中

li2 = sorted(dic1.items(),key=lambda x:x[1])  #将列表中的元组，按照元组的第2项（字典的value）进行排序
print(li2)  #[('1', 'jack'), ('3', 'jack2'), ('2', 'jack3')]

dic3 = {}
for i in li2:
    dic3[i[0]] = i[1]
print(dic3) #{'1': 'jack', '3': 'jack2', '2': 'jack3'} #将字典的value进行排序
print('----------------------2-2 字典的排序 字典的value排序')

#03 按照列表的元素长度来排序
li3 = ['jack','tom','james']
li4 = sorted(li3,key=lambda x:len(x))
print(li4)  #['tom', 'jack', 'james']
print('----------------------3-1 按照列表的元素长度来排序  sorted+lambda')

#04 按照学生的年龄来排序（列表中嵌套字典）
li4 = [{'name':'jack','age':18},
       {'name': 'tom', 'age': 15},
       {'name': 'bob', 'age': 19}]
li5 = sorted(li4,key=lambda dic:dic['age'])
print(li5)
#[{'name': 'tom', 'age': 15}, {'name': 'jack', 'age': 18}, {'name': 'bob', 'age': 19}]
#分析：列表中嵌套字典，字典是作为一个元素，整体传递给自定义函数的参数的









