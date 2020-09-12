#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/25 15:56

from collections import deque

'''
1 新建一个双向队列的对象
2 添加元素到双向队列
3 删除元素
'''

d1 = deque()
d1.append(1)
d1.append(2)
d1.appendleft(3)
d1.appendleft(4)
print(d1)  #deque([4, 3, 1, 2])
print(list(d1))  #[4, 3, 1, 2]

print(d1.pop())  #2  删除最右边的元素，并且返回被删除的元素
print(d1)  #deque([4, 3, 1])
print(d1.popleft())  #4  删除最左边的元素，并且返回被删除的元素
print(d1)  #deque([3, 1])


















