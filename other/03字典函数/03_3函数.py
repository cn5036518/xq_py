#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
1、函数的定义（函数是什么）what
    函数是实现特定功能而封装起来的一组语句块，可以被用户调用

2、函数的分类
    1、自定义函数（用户写的）
    2、自带函数 （lib里的，系统自带的）

3、函数的好处（为什么要使用函数）why
    1、降低编程难度：将大问题拆成若干小问题
    2、代码重用：可以被多次重复调用

4、函数的定义（语法格式）
def 函数名字(参数):  #这里的参数是形参
    函数体（代码块）
    return 语句 #  不带表达式的return相当于返回None

5、函数的调用
函数名字()
函数名字（实参）

"""

#1 定义函数，调用函数-传入实参
def print_me(a):  #函数名最好以下划线分割  这里的a是形参
    print(a)
    return

print_me("hello world")  #括号内是实参
print_me("hello world2")
result1 = print_me("hello world3")
print(result1) #None

#2 函数传参-普通类型参数
"""
所有参数在python里都是按引用传递。----区分于按值传递（先记下来what,python的特点）
一句话：要变都变
"""
def change_me(mylist):
    mylist.append([1,2,3])
    print("函数内取值:",mylist)  #函数内取值 [1, 2, 3, [1, 2, 3]]
    return  #默认返回None

#调用函数
mylist=[1,2,3]
change_me(mylist)
print("函数外取值:",mylist) #函数外取值 [1, 2, 3, [1, 2, 3]]
#列表作为参数，按引用传递，要变都变（先记下来what,python的特点）
#列表作为参数，传递到函数，列表在函数内的取值变化了，列表在函数外的取值也跟着变化--函数内外，要变都变
#列表作为参数，函数内外，要变都变

#3 函数默认参数，python比较灵活
def print_me(name,age=18):  #默认参数age=18
    # print("名字是%s,年龄是%s"%(name,age))   #格式化输出
    print("名字是：",name)
    print("年龄是：",age)
    return

#调用函数
print_me(name="jack",age=19)  #19覆盖18，覆盖默认参数
print_me(age=29,name="jack")  #实际参数顺序不一样的情况，也可以--python比较灵活
print_me(name="jack")  #参数1传入，参数2采用默认参数age=18--python比较灵活

#默认参数的类比：功能测试的时候，网上银行这个，查一个范围内转账明细，默认时间是当天或者一周内

#4 不定长参数  *args    扩展：**kwargs
def print_me(arg1,*args):  #  *号是必须的
    print("arg1是",arg1)
    print("args是",args)  #args是 (22, 33) #传入的是元组
    for i in args:  #  *号不能写，写变量名args即可
        print(i)

#调用函数
print_me(11)
print("=======================")
print_me(11,22,33)  #实参11通过形参1--arg1传入，后面的实参22,33通过形参2--*args一起传入
print("=======================")

#5 匿名函数 lambda函数，了解即可
"""
1、lambda函数只是一个表达式，而不是一个代码块，函数体比def简单很多。仅仅能在lambda写简单的逻辑-比如加减运算
2、语法
    lambda [arg1[,arg2,...argn]]:expression
"""

sum1=lambda arg1,arg2:arg1+arg2  #这里的sum1是匿名函数的名字
sum2=lambda :3  #sum2匿名函数可以不传参数

#调用sum匿名函数
print(sum1(10,20))  #30
print(sum1(11,21))  #32
print(sum2())  #3  匿名函数可以不传参数
print("=======================")

#6 return返回
"""
return语句[表达式]
rerurn后面空白或者不写return都是默认返回None
"""

def sum1(arg1,arg2):#1正常return
    total=arg1+arg2
    return total

result1= sum1(10,20)
print(result1) #30

def sum1(arg1,arg2):#2 不写return，默认返回None
    total=arg1+arg2

result1= sum1(10,20)
print(result1) #None

def sum1(arg1,arg2):#3 return后面空白，默认返回None
    total=arg1+arg2
    return

result1= sum1(10,20)
print(result1) #None

#7 全局变量和局部变量
"""
1、定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
2、局部变量只能在其被声明的函数内部访问-使用，而全局变量可以在整个程序范围内访问-使用。
"""

total=0  #全局变量-函数外
def sum1(arg1,arg2):#3 return后面空白，默认返回None
    total=arg1+arg2 #局部变量-函数内
    print("函数内的total值是：",total)  #30 这里的total是局部变量
    return total

# total=sum1(10,20)  #total是30，覆盖之前的total=0
sum1(10,20)
print("函数外的total值是：",total) #0   这里的total是全局变量














