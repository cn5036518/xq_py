#!/usr/bin/env python
#-*- coding:utf-8 -*-

''''''
'''
函数
1、函数的概念
    函数是功能或者动作的封装

2、函数的定义
    def 函数名(形参列表):
        函数体(return)

    函数名是变量，变量名的命名规范
    1、由数字、字母、下划线组成
    2、不能是数字开头
    3、不能使用关键字
    4、不要使用中文
    5、不要太长
    6、名字要有意义--一看就知道变量代表的意思
    7、建议使用驼峰或者下划线
    8、严格区分大小写

    函数的调用
    ret = 函数名(实参列表)
    这里ret用来接收函数的返回值

3、返回值--return
    1、返回None
        return后面是空白
        return不写
    2、返回一个值
        return 值
    3、返回多个值
        return 值,值,值  结构是元组，可以结构
    4、作用：函数通过return把返回值返回给函数的调用方
    5、函数终止：函数内，return下面的代码是不执行的，函数的运行终止
       （函数的return类似于for循环中的break）

4、参数
    作用：不修改函数体的代码，通过传递参数来实现比如：不同的聊天工具
    定义：
        形参：函数定义中的变量就是形式参数,简称形参
        实参：函数调用中的具体值就是实际参数，简称实参
        传参：函数调用过程中，把实参的值赋值给形参的过程，就是传参
    分类
        实参分类：
            位置参数-最常见
                按照形参的位置，来传递实参
            关键字参数
                按照形参的参数名字，来传递实参
                应用场景：参数比较多，记不住参数的位置顺序的时候
            混合参数
                位置参数必须放在前面，关键字关键字参数必须放在后面（否则报错）
        形参分类：
            位置参数-最常见
                按照形参的位置
            默认参数
                默认参数必须放在最后
                如果实参传值给了默认参数，默认参数就被覆盖
                如果实参没有传值得默认参数，就取默认参数

'''













