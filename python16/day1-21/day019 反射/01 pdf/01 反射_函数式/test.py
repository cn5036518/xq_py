#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/2/9 15:25
#@author:wangtongpei
#@email: cn5036520@163.com

import master
from types import FunctionType

# master.eat()  #hava a breakfast

def reflect(arg):
    if hasattr(master,arg): #参数1是模块py文件名字  参数2要查找的字符串（函数名）
        # 1判断模块py文件中是否包含参数2
        result = getattr(master,arg) #参数1是模块py文件名字  参数2要查找的字符串（函数名）
        # 2从参数1中获取参数2的内存地址
        if callable(result):  #和下面行是等效的
        # if isinstance(result,FunctionType):
            result() #调函数 #hava a breakfast
        else:
            print('不是函数，无法调用')
            print(result)
    else:
        print('对不起，你要查找的内容不存在，请重新输入你要查找的内容')

reflect('eat')












