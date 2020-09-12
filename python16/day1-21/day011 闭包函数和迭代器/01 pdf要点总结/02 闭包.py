#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 6:13
#@author:wangtongpei

''''''
'''
1、闭包的概念
    内层函数，对外层函数变量的引用，就叫闭包
    子级函数，对其父级函数的变量的引用（访问、修改、返回），就叫闭包

    1、内层函数（或者子级函数）是闭包函数（简称-闭包）
    2、外层函数（或者父级函数）不是闭包函数

2、判断函数是否是闭包函数的标准
    执行函数名.__closure__后，返回是None，就不是闭包函数.__closure__是属性名，而不是函数或者方法
    返回带有cell，就是闭包函数

3、闭包的特点
    1、闭包函数中，父级函数的变量，常驻内存（全局变量的优点）
        因为：如果不常驻内存，从外面访问子集函数，就会报错
    2、保护父级函数的变量（局部变量的优点）
       别的同学无法修改你定义的父级函数的变量值
       （别的同学无法随意修改，就是安全的）
    3、全局变量的优点：常驻内存，缺点：不安全（不管是谁，在函数内部的局部变量前加上global就可以修改全局变量）
       局部变量的优点：安全（只能函数定义者可以修改）  缺点：无法常驻内存

4、闭包的写法
5、闭包的应用
    爬虫：让比较耗时的网络连接只进行一次，就把网页的内容保存在变量中，常驻内存
'''

#4闭包的写法
def outer():
    a = 10
    def inner():
        print(a) #内层函数，对外层函数变量（不是全局变量）的引用（访问、修改、返回），就叫闭包
        return a
    return inner
ret = outer()
print(ret)  #<function outer.<locals>.inner at 0x00000000026D9D08>
#返回的是内层函数的内存地址
ret()  #10  调用内存函数
print('---------------------1 闭包的写法')

#2判断函数是否是闭包函数的标准
print(ret.__closure__)   #这里的ret是内层函数inner的内存地址  说明inner函数是闭包
#(<cell at 0x00000000006115B8: int object at 0x000000001E39D8A0>,)
# 这里的 int object  at 0x000000001E39D8A0 表示被保护变量a的内存地址

# print(ret().__closure__) #报错 说明inner()不是闭包
# AttributeError: 'int' object has no attribute '__closure__'

print(outer.__closure__)  #None  说明outer函数不是闭包
print(outer().__closure__)  #(<cell at 0x000000000203A6A8: int object at 0x000000001E39D8A0>,)
#说明outer()是闭包，即inner函数是闭包
print('---------------------4 判断函数是否是闭包函数的标准')
'''
小结：
1、闭包的本质是函数，闭包函数（简称-闭包）
2、内层函数（或者子级函数）是闭包函数（简称-闭包）
    因为：内存函数名.__closure__ 返回的值带有cell
3、外层函数（或者父级函数）不是闭包函数（简称-闭包）
    原因：外层函数名.__closure__ 返回的值是None
'''

#5闭包的应用--爬虫
#好处：通过闭包函数，把耗时的网络连接只进行一次（调用外层函数），然后把网页内容爬取后，常驻内存，下次方便使用（调用内层函数）
from urllib.request import urlopen

def outer():
    url1 = 'https://www.baidu.com'
    content = urlopen(url1).read()
    def inner(): #闭包函数
        print(content)  #闭包  这里的content会常驻内存
        return content
    return inner

ret = outer()  #调用外层函数，此时第一次需要网络连接，加载网页内容，后面就不需要内次都网络连接了
#因为网络连接后的网页内容，会常驻内存
print(ret) #返回inner的内存地址
ret()  #第一次获取内容，不需要网络连接，只需要访问content（已经常驻内存了）
ret()  #第二次获取内容，不需要网络连接，只需要访问content（已经常驻内存了）
print('-------------------5 闭包的应用--爬虫')

#6多层嵌套的写法
def outer():
    a = 10
    def func2():
        print(a)
        def func3():
            print(a)
        return func3
    return func2
ret = outer()  #执行外层函数outer，返回的是func2的内存地址
ret()  #执行func2函数，返回的是func3的内存地址
ret()() #执行func3函数
print('-------------------6 多层嵌套的写法')

