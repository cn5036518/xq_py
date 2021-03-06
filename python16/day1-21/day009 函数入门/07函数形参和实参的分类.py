#!/usr/bin/env python
#-*- coding:utf-8 -*-

#先写参数的分类，然后总结函数-今天所学

'''
实参的分类
1、位置参数：按照位置的顺序，给形参赋值--最常见
2、关键字参数：按照形参的名字，给形参赋值
3、混合参数：位置参数必须放在前面，关键字参数必须放在后面（否则，报错）

形参的分类
1、位置参数：按照形参位置的顺序，来定义形参，定义函数
2、默认参数：位置参数必须放在前面，默认参数必须放在后面
    不传递实参的时候，形参-默认参数起作用，取默认值
    传递实参的时候，形参-默认参数不起作用，默认值会被传递的实参覆盖
'''

#一、定义函数
def eat(good_food,no_good_food,drink): #1
    print("我要吃",good_food,no_good_food,drink)

#二、调用函数
#1 实参-位置参数   ---最常见
eat('大米饭','薯条','可乐')  #位置参数，最常见，按照位置的顺序，给形参赋值
#我要吃 大米饭 薯条 可乐

#2 实参-关键字参数
eat(drink='可乐',no_good_food='薯条',good_food='大米饭')
#实参-关键字参数，按照形参的名字，给形参赋值（实参-关键字参数，key不考虑顺序）
# 我要吃 大米饭 薯条 可乐

#3 实参-混合参数
#实参-混合参数：就是位置参数和关键字参数混合使用
eat('大米饭','薯条',drink='芬达')
#前面2个参数是位置参数，后面1个参数是关键字参数
#位置参数必须在前面，关键字参数必须在后面（否则，就会报错）
#我要吃 大米饭 薯条 芬达

#例子
f = open('疙瘩汤.txt',mode='r',encoding='utf-8')
#这个就是实参-混合参数  第一个参数是位置参数，后面2个参数是关键字参数

'''
实参的分类
1、位置参数：按照位置的顺序，给形参赋值--最常见
2、关键字参数：按照形参的名字，给形参赋值--打开文件用到了mode='r',encoding='utf-8' 就是
3、混合参数：位置参数必须放在前面，关键字参数必须放在后面（否则，报错）
'''

'''
形参的分类
1、位置参数：按照位置的顺序，定义形参，定义函数--最常见
2、默认参数：
    规则：位置参数必须放在前面，默认参数必须放在最后（否则，报错）
          定义形参-默认参数后，传递实参的时候，可以不传值给形参-默认参数，此时，就取形参-默认参数的值
                              传递实参的时候，如果传了值给形参-默认参数，此时，形参-默认参数的值就会被覆盖
'''

#一、定义函数
#1形参-位置参数
def register(name,age,sex):
    print(name,age,sex)
#2形参-默认参数
def register2(name,age,sex='男'): #这里最后一个形参就是默认参数，前面2个形参是位置参数
    print(name,age,sex)

#二、调用函数
register('jack',18,'男')  #jack 18 男
register2('tom',19)  #tom 19 男
#这里只传递了前2个实参，第三个实参没有传递，取形参-默认参数的值-男
register2('lucy',17,'女')  #lucy 17 女
#这里第三个实参传递了-女，形参-默认参数就被覆盖了，取值变成-女



