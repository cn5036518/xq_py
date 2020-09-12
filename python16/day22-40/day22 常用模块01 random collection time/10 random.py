#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/25 9:44

''''''
'''
需求1：
1、产生随机小数

'''

import random

print(random.random())   #产生0-1之间的随机小数  x in the interval [0, 1)
#0.5044532692647281
print(random.uniform(1,2))  #产生1-2之间的随机小数  [1,2)或者[1,2]
#Get a random number in the range [a, b) or [a, b] depending on rounding
print('-----------------------------   产生随机小数1')

'''
小结1：
产生指定范围内随机小数
random.random()      产生[0,1）之间的随机小数，左闭右开
random.uniform(a,b)  产生[a,b]或者[a,b)之间的随机小数  左闭右开或者左闭右闭
'''

'''
需求2
1、产生指定范围内的随机整数

'''

print(random.randint(1,2))  #Return random integer in range [a, b], including both end points
#产生[1,2]范围内的整数
print(random.randrange(1,5,3))  #在[1,5)范围内，步长是3，取随机整数值，要么输出1，要么输出4
#Choose a random item from range(start, stop[, step])

'''
小结2：
产生指定范围内随机整数
random.randint(a,b)      产生[a,b]之间的随机整数，左闭右闭
random.randrange(a,b,step)  产生[a,b)范围内，步长是step，取随机整数值
'''
print('-----------------------------   产生随机整数2')

li1 = ['jack','tom','bob']
print(random.choice(li1))   #Choose a random element from a non-empty sequence.
#参数是列表（元组等序列），从列表中随机获取一个元素

print(random.sample(li1,2))  #从参数1：序列或者集合中 随机获取2个元素组成的序列或者集合
#['tom', 'jack']
#Chooses k unique random elements from a population sequence or set
print(random.sample(list(range(1,37)),7))  #[26, 6, 21, 34, 12, 10, 28]
#从1-37个数字中，随机获取7个数字，组成一个列表
print('-----------------------------   从序列中获取1个元素，或者获取多个元素组成的序列3')

li2 = [1,2,3,4,5]
random.shuffle(li2) #改变列表本身，将列表中元素的顺序打乱
#Shuffle list x in place, and return None
print(li2)  #[1, 2, 4, 5, 3]

'''
小结
1、指定范围内随机小数
random.random()    #输出[0,1)范围内的随机小数
random.uniform(a,b) #输出[a,b]或者[a,b)范围内的随机小数

2、指定范围内随机整数
random.randint(a,b)  #输出[a,b]之间的随机整数
random.randrange(a,b,step)  #在[a,b)范围内，步长是step，取随机整数

3、从列表、序列中获取一个元素，多个元素组成的序列
random.choice(序列)             #从sequence（列表、元组等序列）中随机获取一个元素
random.sample(序列或者集合,n)   #从序列或者集合中随机获取n个元素，组成新的序列或者集合

4、打乱顺序
random.shuffle(list)  #将列表本身改变，列表元素的顺序打乱，返回是None


'''






