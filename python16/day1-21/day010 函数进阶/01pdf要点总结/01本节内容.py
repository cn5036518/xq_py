#!/usr/bin/env python
#-*- coding:utf-8 -*-

''''''
'''
本节主要内容
1、动态参数 *args **kwargs
    形参：*args将多个位置参数聚合打包成元组
          **kwargs将多个关键字参数聚合打包成字典
    实参：*li1将列表进行解包打散成多个位置参数
          **dic1将字典进行解包打散成多个关键字参数
    形参顺序：
        位置参数、
        动态参数：*args接收多个位置参数，聚合打包成元组
        默认值参数
        动态参数：**kwargs接收多个关键字参数，聚合打包成字典

2、名称空间-命名空间
    含义：python解释器开始执行的时候，就会开辟一个空间，每当遇到一个变量，就把变量名和值的对应关系记录下来，
          这个存放变量名字和值关系的内存空间就叫名称空间（也叫'命名空间'）
    分类：
        内置名称空间：存在python解释器为我们提供的名字，比如：list，dict，tuple，str，int等都是内置名称空间
        全局名称空间：函数外申明的变量会存放在全局名称空间
        局部名称空间：函数内申明的变量会存在在局部名称空间
    加载顺序：内置名称空间>全局名称空间>局部名称空间（函数执行的时候）
    取值顺序：局部名称空间>全局名称空间>内置名称空间

3、作用域
    含义：作用域就是作用范围
    分类：
        全局作用域：内置名称空间+全局名称空间
        局部作用域：局部名称空间
    查看：
        globals（）函数：查看全局作用域中的内容-（全局变量和全局作用域中的函数信息）
         locals（）函数：查看当前作用域中的内容-函数和变量
        （注意：是当前，而不是局部作用域，当位置在函数内，就查看局部作用域的内容；
                当位置在函数外，就是查看全局作用域的内容。取决于local()函数所在的位置）

4、函数的嵌套
    关键字：
        global：在函数内(局部)，引入全局变量
        nonlocal:在函数内（局部），调用父级命名空间中的变量
        注意点：不管是global还是nonlocal关键字，变量申明和变量赋值都需要分别2行写才行，写在一行会报错
            例子：global a
                  a =20 #是正确的
                  global a = 20 #会报错
'''

#1 位置参数
def eat(quality_food,junk_food):
    print('我要吃',quality_food,junk_food)
eat('apple','cherry')  #我要吃 apple cherry
print('-------------1 位置参数')

#一、形参-动态接收位置参数*args
#2 动态参数-形参 动态接收位置参数 形参一个星*
def eat2(*food): #形参的星号* 将接收到的多个参数，聚合打包成元组，接收到的是一个元组
    print('我要吃',food)
eat2('apple','orange')  #我要吃 ('apple', 'orange')   #接收到的是一个元组
print('-------------2 动态参数-接收多个位置参数 形参一个星*')

#3 动态参数-实参 实参一个星*
def eat3(*food): #形参一个星* 聚合打包多个位置参数成一个元组
    print('我要吃',food)
li1 = ['apple','banana']
eat3(*li1)  #我要吃 ('apple', 'banana')  #实参一个星，将可迭代类型（列表、字符串等）解包打散成多个位置元素
print('-------------3 动态参数-接收多个位置参数 实参一个星*')

#4动态参数的位置  必须在位置参数后面    形参顺序：位置参数、动态参数*args
# 因为动态参数如果在位置参数前面，位置参数就永远无法接收到参数
def eat4(a,b,*food):
    print('我要吃',a,b,food)
a1 = 'cherry'
b1 = 'banana'
li1=['apple','orange']
eat4(a1,b1,*li1)  #我要吃 cherry banana ('apple', 'orange')
print('-------------4 动态参数 形参顺序：位置参数必须在动态参数*args前面')

def eat5(*food,a,b):   #错误的
    print('我要吃',a,b,food)
# eat5('apple','orange','cherry')  #会报错
# TypeError: eat5() missing 2 required keyword-only arguments: 'a' and 'b'
print('-------------5 动态参数 形参顺序：位置参数如果在动态参数*args后面，就会报错')

def eat6(*food,a,b):   #形参顺序：位置参数、动态参数*args、默认值参数、动态参数**kwargs
    print('我要吃',food,a,b)  #我要吃 ('apple', 'orange') cherry banana
