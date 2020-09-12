#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/5/24 11:38

''''''
'''
需求：
写一个迭代器  iterator

思路：
1、生成器的本质是迭代器
2、先写一个生成器
3、通过生成器表达式来写生成器
4、类中含有__iter__()，那么该类的对象就是可迭代的对象iterable
'''

class Foo:
    def __iter__(self):
        return (i for i in range(3))    #返回 生成器表达式--生成器--迭代器iterator

f1 = Foo()  #f1是可迭代的对象  iterable
print(f1)  #<__main__.Foo object at 0x0000020D11D69E48>
print(type(f1))  #<class '__main__.Foo'>
for i in f1:  #可迭代的对象就可以进行for循环
    print(i)
print('--------------------1')

gen1 = f1.__iter__()   #对象调方法
print(gen1)  #<generator object Foo.__iter__.<locals>.<genexpr> at 0x0000025A781ABB10>
print(type(gen1))  #<class 'generator'>
print(gen1.__next__())  #0
print(gen1.__next__())  #1
print(gen1.__next__())  #2
# print(gen1.__next__())  #StopIteration
print('--------------------2')

gen1 = (i for i in range(3))   #生成器表达式--生成器-迭代器
print(gen1)  #<generator object <genexpr> at 0x0000020D11CDB5E8>
print(type(gen1))  #<class 'generator'>
for i in gen1:
    print(i)
print('--------------------3')

















