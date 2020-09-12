#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/7/25 15:42

import queue

'''
1、新建一个队列对象
2、往队列中添加元素
3、从队列中拿出元素
'''

d1 = queue.Queue()
d1.put(1)
d1.put(2)
d1.put(3)
print(d1)  #<queue.Queue object at 0x000001EFB90473C8>

print(d1.get())  #1
print(d1.get())  #2   先进先出
print(d1.get())  #2   先进先出
# print(d1.get())  #    这里程序会阻塞，队列里面没有了的情况



