eat6('apple','orange',a='cherry',b='banana')
print('-------------6 动态参数+关键字参数')

def eat7(a,b,c='娃哈哈',*food):  #默认值参数在动态参数*args之前
    print('我要吃',a,b,c,food)
eat7('apple','orange')  #我要吃 apple orange 娃哈哈 () 默认值参数生效，形参*food传入空元组()
eat7('apple','orange','cherry') #我要吃 apple orange cherry () 默认值参数不生效，形参*food传入空元组()
eat7('apple','orange','cherry','banana') #我要吃 apple orange cherry ('banana',) 默认值参数不生效，形参*food传入元组('banana',)
eat7('apple','orange','cherry','banana','peer') #我要吃 apple orange cherry ('banana', 'peer')
# 默认值参数不生效，形参*food传入元组('banana', 'peer')
# 综上，只有第一种情况，默认值参数是生效的，其余3种默认值参数都不生效，形参顺序 所以默认值参数要放在动态参数*args之后
print('-------------7 位置参数+默认值参数+动态参数*args 默认值参数在动态参数*之前--不推荐')

def eat8(a,b,*food,c='娃哈哈'):  #默认值参数必须在动态参数*args之后  形参顺序： 位置参数、动态参数*args、默认值参数
    print('我要吃',a,b,food,c)
eat8('apple','orange')  #我要吃 apple orange () 娃哈哈 默认值参数生效，形参*food传入空元组()
eat8('apple','orange','cherry') #我要吃 apple orange ('cherry',) 娃哈哈 默认值参数生效，形参*food传入元组 ('cherry',)
eat8('apple','orange','cherry','banana') #我要吃 apple orange ('cherry', 'banana') 娃哈哈
# 默认值参数生效，形参*food传入元组('cherry', 'banana')
eat8('apple','orange','cherry','banana','peer')  #我要吃 apple orange ('cherry', 'banana', 'peer') 娃哈哈
# 默认值参数生效，形参*food传入元组('cherry', 'banana', 'peer')
print('-------------8 形参顺序 位置参数+动态参数*args+默认值参数 默认值参数必须在动态参数*args之后--推荐')

#二、形参-动态接收关键字参数**kwargs
def func(**kwargs): #形参 **kwargs将多个关键字参数掘和打包成字典
    print(kwargs)  #{'b': 2, 'a': 1}
func(a=1,b=2)  #实参 多个关键字参数
print('-------------2-1 形参 动态参数**kwargs接收多个关键字参数 聚合打包成字典')
#形参-位置参数必须放在关键字参数前面，否则报错
#形参顺序：
# 位置参数、--顺序1
# 动态参数*args（接收多个位置参数，聚合打包成元组）、--顺序2
# 默认值参数、--顺序3
# 动态参数**kwargs（接收多个关键字参数、打包成字典）--顺序4

def func2(**kwargs): #形参 **kwargs将多个关键字参数聚合打包成字典
    print(kwargs)  #{'b': 2, 'a': 1}
dic1 = {'a':1,'b':2}
func2(**dic1)  #实参 **kwargs 将字典的元素-键值对进行解包打散成 多个关键字参数
print('-------------2-2 形参 动态参数**kwargs接收多个关键字参数 聚合打包成字典')

#三、形参-动态接收任何参数（多个位置参数或者多个关键字参数及其组合）*args **kwargs
def func3(*args,**kwargs): #形参*args将多个位置参数聚合打包成元组，形参-**kwargs将多个关键字参数聚合打包成字典
    print(args,kwargs)  #(1, 2) {'name': 'jack', 'age': 18}
li1 = [1,2]
dic1 ={'name':'jack','age':18}
func3(*li1,**dic1) #实参-*args将列表进行解包打散，成多个位置参数；实参-**kwargs将字典进行解包打散成多个关键字参数
func3(3,4,a=5,b=6) #(3, 4) {'a': 5, 'b': 6}
print('-------------3-1 形参 动态参数*args,**kwargs接收任何参数--多个位置参数或者多个关键字参数及其组合')

#函数的注释
def eat(food,drink):
    '''
    这里是函数的注释，先写一下这个函数是干什么的
    :param food：参数food是什么意思
    :param drink：参数drink是什么意思
    :return:返回的是什么
    '''
    print(food,drink)
    return(food,drink)

