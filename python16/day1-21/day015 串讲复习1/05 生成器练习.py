#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/21 6:11
#@author:wangtongpei
#@email: cn5036520@163.com

#1 生成器函数
def func():  #1 定义生成器函数
    li1 = ['jack','tom','bob']
    for i in li1:
        yield i
gen1 = func()  # 2 调用生成器函数，产生生成器generator
print(gen1)  #<generator object func at 0x0000008644E74D48>

print(next(gen1))  #jack  3生成器的取值（单次取值） next() __next__()
print(gen1.__next__())  #tom
print(gen1.__next__())  #bob
# print(gen1.__next__())  #报错StopIteration
print('------------------------1  生成器单个取值 next')

#2 生成器的本质是迭代器，支持for循环
def func(li):  #1 定义生成器函数
    for i in li:
        yield i
li1 = ['jack', 'tom', 'bob']
gen1 = func(li1)  #把iterable转成生成器
for i in gen1:
    print(i)
print('------------------------2  生成器遍历循环 for')

#3 把可迭代对象-iterable转换成生成器-generator
def func3(li):
    yield from li #实现把iterable转换成generator
li1 = [1,2,3]
gen3 = func3(li1)  #把iterable转换成生成器-generator
print(gen3)  #<generator object func3 at 0x000000E53FF24CC8>
for i in gen3:
    print(i)
print('------------------------3  把可迭代对象-iterable转换成生成器-generator')

'''
小结：
def func(li):
    for i in li:
        yield i
def func3(li):
    yield from li
1、上述2个函数的函数体是等效的
'''

gen1 = (i for i in range(3))  #0 1 2
print(gen1)  #<generator object <genexpr> at 0x000000B175FB4DC8>
print(next(gen1))  #0
for i in gen1:
    print(i)
print('------------------------4 生成器表达式')

#练习1
def add(a, b):
    return a + b
def test():
    for r_i in range(4):
        yield r_i
g = test()  #产生生成器  0 1 2 3
g = (add(6, i) for i in g)  #生成器表达式
print(g)  #<generator object <genexpr> at 0x000000C26A954E48>
print(list(g))  #[6, 7, 8, 9]  #生成器转换成列表
print('--------------1')

#练习2
def num():
    return [lambda x:x+i for i in range(4)]
# print([i(2) for i in num()])
print([j(2) for j in num()])   #这里i换成j 和上面函数的i进行区分,方便理解（去掉混淆）
#[5, 5, 5, 5]

#1 第一步：将匿名函数转换成普通函数
def num():
    for i in range(4): # 0 1 2 3
        # print(i)   #这里分别是 0 1 2 3  类比：内层函数定义一次，就调用一次
    # print(i)  #这里i是3  #类比：内层函数4个全部定义完了，最后调用（4个函数共用一个i，最后就是i=3）
        def inner(x):
            return x+i  #闭包
        #外层函数中的变量，内层函数中用到了，就是闭包
print('--------------2-1')

#2分析打印结果
# print([j(2) for j in num()])
#列表推导式
#第一步  for j in num()
#这里num()是外层函数，里面包含4个内层函数，所有循环遍历后，就是4个内层函数

#第二步  j(2)
# j(2)表示 4个内层函数的参数都是2，  即x是2
# 列表推导式结果是4个内层函数的返回值构成的列表（列表的元素个数是4个）
# 这里的i依次取值是0,1,2，3   [2,3,4,5]
# 关键点；这里的i每次都是3  [5,5,5,5]  why
#        原因是：4个内层函数的都是共用一个i，这4个内层函数只是定义了，没有被执行，全部定义完了，才执行
#   所以最后的i是3（如果是定义一个内层函数，就执行一个，就是[2,3,4,5]，这里是全部定义完了，就是[5,5,5,5]）






















