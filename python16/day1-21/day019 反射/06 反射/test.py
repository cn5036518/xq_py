#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/6 9:06
#@author:wangtongpei
#@email: cn5036520@163.com

import master   #导入模块，同目录的文件
from master import Person

# delattr(master,'play')  #参数1可以是类、模块py文件

p1 = Person('tom')
# delattr(Person,'eat')  #2从类中删除函数eat

p1.eat()  #AttributeError: 'Person' object has no attribute 'eat
# master.play()  #AttributeError: module 'master' has no attribute 'play'

master.eat() #调用其他文件的函数

while 1:
    '''
    eat
    drink
    play
    '''
    val = input('请输入：')

    # if val == 'eat':
    #     # master.val()  #AttributeError: module 'master' has no attribute 'val'
    #     master.eat()
    if hasattr(master,val): #参数1是文件名（模块名） 参数2是函数名或者变量名
        #1 判断参数1中是否有参数2
        attr1 = getattr(master,val)   #参数1是文件名（模块名） 参数2是函数名或者变量名
        # 变量名用attr更合适  attr包含func和val（属性包含函数和变量名）
        #2从参数1中，查找参数2，找到参数2了，把参数2的地址存在变量func1中
        if callable(attr1):  #3 判断参数是否可以被调用（可以的话，是函数；不可以，就是变量）
            attr1()   #4 可以被调用，是函数，加小括号，调用
        else: #5 不可以被调用，不是函数，是变量，直接打印变量的值
            print(attr1)  #打印变量的值
    else:
        print('你输入的函数或者变量在文件中没有找到，请检查你的输入是否正确')











