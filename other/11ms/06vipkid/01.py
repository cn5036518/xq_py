#!/usr/bin/env python
#-*- coding:utf-8 -*-

#列表中的元素打散（重新排列），每个元素不能出现在原来的位置
# 比如 li1= [1,2,3]  元素1不能出现在位置1  元素2不能出现在位置2 元素3不能出现在位置3
import random
li1= ["a","b","c"]
li2 = []
# for i in range(len(li1)): #0-2
#     num1 = random.randrange(0,len(li1)) #0-2
#     if i != num1:
#         li2.append(li1[num1])
#     else:
#         li2.insert(0,li1[num1])
# print(li2)
# print("-----------0")

"""
i =0  num1= 1,2
i =1 num1= 0,2
i =2 num1= 0,1
"""

# li1= ["a","b","c"]
# li3 = []
# for i in range(len(li1)):
#     li2 = li1[:]
#     li2.remove(i)
#     s1 = random.choice(li2)
#     li2.append(s1)
#     li2 = li1[:]
#
# print(li3)


set3 = {22,11}
print(set3)  #{11, 22}
li2 = []
for i in set3:
    li2.append(i)
print(li2)  #[11, 22]   #集合是无序的，但是在py3.3版本中，遍历循环集合的每个元素，依次添加到空列表的时候
#每次都是11排在前面，22排在后面（字典是无序的，但是3.6版本之后，字典在控制台显示的是按照添加顺序来的，但是
#实际上，在内存中字典的key是无序的；同理，集合也是无序的,但是在控制台输出，每次都是11在前，22在后，但是实际上
#集合的元素在内存中是无序的  ）












