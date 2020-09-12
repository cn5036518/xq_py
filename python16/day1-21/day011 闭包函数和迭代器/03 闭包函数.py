#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/5 11:29
#@author:wangtongpei

#1在外面，是不能访问到局部变量的
def func1():
    a = 10
    print(a)  #10  局部变量
func1()  #10  局部变量
# print(a)  #报错 NameError: name 'a' is not defined
print('-----------------1')

#2 全局变量和局部变量名字相同，但是是分开的
a = 20
def func2():
    a = 10
    print(a) #10   局部变量
func2()  #10   局部变量
print(a)  #20  全局变量
print('-----------------2')

#2 全局变量和局部变量名字相同，但是是分开的
a = 20
def func3():
    global a  #局部变量升级成了全局变量，可以访问和修改全局变量
    a = 10
    print(a) #10   局部变量
func3()  #10   局部变量
print(a)  #10  全局变量被修改成了10
print('-----------------3')

'''
1、全局变量是不安全的，因为局部变量前面加上global后，就可以随便修改全局变量了
2、局部变量是安全的，只能在函数内修改，函数外是无法修改的，但是局部变量在外面是访问不到的
以上问题，闭包来解决
'''
#3 闭包的概念
# 父级函数的变量a，被其子函数用到了（访问或者修改），这个变量a就叫闭包
def outer():
    a = 11
    def inner():
        print(a)
    return inner

ret = outer()  #这里的ret就是inner函数的内存地址  <function outer.<locals>.inner at 0x0000000002712158>
ret()  #11
print(ret())  #None 因为inner函数没有return，默认返回None
print(ret.__closure__)  #(<cell at 0x0000000001F015B8: int object at 0x000000001E39D8C0>,)
# 这里的int object就是变量a  0x000000001E39D8C0就是变量a的内存地址
#  如果函数调__closure__属性后，有返回值（不是None），就表示是闭包
print(outer.__closure__)   #None
# 说明ret函数是闭包，而outer函数不是闭包
print('-----------------4')

'''
闭包的概念：父级函数的变量a，被其子函数用到了（访问或者修改、返回），含有变量a的函数就叫闭包函数（简称-闭包）
           --需要嵌套函数
首先，什么是闭包呢？
简单的理解就是一个内建函数，什么样的内建函数呢？
就是里面的函数会使用到外层函数中变量的这样一个内建函数。

注意点：
outer不是闭包函数
outer()才是闭包函数

闭包的特点：
1、闭包-父级函数的变量a会常驻内存（和全局变量一样常驻内存），
   原因是：如果变量a不是常驻内存，那么ret()会用到变量a，ret（）一执行就会报错
2、闭包-父级函数的变量a比较安全，因为只有我可以对a进行修改，别的同学是无法对闭包a进行修改的
   这样的好处是：闭包-父级函数的变量a会常驻内存-这个是全局变量的优点
                闭包-父级函数的变量a只能自己修改，别人无法修改--这个刻服了全局变量的缺点
                （全局变量是别人也能修改，不安全）

判断是否是闭包的标准：
print(函数名.__closure__)  如果有返回值，就是闭包，没有返回值，就不是闭包

闭包的应用
1、保护变量
2、常驻内存（爬虫，把网址上的东西存在内存）
'''

#1爬虫--不用闭包函数
from urllib.request import urlopen

def func():
    content = urlopen('http://m.xiaohuar.com/').read()
    #将网址的内容爬取到，存在变量content中
    print(content)
func()  #这里每次调用，都在请求网络
print('----------------------5-1')

#爬虫--用闭包函数
def outer2():
    content = urlopen('http://m.xiaohuar.com/').read()
    def inner():
        return content #父级函数的变量content在子级函数中用到了（访问、修改或者返回）
    #这里的content会常驻内存
    return inner
ret = outer2()  #inner函数的内存地址  这里是网络请求，然后把网络请求的结果存在内存
print(ret())  #闭包函数  这里是访问内存
print(ret())  #闭包函数  这里是访问内存
print('----------------------5-2')












