#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/7 6:51
#@author:wangtongpei

# 6，用filter来处理,得到股票价格大于20的股票名字
shares={
   	'IBM':36.6,
   	'Lenovo':23.2,
  	'oldboy':21.2,
    'ocean':10.2,
	}


li61 = filter(lambda x:x[-1]>20,shares.items())
print(list(li61))  #[('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]
print('----------------------1')

def func62(items1):
    if items1[1] >20:
        return items1   #返回的是参数，键值对
li62 = filter(func62,shares.items())  #shares.items()的每一个元素都是键值对
print(list(li62)) #[('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]
#最后返回的是键值对，组成的列表
print('----------------------2')

def func621(items1):
    return items1[1] >20   #返回的是参数，键值对
li621 = filter(func621,shares.items())  #shares.items()的每一个元素都是键值对
print(list(li621)) #[('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]
#最后返回的是键值对，组成的列表
print('----------------------2-2')
'''
分析过程1：
1 遍历循环字典.items()后，每一个元素都是键值对元组,而不是key，在这里--关键点
2 把每一个键值对元组依次作为参数items1传入
3 当字典的值items1[1]大于20的时候
4 将字典的items1(即参数)返回，而不是字典的key返回
5 最后返回的是满足条件的items1（键值对元组）组成的列表
'''

it63 = filter(lambda k:shares[k]>20,shares)
print(list(it63)) #['IBM', 'Lenovo', 'oldboy']
print('----------------------3')
'''
分析过程2：
1 遍历循环字典后，每一个元素都是key,而不是键值对，在这里--关键点
2 把每一个key依次作为参数k传入
3 当字典的值share[k]大于20的时候
4 将字典的k返回，而不是字典的键值对返回
5 最后返回的是满足条件的key组成的列表
'''

for i in shares:
    print(i)  #这个i是字典的key，而不是键值对
# IBM
# Lenovo
# oldboy
# ocean
print('----------------------3-1')

for i in shares.items():
    print(i)  #这个i是字典的key，而不是键值对
# ('IBM', 36.6)
# ('Lenovo', 23.2)
# ('oldboy', 21.2)
# ('ocean', 10.2)
print('----------------------3-2')

def func64(key):
    if shares[key]>20:
        return key   #返回的是字典的key，而不是字典的键值对
li64 = filter(func64,shares)
print(list(li64)) #['IBM', 'Lenovo', 'oldboy']
#最后返回的是满足条件的key组成的列表
print('----------------------4')

def func65(key):
    return shares[key]>20  #返回的是字典的key，而不是字典的键值对 关键点
li65 = filter(func65,shares)
print(list(li65)) #['IBM', 'Lenovo', 'oldboy']
print('----------------------5')

'''
小结：
filter函数+匿名函数，当iterable是字典的时候
it1 = filter(lambda k:dic1[k]>20,dic1)
print(list(it1))  #传入的参数是key，返回的就是key组成的列表

it2 = filter(lambda items1:items1[-1]>20,dic1.items())
print(list(it2))  #传入的参数是item（键值对元组），返回的就是键值对元组组成的列表

上述两个的区别
1 前者返回的是符合条件（字典的value-dic1[k]大于20）的字典key，组成的列表
    ['IBM', 'Lenovo', 'oldboy']
2 后者返回的是符合条件（字典的value-items[1]大于20）的字典的items（键值对元组），组成的列表
    [('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]

'''












