#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
①，return的作用。
②，传参的几种方法，每个都简单写一个代码。
如，实参，按位置传参。
def func(x,y):
Pass
func(‘a’,’b’)
'''

'''
return的作用
1、将函数的输出，返回给函数的调用方
2、函数内，return下面的代码是不执行的，终止函数运行
3、return可以返回一个值
4、return也可以返回多个值，结构是元组（可以解构）
5、return后面空白或者return不写，默认会返回None
'''

'''
实参的分类：
1、位置--最常见
    stu_info('jack',18)  #和下面的形参-位置参数 对应

2、关键字
    stu_info(name='tom',age=19)  #这里把形参的参数名字写出来了，就可以不考虑顺序了
    stu_info(age=17,name='bob')
    应用场景：参数比较多，记不住参数先后顺序的时候

3、混合参数：
    位置参数必须在前面，关键字参数必须放最后（否则报错）
    例子：
    f = open('001.txt',mode='w',encoding='utf-8')
    参数1就是位置参数，参数2和参数3就是关键字参数，整个就是混合参数

形参的分类：
1、位置--最常见
    例子：
    def stu_info(name,age):
        pass
2、默认参数
    默认参数必须放在最后（否则报错），实参没有传值给默认参数，就取默认参数
    实参如果传值给了默认参数，默认参数就会被覆盖
    例子：
    def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True):
        pass
    这里参数2 mode就是默认参数，如果实参不传值，默认就取只读'r'
    如果实参传了值写'w'，默认参数就被覆盖，取写'w'
3、动态参数--下节分解
    *arg,**kwargs
'''













