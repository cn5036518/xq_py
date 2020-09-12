#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 12写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]

def poker(num,spade):
    n = 0
    for i in num:
        for j in spade: #扑克的花色（桃心梅方）
            print((j, i))
            n += 1
    print(n)  #一共是52张牌

spade1 = ['黑桃', '红心', '梅花', '方块'] #4个
num1 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] #13个
#2个集合，两两相乘，笛卡尔积
poker(num1,spade1)

















