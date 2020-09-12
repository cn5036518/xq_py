#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
5，文件t51.txt内容(升级题)

name:apple price:10 amount:3 year:2012
name:tesla price:100000 amount:1 year:2013
.......

通过代码，将其构建成这种数据类型：
[{'name':'apple','price':10,'amount':3},
{'name':'tesla','price':1000000,'amount':1}......]
并计算出总价钱。
'''

f = open('t51.txt',mode='r',encoding='utf-8')
# s5 = f.read()
# print(s5)
li1 = []
for i in f:
    name1,price1,amount1,year1 = i.strip().split()   #拆包 分包
    print(name1)
    a1,b1 = name1.split(':')
    a2,b2 = price1.split(':')
    a3,b3 = amount1.split(':')
    dic1  = {}   #必须在for循环之内，而不能在for循环之外--关键点
    dic1[a1] = b1
    dic1[a2] = int(b2)  #字符串转换成int，方便计算总价钱
    dic1[a3] = int(b3)
    # print(dic1)
    li1.append(dic1)
print(li1) #
f.close()
# [{'name': 'apple', 'amount': '3', 'price': '10'},
# {'name': 'tesla', 'amount': '1', 'price': '100000'}]

#计算总价钱
total = 0
for i in li1:
    # print(i)
    total += i['price']*i['amount']
print(total)  #100030

'''
伪代码思路：
1、读取文件的每一行
2、遍历循环文件对象
3、空格拆分每一行，得到键值对
4、冒号拆分每一个键值对，构成字典
5、字典依次追加都空列表
'''











