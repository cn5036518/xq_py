#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/7 5:54
#@author:wangtongpei

''''''
'''
内置函数或者和匿名函数结合输出
4，用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
	name=[‘oldboy’,'alex','wusir']

5，用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
	l=[{'name':'alex'},{'name':'y'}]

6，用filter来处理,得到股票价格大于20的股票名字
shares={
   	'IBM':36.6,
   	'Lenovo':23.2,
  	'oldboy':21.2,
    'ocean':10.2,
	}

7,有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
结果：list一下[9110.0, 27161.0,......]
portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]

8,还是上面的字典，用filter过滤出单价大于100的股票。

9,有下列三种数据类型，
	l1 = [1,2,3,4,5,6]
	l2 = ['oldboy','alex','wusir','太白','日天']
	tu = ('**','***','****','*******')
写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个）
	[(3, 'wusir', '****'), (4, '太白', '*******')]这样的数据。

10,有如下数据类型：
	l1 = [ {'sales_volumn': 0},
     		{'sales_volumn': 108},
     		{'sales_volumn': 337},
     		{'sales_volumn': 475},
     		{'sales_volumn': 396},
     		{'sales_volumn': 172},
     		{'sales_volumn': 9},
     		{'sales_volumn': 58},
     		{'sales_volumn': 272},
     		{'sales_volumn': 456},
     		{'sales_volumn': 440},
     		{'sales_volumn': 239}]
将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
'''

# 4，用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# 	name=[‘oldboy’,'alex','wusir']
name=['oldboy','alex','wusir']
it2 = map(lambda x:x+'_sb',name)
print(it2)   #返回的是迭代器
print(list(it2))  #把迭代器转成列表
#['oldboy_sb', 'alex_sb', 'wusir_sb']
print('----------------------------------4')

# 5，用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# 	l=[{'name':'alex'},{'name':'y'}]
#方法1  --本题正确写法
l=[{'name':'alex'},{'name':'y'}]
it5 = map(lambda dic:dic['name']+'sb',l)
# 列表的元素是字符串
print(it5)
print(list(it5))  #['alexsb', 'ysb']
print('----------------------------------5-1')

#方法2  --
l=[{'name':'alex'},{'name':'y'}]
it52 = map(lambda dic:{'name':dic['name']+'sb'},l)
# 列表的元素是字典
print(list(it52))  #[{'name': 'alexsb'}, {'name': 'ysb'}]
print('----------------------------------5-2')

'''
第5题小结
方法1：返回的是列表，列表的元素是字符串
       将原字典的value进行了批量修改后，把原字典的value作为新列表的元素
方法2：返回的是列表，列表的元素是字典
       将原字典的value进行了批量修改，将修改后的字典作为新列表的元素
'''

# 8,还是上面的字典，用filter过滤出单价大于100的股票。
portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]

it8 = filter(lambda dic:dic['price']>100,portfolio)
print(it8)
print(list(it8))
#[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
print('----------------------------------8')

# 10,有如下数据类型：
# 	l1 = [ {'sales_volumn': 0},
#      		{'sales_volumn': 108},
#      		{'sales_volumn': 337},
#      		{'sales_volumn': 475},
#      		{'sales_volumn': 396},
#      		{'sales_volumn': 172},
#      		{'sales_volumn': 9},
#      		{'sales_volumn': 58},
#      		{'sales_volumn': 272},
#      		{'sales_volumn': 456},
#      		{'sales_volumn': 440},
#      		{'sales_volumn': 239}]
# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
l1 = [ {'sales_volumn': 0},
        {'sales_volumn': 108},
        {'sales_volumn': 337},
        {'sales_volumn': 475},
        {'sales_volumn': 396},
        {'sales_volumn': 172},
        {'sales_volumn': 9},
        {'sales_volumn': 58},
        {'sales_volumn': 272},
        {'sales_volumn': 456},
        {'sales_volumn': 440},
        {'sales_volumn': 239}]
li10 = sorted(l1,key=lambda dic:dic['sales_volumn'],reverse = False)
print(li10)  #返回的是列表
#[{'sales_volumn': 0}, {'sales_volumn': 9}, {'sales_volumn': 58}, {'sales_volumn': 108},
#  {'sales_volumn': 172}, {'sales_volumn': 239}, {'sales_volumn': 272}, {'sales_volumn': 337},
#  {'sales_volumn': 396}, {'sales_volumn': 440}, {'sales_volumn': 456}, {'sales_volumn': 475}]
print('----------------------------------9')

'''
sorted（） 函数返回的是列表等iterable
filter()函数和map（）函数 返回的是iterator（可以转成列表）
'''
















