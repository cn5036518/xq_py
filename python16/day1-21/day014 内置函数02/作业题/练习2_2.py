#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/9 9:41
#@author:wangtongpei
#@email: cn5036520@163.com

# 6，用filter来处理,得到股票价格大于20的股票名字
shares={
   	'IBM':36.6,
   	'Lenovo':23.2,
  	'oldboy':21.2,
    'ocean':10.2,
	}

#方法1
it1 = filter(lambda k:shares[k]>20,shares)  #匿名函数的参数是字典的key
print(list(it1))  #['IBM', 'Lenovo', 'oldboy']
print('-----------------------------1')

#方法2
it2 = filter(lambda x:x[-1]>20,shares.items()) #匿名函数的参数是字典的键值对元组
print(list(it2))  #[('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]
print('-----------------------------2')

#方法3
it3 = filter(lambda x:x[-1]>20,shares.items())
li3 = list(it3)
print(li3)  #[('IBM', 36.6), ('Lenovo', 23.2), ('oldboy', 21.2)]

it4 = map(lambda x:x[0],li3)  #获取iterable中每个元素的第一项
print(list(it4))  #['IBM', 'Lenovo', 'oldboy']
print('-----------------------------3')









