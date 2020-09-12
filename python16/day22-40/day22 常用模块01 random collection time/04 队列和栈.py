#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/6/27 14:56

''''''
'''
队列 queue  先进先出，后进后出   first in first out   FIFO   类比例子：银行柜台办业务
栈  stack   后进先出，先进后出   first in last out    FILO   类比例子:电梯  子弹夹

队列的代码
思路：
1、导包
2、创建一个队列对象
3、往空队列里面加元素--人
4、先进先出，从队列里面取元素

'''

# 1、导包
import queue

# 2、往空队列里面加元素--人
q = queue.Queue()   #创建一个队列对象
q.put('jack')
q.put('tom')
q.put('bob')
print(q)   #<queue.Queue object at 0x00000223EE5E9F98>
# print(dir(q))  #不包含__iter__ 说明队列对象不是interable

# 3、先进先出，从队列里面取元素
print(q.get())   #jack  #先进先出
print(q.get())   #tom
print(q.get())   #bob
# print(q.get())  #队列有3个人，取第4个元素的时候，会夯在这里（阻塞在这里，等下一个元素）  #input--不enter就一直夯住
print('---------------------------1 队列')