#四 查看全局作用域和局部作用域中的内容
a =10
def func():
    a= 10
    b= 20
    def abc():
        print('哈哈')
    print(a,b) #打印局部变量
    print(globals()) #打印全局作用域中的内容（全局变量和全局作用域中的函数信息）
    #{'__file__': 'D:/Program/JetBrains/PycharmProjects/xq_py/全栈16/day010 函数进阶/01pdf要点总结/01本节内容.py',
    # 'a1': 'cherry', 'func3': <function func3 at 0x00000000026B2488>,
    #  'func': <function func at 0x00000000020A6730>, 'b1': 'banana', 'eat': <function eat at 0x00000000026B2510>,
    # '__cached__': None, 'a': 10, 'li1': [1, 2], '__builtins__': <module 'builtins' (built-in)>,
    #  'eat8': <function eat8 at 0x00000000026B22F0>, 'eat5': <function eat5 at 0x00000000026B2158>,
    # 'eat4': <function eat4 at 0x00000000026B20D0>, 'func2': <function func2 at 0x00000000026B2400>,
    #  'eat6': <function eat6 at 0x00000000026B21E0>, '__package__': None, '__name__': '__main__',
    # 'eat3': <function eat3 at 0x00000000026A9D08>, 'eat2': <function eat2 at 0x00000000026A9C80>,
    # 'dic1': {'age': 18, 'name': 'jack'},
    # '__loader__': <_frozen_importlib.SourceFileLoader object at 0x000000000216B9B0>, '__doc__': '',
    # 'eat7': <function eat7 at 0x00000000026B2268>}
    print(locals()) #{'abc': <function func.<locals>.abc at 0x00000000026B2378>, 'b': 20, 'a': 10}
    #打印局部作用域中的内容（局部变量和局部作用域中的函数信息）
func() #10 20
print(locals()) #注意点：当函数的位置在全局作用域时，就打印全局作用域中的变量和函数信息
print('-------------4-1 查看全局作用域和局部作用域中的内容')

#五 函数的嵌套
def fun1():
    print(111) #2-顺序2
def fun2():
    print(222) #1-顺序1
    fun1()
fun2()
print(111) #3-顺序3
# 222
# 111
# 111
print('--------------5-1 函数嵌套')

def fun2():
    print(222)  #顺序2
    def fun3():
        print(666)  #顺序4
    print(444)  #顺序3
    fun3()
    print(888)  #顺序5
print(33)  #顺序1
fun2()
print(555)  #顺序6
# 33
# 222
# 444
# 666
# 888
# 555
print('--------------5-2 函数嵌套')

#六 关键字global和nonlocal
a =100
def func():
    global a  #关键字global表示不再是局部创建变量了，而是直接引用了全局变量a
    # global a = 20  #注意点：这里会报错，应该分成2行来写
    a =20  #给全局变量赋值
    print(a) #20
func()
print(a) #20  #全局变量的值被修改了
print('--------------6-1 global关键字 在函数内引用全局变量')

li1 = []
def func():
    li1.append('jack')
    print(li1)
func()  #['jack']
print(li1)  #['jack']

#nolocal表示在局部作用域中，直接调用父级命名空间中的变量
a = 10
def func1():
    a = 20  #30
    def func2():
        nonlocal a #调用父级命名空间中的变量
        #如果加了nonlocal a 打印的就是30 30
        #如果不加nonlocal a 打印的就是30 20
        # nonlocal a =30  #注意点：写在一行会报错，nonlocal变量的申明和赋值需要分开2行来写
        a =30
        print(a)  #30
    func2()
    print(a)  #30
func1()
# 30
# 30
print('--------------6-2 nonlocal关键字 在局部作用域中，直接调用父级命名空间中的变量')

a = 1
def fun_1():
    a = 2   #改成了3
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)  #顺序4 打印4
        print(a)  #顺序3 打印3
        fun_3()
        print(a)  #顺序5 打印3
    print(a)  #顺序2 打印2
    fun_2()
    print(a)  # 顺序6 打印3
print(a)  #顺序1 打印1
fun_1()
print(a)  # 顺序7 打印1
# 1
# 2
# 3
# 4
# 3
# 3
# 1
print('--------------6-3 nonlocal关键字 多层函数嵌套')








