#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/8/16 16:41

import random

#一 返回小数
print(random.random())   #返回0-1的小数 范围是[0,1) 左闭右开
#x in the interval [0, 1).
# 0.21493505107136868

print(random.uniform(1,2.1))  #返回[1,2.1]之间的小数  这里的参数可以是小数
#Get a random number in the range [a, b) or [a, b] depending on rounding.
print('-------------------------------------   返回随机小数')

#二 返回整数
print(random.randint(1,3)) #返回[1,3]的整数 参数只能是整数，不能是小数
#Return random integer in range [a, b], including both end points.

print(random.randrange(1,3,2))  #返回范围是[1,3)之间的整数，步长是2  参数只能是整数，不能是小数
#Choose a random item from range(start, stop[, step])
print('-------------------------------------   返回随机整数')

#三 选择一个元素
li1 = [1,3,2]
print(random.choice(li1))   #每次返回列表中的一个随机元素
#Choose a random element from a non-empty sequence

#四 选择返回多个元素组成的列表
li2  = [1,3,2]
print(random.sample(li2,2))  #[3, 2]   每次返回列表中随机2个元素组成的列表
#Chooses k unique random elements from a population sequence or set

#五  将列表的元素顺序给打乱--列表本身改变了
li3 = [1,3,5]
print(random.shuffle(li3)) #None  #返回值是None，列表本身改变了
print(li3)  #[5, 1, 3]
#Shuffle list x in place, and return None

'''
小结
1、返回一个随机小数
    random()        #返回[0,1)之间的小数， 左闭右开
    uniform(1,2.1)  #返回[1,2.1]之间的小数，参数可以是小数  左闭右闭

2、返回一个随机整数
    randint(1,3)      #返回[1,3]之间的一个随机整数，参数只能是整数，不能是小数  左闭右闭
    randrange(1,4,2)  #返回[1,4)之间，步长是2的一个随机整数   左闭右开
 
3、返回列表中的单个元素
   choice(list)
   
4、返回列表中多个元素组成的列表
   sample(list,2)
   
5、将列表的元素打乱，改变列表本身
    shuffle(list)

'''



















