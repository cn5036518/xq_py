#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
4，写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者。
'''

def first_two_items(li): #形参的名字用li 一看就知道是列表
    if len(li) > 2:
        # return li[0],li[1]   #分别返回前2个元素
        return li[:2]  #把列表的前2个元素切片后，形成一个新的列表返回

li1 = ['a','b','c']
ret = first_two_items(li1)
print(ret) #['a', 'b']











