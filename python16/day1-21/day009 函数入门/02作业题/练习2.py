#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
'''

'''
思路：
切片

题目多读几遍
1、如何输出列表的奇数位索引对应的元素（奇数位元素）
'''
#方法1  推荐  简洁
def odd(li):  #形参不带1
    return li[::2]  #返回列表的奇数位索引对应的元素
    # 浅拷贝 li[:]

li1 = [1,3,5,6]  #实参后面可以带1
ret = odd(li1)
print(ret)  #[1, 5]

#方法2
def odd1(li):
    li2 = []
    for i in range(len(li)):  #遍历列表，取索引号
        if i%2 ==1:  #取模余数是1，就是索引号是奇数
            li2.append(li[i])  #根据索引号取列表的元素值  知识点
    return li2

li1 = [1, 3, 6, 4]
ret2 = odd1(li1)
print(ret2)








