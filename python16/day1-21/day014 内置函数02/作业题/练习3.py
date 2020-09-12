#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/7 7:55
#@author:wangtongpei

# 7,有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
# 结果：list一下[9110.0, 27161.0,......]
portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]

#方法1 普通函数
def func1(dic1):
    return dic1['shares'] * dic1['price']

# func1(portfolio)
it1 = map(func1,portfolio)
print(list(it1))  #[9110.0, 27161.0, 4218.0, 1111.25, 735.7500000000001, 8673.75]
print('------------------1 map+普通函数')
'''
分析过程：
1 portfolio是列表，列表的每一个元素是字典
2 把字典作为普通函数的参数，依次传入，将股票价格*股票数量=股票总价值 作为元素返回
3 最后得到股票总价值作为元素的列表
注意：map和filter不同的地方
1、map最后得到的是将普通函数（或者匿名函数）的返回值作为元素的列表
2、filter最后得到的是普通函数（或者匿名函数）的参数（参数经过了筛选，返回的是True）作为元素的列表
'''

#方法2 匿名函数
it2 = map(lambda dic1:dic1['shares'] * dic1['price'],portfolio)
print(list(it2))
#[9110.0, 27161.0, 4218.0, 1111.25, 735.7500000000001, 8673.75]
print('------------------2 map+匿名函数')

'''
方法论小结：
当匿名函数一下子写不出来的时候，就需要先写出普通函数（写普通函数的过程就是在整理思路）
   然后，将普通函数的参数和返回值，填入匿名函数即可，匿名函数就写出来了
'''












