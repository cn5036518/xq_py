#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 11:45
#@author:wangtongpei

''''''
'''
1、send（）和__next__()的区别
send（）和__next__()向下取值的功能是一样的，send（）另外还能给上一个yield传值（传值的功能，__next__()是没有的）

'''

def func1():
    print("康师傅")
    a = yield '娃哈哈'
    print("统一100",a)
    b = yield '娃哈哈2'
    print("好劲道", b)
ret = func1()  #生产一个生成器对象
print(ret.__next__())
print(ret.__next__())
# 康师傅
# 娃哈哈
# 统一100 None  #因为第一次yield后，在第二次yield前，a的值是None
# 娃哈哈2
print('-----------------1 __next__()方法')

def func2():
    print("康师傅")
    a = yield '娃哈哈'
    print("统一100",a)
    b = yield '娃哈哈2'
    print("好劲道", b)
    c = yield '娃哈哈3'
    print("老北京", c)
ret = func2()  #生产一个生成器对象
print(ret.__next__())  #生成器对象产生后，第一次取值必须是__next__()，而不能是send()
# print(ret.send('start1'))  #报错  TypeError: can't send non-None value to a just-started generator
print(ret.send('刘德华'))  #关键点  send()可以给上一次yield(第一次yield)进行传值
print(ret.send('刘德华2'))  #关键点  send()可以给上一次yield(第一次yield)进行传值
# print(ret.send('刘德华3'))  # 报错  StopIteration
# 康师傅
# 娃哈哈
# 统一100 刘德华  #因为第一次yield后，在第二次yield前，a的值被send（'刘德华'）传值了
# 娃哈哈2
#好劲道 刘德华2  #因为第2次yield后，在第3次yield前，b的值被send（'刘德华2'）传值了
print('-----------------2 send()方法')

'''
小结
1、send（）和__next__()的区别
send（）和__next__()向下取值的功能是一样的，send（）另外还能给上一个yield传值（传值的功能，__next__()是没有的）

1、send()不能写在生成器产生后，第一次取值，第一次取值必须是用__next__()
2、生成器函数如果包含3个yield的话，最多允许2个send（），第三个send()会报错-StopIteration

'''

def func():
    yield '马云'
    yield '马化腾'
    yield '李彦宏'
    yield '刘强东'
gen = func()  #生产一个生成器对象,生成器的本质是迭代器,迭代器是可以迭代类型的（可迭代的）--Iterable，即可以for循环遍历

print('__iter__' in dir(gen))  #True 判断对象是否是迭代器的标准
for i in gen:
    print(i)
# 马云
# 马化腾
# 李彦宏
# 刘强东
print('-----------------3 生成器可以for循环，遍历取值')

def func():
    yield '马云'
    yield '马化腾'
    yield '李彦宏'
    yield '刘强东'
gen = func()   #生产一个生成器对象
li1  = list(gen) #将生成器对象转换成列表类型  应用场景：主要用于测试-可以直接看到结果
#注意：如果gen已经for循环遍历取值结束了，再转换成列表，列表是空的，因为生产器中不能再取值了
print(li1)  #['马云', '马化腾', '李彦宏', '刘强东']







