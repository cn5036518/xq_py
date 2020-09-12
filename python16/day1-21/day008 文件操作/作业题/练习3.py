#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
3，文件a.txt内容：每一行内容分别为商品名字，价钱，个数。

apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},
{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
'''

f = open('a.txt',mode='r',encoding='utf-8')
li1 = []
# dic1 = {}  #注意点：# dic1 = {}不能放在这里（不能放在for循环外）
# 如果放在外面，5次小循环后，5个字典的值是一样的（5个字典是 一改都改）
for i in f:
    name1,price1,amount1=i.strip().split()  #拆分  默认空白（空格 \t \n）去拆分
    # name1,price1,amount1=i.strip().split('\t')  #拆分   /t   tab去拆分（生产环境注意用tab这个）
    dic1 = {}   #注意点：# dic1 = {}必须放在for循环内，这样，每次小循环后的值都是不一样的
    # （5个字典不是 一改都改，而是独立的）
    print(name1)
    dic1['name'] = name1
    dic1['price'] = int(price1)  #字符串转换成int 方便计算
    dic1['amount'] = int(amount1) #字符串转换成int 方便计算
    print(dic1)  #{'amount': '1', 'name': 'tesla', 'price': '100000'}
    li1.append(dic1)  # [{'amount': '1', 'name': 'tesla', 'price': '100000'}]
print(li1)
f.close()

# apple
# {'price': '10', 'name': 'apple', 'amount': '3'}
# tesla
# {'price': '100000', 'name': 'tesla', 'amount': '1'}
# [{'price': '10', 'name': 'apple', 'amount': '3'}, {'price': '100000', 'name': 'tesla', 'amount': '1'}]

'''
过程分析：
1、dic1 = {}如果放在for循环外，那么第一次小循环后，
   dic1={'price': '10', 'amount': '3', 'name': 'apple'}
   第二次小循环后
   {'price': '100000', 'amount': '1', 'name': 'tesla'}
   。。。
   第五次小循环后
   {'price': '10', 'amount': '3', 'name': 'chicken'}
   每次小循环后，dic1都没有重置成{}，就相当于把前一次小循环的值给修改了
   即5次小循环后的字典值都是一样的
   li1就是  [{'price': '100000', 'amount': '1', 'name': 'tesla'},
   {'price': '100000', 'amount': '1', 'name': 'tesla'}]
   而不是
   [{'amount': '3', 'name': 'apple', 'price': '10'},
    {'price': '100000', 'amount': '1', 'name': 'tesla'}]
   注意点：这里是2条一样的tesla，是因为列表的元素-字典修改后，将字典作为第二个元素添加的时候
           列表的第一个元素-字典也随之变化了

2、dic1 = {}如果放在for循环内，那么第一次小循环后，
    dic1={'price': '10', 'amount': '3', 'name': 'apple'}
   第二次小循环后
   {'price': '100000', 'amount': '1', 'name': 'tesla'}
   。。。
   第五次小循环后
   {'price': '10', 'amount': '3', 'name': 'chicken'}
   每次小循环后，dic1都重置成{}，就相当于前一次小循环的值没有修改
   即5次小循环的值都是不同的
'''
print('---------------1')

# 计算出总价钱
print(li1)
#[{'name': 'apple', 'amount': '3', 'price': '10'}, {'name': 'tesla', 'amount': '1', 'price': '100000'}]
total = 0
for i in li1:
    print(i)
    total += i['price']*i['amount']
print(total)  #100030









