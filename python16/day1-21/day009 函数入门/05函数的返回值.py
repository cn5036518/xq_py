#!/usr/bin/env python
#-*- coding:utf-8 -*-

def yue():  #1定义函数
    print('打开手机')
    print('打开陌陌')
    print('找到心仪的对象')
    # return  #如果这里返回，那么下面的代码是不执行的
    print('出来吃吃饭')
    print('跳跳广场舞')
    # return '小姐姐'   #1返回一个值
    # return '小姐姐','小护士','广场舞大妈'  #2返回多个值（元组）   和下面等效
    # return ('小姐姐','小护士','广场舞大妈')
    return   #返回的是None  和没有return但是等效的

ret = yue()  #这里的ret变量用于接收函数的返回值
print(ret)  #None

'''
函数的返回值
1、一个返回值：当return一个值的时候
2、多个返回值：当return多个值的时候，用变量接收后，打印出来，是一个元组 ('小姐姐', '小护士', '广场舞大妈')
3、没有返回值：函数体没有return的时候，默认返回的是None
4、没有返回值：函数体有return，但是return后面是空白的时候，默认返回的是None
5、终止函数运行：在调用函数的时候，一旦遇到return，就会终止函数的运行，return下面的代码行是不运行的
    函数里的return就类似于：for循环中的break
'''
#例子
li1 = []
ret2 = li1.append('jack')
print(li1)  #['jack']
print(ret2)  #None  #因为函数append是没有返回值的，所以会打印出None











