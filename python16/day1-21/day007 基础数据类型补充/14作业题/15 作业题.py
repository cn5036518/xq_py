#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 3. 完成彩票36选7的功能. 从36个数中随机的产生7个数. 最终获取到7个不重复的数据作为最终的开奖结果.
# 随机数:
# from random import randint
# randint(0, 20) # 0 - 20 的随机数

import random
#方法1  sample
"""
思路：
1产生36个数字，存在列表1中
2从列表1中随机取7个数  --sample

"""

# li1 = []
# for i in range(36):
#     li1.append(i)
# print(li1)   #1产生36个数字，存在列表中

set1 = set()
# for i in range(100):   #限定范围
while 1:
    int36 = random.randint(0, 100)  #1从0-100这个范围（包含100），随机获取36个不重复的数字，添加到集合
    # Return random integer in range [a, b], including both end points.
    set1.add(int36)
    if len(set1) == 36:
        break
print(set1)
# print(len(set1)) #36

li2 = random.sample(set1,7)    #参数1是列表或者集合  参数2是随机获取的个数(获取的数是不重复的)  返回的是列表2
# Chooses k unique random elements from a population sequence or set.
print(li2)  #[11, 7, 23, 13, 27, 16, 24]
print("--------------1")

#方法2  sample的实现算法
"""
思路：
1产生36个数字，存在列表1中,将列表去重，转成集合（去重、无序、元素不可变）
2从集合1中随机取7个数  --sample
"""

# int36 = random.randint(0,35)  #返回0-35之间，包含35的随机数，每次返回一个数字
# # Return random integer in range [a, b], including both end points.
# print(int36)

li1 = []
for i in range(36):
    int36 = random.randint(0, 35)
    li1.append(int36)  #问题：虽然尝试了36次随机数，但是这36个随机数中有重复的，去掉重复后，就没有36个不重复的随机数了
print(li1)
set1 = set(li1)
print(set1)   #去重

set2 = set()
count = 0
for i in set1:
    if count <7:
        set2.add(i)
    count +=1
print(set2)  #{32, 1, 2, 3, 4, 5, 7}   集合是无序，去重、元素不可变
print("---------------2")

#方法3  sample的实现算法  改进
"""
思路
1 随机产生数字，依次添加到空集合中，由于集合的（无序、去重、元素不可变）
  当集合的元素是36个时（长度len），就停止添加
2、新建空集合2
    遍历循环集合1，计数器从0开始，当计数器小于7的时候，依次把集合1的元素添加到集合2
    由于集合的（去重、无序）的特点，所有7位数字，是无序且不重复的
"""

set1 = set()
# for i in range(100):   #限定范围
while 1:
    int36 = random.randint(0, 100)  #1从0-100这个范围，随机获取36个不重复的数字，添加到集合
    # Return random integer in range [a, b], including both end points.
    set1.add(int36)  #2 单个添加数字到集合1中
    if len(set1) == 36: #3 当集合1的长度是36时，即已经有了36个不重复的数字时，就停止添加
        break
print(set1)
print(len(set1)) #36

set2 = set()
count = 0
for i in set1:   #2 从36个数字的集合中，随机选择7个数字   集合特点（无序、去重、元素不可变）
    if count <7:
        set2.add(i)
    count +=1  #计数，只添加7个
print(set2)  #{32, 1, 2, 3, 4, 5, 7}   集合是无序，去重、元素不可变
print("---------------3")

#方法4 老师  推荐 好理解
"""
思路：
1、从1-36这个范围，随机获取一个数 randint(1,36)
2、for循环7次，获得7个随机数（但是这7个随机数可能有重复，如何去重）
3、定义一个空集合set1 = set()
4、往空集合中添加随机数，当空集合的长度是7的时候，停止，不再增加
注意点：
产生7个随机数容易解决，如何让这7个数不重复--集合去重，集合长度
"""

set1 = set()  #1定义空集合  去重
# for i in range(100): #2循环遍历100次
while 1:  #不限定循环次数
    num = random.randint(1,36)  #每次循环，都产生一个范围是1-36之间的随机数（这个随机数是有可能重复的）
    set1.add(num) #3 把产生的随机数添加到集合
    if len(set1) ==7: #4 当集合的长度是7的时候，停止新增，跳出循环  关键点：产生7个随机数容易，如何让这7个数不重复--集合去重
        break
print(set1)  #{32, 36, 14, 18, 21, 24, 29}
print("---------------4")

#方法5 老师  推荐2 好理解  最简洁 5行代码
"""
思路：
1、从1-36这个范围，随机获取一个数 randint(1,36)
2、for循环7次，获得7个随机数（但是这7个随机数可能有重复，如何去重）
3、定义一个空集合set1 = set()
4、往空集合中添加随机数，当空集合的长度是7的时候，停止，不再增加（可以在while循环中break，也可以写在while后面）
    （如果是for循环，只能break；而while除了break，还可以写在while后面）
注意点：
产生7个随机数容易解决，如何让这7个数不重复--集合去重，集合长度
"""

set1 = set()  #1定义空集合  去重
# for i in range(100): #2循环遍历100次
while len(set1)< 7:  #限定循环次数0-6（此时已经添加了7个不重复的数到集合）,当集合的长度是7，就不再循环
    #注意点：这里是小于7，是7个随机数（0-6 一共是7个） ；如果是小于等于7，就是8个随机数（0-7，一共是8个）
    num = random.randint(1,36)  #每次循环，都产生一个范围是1-36之间的随机数（这个随机数是有可能重复的）
    set1.add(num) #3 把产生的随机数添加到集合
    # if len(set1) ==7: #4 当集合的长度是7的时候，停止新增，跳出循环  关键点：产生7个随机数容易，如何让这7个数不重复--集合去重
    #     break
print(set1)  #{32, 36, 14, 18, 21, 24, 29}
print("---------------5")


















