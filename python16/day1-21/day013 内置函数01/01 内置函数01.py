#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/8 8:22
#@author:wangtongpei

#python3.6.2 一共有 68个内置函数
''''''
'''
参看资料  https://www.processon.com/view/link/5b4ee15be4b0edb750de96ac#map  思维导图分类

1、python3.6.2 一共有 68个内置函数
2、分成6个大类
    1、反射相关-4个
    2、面向对象相关-9个

    3、作用域相关--2个
        1、globlas（）   #注意：最后是s，复数形式
           查看全局作用域中的全局变量的名字--返回的是字典

        2、locals()     #注意：最后是s，复数形式
           查看当前位置中变量的名字--返回的是字典
           1、当前位置是函数内，就是查看局部作用域中的局部变量的名字
           2、当前位置是函数外，就是查看全局作用域中的全局变量的名字（和globals()一样）
           取决于当前位置是函数内还是函数外

    4、迭代器、生成器相关-3个
        1、range()
            主要用于for循环，进行循环遍历

        2、iter() 和__iter__()
            001 __iter__()
            1、可迭代的：判断一个对象是否是可迭代类型的（可迭代的）--Iterable
               就看这个对象或者类的全部方法中是否包含__iter__()，包含就是可迭代的
               li1 = [1,2]
               print('__iter__' in dir(li1)) #True 就说明对象li1是可迭代的--Iterable
            2、可迭代的数据类型：str list tuple dict set open() range(3)
            3、迭代器：it1 = li1.__iter__() #这里it1就是迭代器--Iterator

            002 iter()   #内部执行依然用的是__iter__()
                li1 = [1,2]
                it1 = iter(li1)  #这里的it1就是迭代器--Iterator
                it1 = li1.__iter__()  #和上面等效

                def iter(args):
                    return args.__iter__()

            小结：
                it1 = iter(li1)  #这里的it1就是迭代器--Iterator 参数是可迭代对象
                it1 = li1.__iter__()

                写法
                迭代器1 = iter(可迭代对象)        #对象作为参数传入
                迭代器2 = 可迭代对象.__iter__()   #对象调方法

        3、next()和__next__()
            001 __next__()
            迭代器或者生成器向下取值，只能向下取值，不能后退
            1、迭代器向下取值
               li1 = [1,2]
               it1 = li1.__iter__()   #迭代器
               it1.__next__()   #取值一次
               next(li1)   #和上面等效
            2、生成器向下取值
                gen = (i for i in range(3))  #产生一个生成器
                gen.__next__() #取值一次
                next(li1)   #和上面等效

            002 next()  #内部执行依然用的是__next__()

            小结：
                迭代器对象.__next__()  #对象调方法
                next(迭代器对象)  #对象作为参数传入  和上面是等效的

                生成器对象.__next__()  #对象调方法
                next(生成器对象)  #对象作为参数传入  和上面是等效的


    5、其他-12个
        1、输入输出--2个
            input()
            print()

        2、内存相关--2个
            id() :输出对象的内存地址
            hash()

            数据结构--重点理解--及其重要--必须理解掌握
            1、列表（数组）：list(array)
                有索引号，有位置的一组数据
                优点：查询根据索引号，效率非常高
                缺点：删除一个元素或者新增一个元素，其他所有的元素都要移动位置，效率非常低

            2、链表：
                概念：由数据和后面的指针组成，指针指向下一个元素的位置，一个接一个
                类比：火车每一节车厢就是数据-装人，
                      车厢后面的连接处的车钩就是指针-指向下一节车厢
                优点：新增一个元素到指定位置，比如新增一个元素到位置2和位置3之间，
                        只需要把位置2后面的指针，指向新元素，然后把新元素的指针指向位置3即可完成；
                     删除一个指定位置的元素，比如删除位置4的元素，
                        只需要将位置3后面的指针指向位置5即可
                     上述不管是新增还是删除一个元素，都不需要向列表一个，整个列表其它元素的位置都要偏移
                     所以，新增或者删除的效率非常高
                缺点：查询的效率比较低
                      原因：要找到位置3的数据，需要找到位置2的指针，
                            找到位置2后，还需要找到位置1的指针
                            就是每次查询一个元素，都需要查询到这个元素的起点元素才行

            3、哈希表：hash（）
                概念:由列表和链表2部分组成
                    第一排是列表
                    第二排是列表的每个元素下面都连接着链表
                原理：哈希表在每次存储的时候，把对象（比如-alex）交给hash()算法计算出一个数值-哈希值，
                      根据这个数值，存储到对应的列表的索引号位置
                      比如：存储过程：   'alex'=5
                            'alex'这个变量经过hash()算法计算出的数值是5，那么就存储到索引号是5的位置（属于列表），
                            'alex'这个变量不是直接存放在索引号5这个位置，
                                    而是放在列表中索引号是5这个位置下面的链表的数据中
                            查询-取值过程：
                              下一次，取值或者查询、查找'alex'这个变量的时候，依然会根据对象交给hash()算法
                               计算出-哈希值（这里是5），然后直接取找5这个位置
                      备注：这里的5这个位置-或者索引号，就是'alex'这个变量在内存空间的内存地址--房间号

                优点：由于兼具列表和链表，所以新增、删除、查询的效率都非常高
                缺点：哈希表都比较的大，比如有100个索引号（内存编号）位置，只存储了10个数值，其余90个位置是空的，
                      就浪费了90%的空间
                      比较耗费空间--内存（就是以空间换时间）
                备注：空间换时间
                      空间上：浪费内存空间
                      时间上：快，效率高
                应用：字典的存储就是--哈希表
                      哈希表中列表存储的是字典的key，链表存储的是字典的value

                目前基本数据结构：列表（数组），链表，哈希表-dict（堆栈、队列、树）
                    基本数据类型：bool int(float) str list tuple dict set

        3、文件操作相关
            open()

        4、查看帮助
            help()

        5、查看对象或者类有哪些内置方法
            dir()

        6、查看变量名是否是可以被调用的,用来区分普通变量和函数名
            callable()

        7、模块导入相关
            __import__() #用的较少 一般是import os

        8、字符串类型代码的执行
            01 eval()  参数是字符串，返回的是去掉字符串两端的引号
                #1 将字符串形式的列表，转换成列表
                s1 = "['jack','tom']"  #字符串转换成了列表，去掉了两端的双引号
                print(eval(s1))  #['jack', 'tom']

                #2 将字符串形式的字典，转换成字典 应用场景：前后端传递数据的json串就是--字符串形式的字典
                s2 = "{'name':'jack','age':123}"  #字符串转换成了字典，去掉了两端的双引号
                print(eval(s2)) #{'name': 'jack', 'age': 123}

                #3 将字符串形式的数字，转换成数字int
                s3 = '12'
                print(eval(s3)) #12
                print(type(eval(s3))) #<class 'int'>

                #4 将字符串形式的数字表达式，转换表达式的结果-int  应用场景：计算器
                s4 = '1+2+3'
                print(eval(s4)) #6
                print(type(eval(s4))) #<class 'int'>

            2 exec()  可以执行字符串的代码，只是执行，没有返回值（可以变相获得返回结果
                print(exec('1+2+3'))  #None  没有返回值，所以是None
                print(exec('a=1+2+3')) #None 没有返回值，所以是None,但是'a=1+2+3' 相当于a=6  注意点
                print(exec('a=6')) #None 没有返回值，所以是None,和上面等效  变相获取返回结果
                print(a) #6

                eval（）和exec()之间的区别
                1、前者有返回值
                2、后者没有返回值（部分情况，可以变相获得返回值）

            3 compile() 将字符串类型的代码编译. 代码对象能够通过exec语句来执行或者eval()进行求值

            参数1：存放字符串类型的代码
            参数2：py文件的文件路径，类型是str
                   代码存放的⽂文件名, 当传⼊了第一个参数的时候, 这个参数给空就可以了
            参数3：模式，一共是3个，类型是str
                    1、模式1--eval模式，对应计算表达式，有返回值的，列表或者字典去掉双引号
                    2、模式2--exec模式，没有返回值的，比如for循环
                    3、模式3--single模式-交互模式，比如：含有input的

            上述参数1和参数2是二选一的
            如果用了参数1，参数2就是空字符串''

            compile(source, filename, mode)
            参数
            source -- 字符串或者AST（Abstract Syntax Trees）对象。。
            filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
            mode -- 指定编译代码的种类。可以指定为 exec, eval, single。

            返回值
            返回表达式执行结果

            compile()和---exec()、eval()的区别
            1、前者多了多代码的编译，最后还是要用到后者
            2、后者少了编译的动作，直接运行代码

    6、基本数据类型相关-38个
        1、和数字相关--14个
            1、数字类型--4个
                1、bool()
                    True 1及其他非空的，包括空格
                    False 0 None Null '' [] () {} set()

                2、int()   #整数

                3、float()  #小数

                4、complex() #复数
                    整数+小数=有理数
                        无理数：无限循环小数 比如：pi 1/3
                    有理数+无理数=实数
                        虚数：-1的平方根就是虚数
                    实数+虚数=复数

            2、进制转换--3个
                1、bin()  --十进制转二进制
                   0b开头表示二进制
                   0b101就是5

                2、oct（）--十进制转八进制
                    0o开头表示八进制
                    0o11就是9

                3、hex()  --十进制转十六进制
                    0x开头表示十六进制
                    0x11表示11

            3、数学运算--7个
                1、abs() --求绝对值

                2、divmod(arg1,args2) --求商和余数
                    参数1是被除数，参数2是除数

                3、pow(args1,args2)  --求args1的args2次方

                4、round(args1[,args2])  --四舍五入
                   将参数1进行四舍五入，参数2不是必须，如果参数2写了3，就是保留3位小数
                   注意：小数的四舍五入可能不准确

                    print(round(4.12345,2))  #4.12 四舍五入保留2位小数
                    print(round(4.5))  #4  因为4.5在计算机中可能是4.49999999999
                    print(round(9.5))  #10 因为9.5在计算机中可能是9.50000000001

                5、sum(Iterable[,int|float])
                    1、参数是可迭代的-Iterable
                    2、参数2可以不写，默认是0
                    3、参数1的元素和参数2可以是int，也可以是float
                    4、返回的是Iterable中元素的和，然后加上参数2
                    5、注意:1：参会1如果不是Iterable，就会报错
                        print(sum(1,2))  #报错 TypeError: 'int' object is not iterable
                    6、注意点2：参数1是字符串的时候
                        s1 = '123'  #当s1 = 123的时候，会自动把int123转换成str-'123'
                        print(s1,2)  #123 2

                6、max(arg1,arg2...argn)
                   max(Iterable)
                   1、如果是多个位置参数，则返回其最大值
                      位置参数推荐是int或者float，不推荐字符串
                    2、如果参数是Iterable，则返回其元素中最大值

                7、min(arg1,arg2...argn)
                   min(Iterable)
                   1、如果是多个位置参数，则返回其最小值
                      位置参数推荐是int或者float，不推荐字符串
                    2、如果参数是Iterable，则返回其元素中最小值

        2、和数据类型相关--24个
            1、数据集合--3个
                1 set()
                2 frozenset()
                    set和frozenset的区别  类似 列表和元组
                    set是可变类型，可以增删改
                    frozenset是不可变类型，不能增删改

                    不可变类型（可哈希的）可以作为字典的key
                    可变类型（不可哈希的）不能作为字典的key--会报错
                            TypeError: unhashable type: 'set'

                    不可变数据类型：str int|float  bool tuple frozenset
                    可变数据类型：list dict set
                3 dict()

            2、相关内置函数--8个
                1 len(Iterable)   求长度   -ok  1 代码注释-help  2 官网  3 cainiao
                    1、参数是可迭代的-Iterable
                        str list tuple dict set range()

                2 sorted(iterable, cmp=None, key=None, reverse=False)  排序
                    1、参数1是可迭代的-Iterable
                    2、后面的3个参数都是必选的（不写都有默认值）
                       1、reverse=False，默认升序
                          reverse=True，是降序
                        2、参数3--key
                            默认是None
                            比如：列表的元素是元组，按照元组的第二个元素进行排序
                    3、sorted()函数是将原迭代的对象复制了一份，而没有修改原对象本身
                                sorted()函数适用于所有的可迭代的类型--Iterble
                       sort()方法是列表的内置方法，对列表本身进行了修改
                                sort()方法只适用于列表
                    4、注意点：参数4是reverse,自动提示出来的是reversed，要区分

                3 enumerate(iterable, start=0) 枚举
                    1、参数1是可迭代的-Iterable
                    2、参数2表示索引的起始值

                4 any(Iterable)
                    any相等于or--或者
                    1、其参数中的元素有一个是True，结果就是True；
                    2、只有全部元素都是False，才是False；
                    3、如果是空列表、空元组，也是False；
                    4、0 None '' [] () {} set() False是False；其余都是True
                        0 None False 空--'' [] () {} set()
                    5、any的参数是可迭代的对象-Iterable

                5 all(Iterable)
                    all相等于and-并且，与
                    1、其参数中的全部元素都是True，结果才是True；有一个是False，结果就是False
                    2、0 None '' [] () {} set() False是False；其余都是True
                        0 None False 空--'' [] () {} set()
                    3、all的参数是可迭代的对象-Iterable
                    4、参数是空列表或者空元组，返回是True--特殊点

                6 zip([iterable1, iterable2,...])
                    1、将2个或者2个以上可迭代对象的对应位置的元素，打包成一个个元组
                        返回一个迭代器（可以转换成列表，也可以直接遍历循环）
                    2、如果可迭代对象的元素个数不相等，打包成元组的时候，以最少元素的为准
                    --水桶效应

            3、序列
                1、列表和元组
                    list()   #把参数转换成列表类型
                    tuple()  #把参数转换成元组类型

                2、翻转和切片
                    reversed() #把参数转换成迭代器，把迭代器转换成列表，元素就是反转的
                                #参数是可迭代类型-Iterable
                    slice()  #切片，不常用，了解即可，推荐li1[0:2]写法
                3、字符串相关
                    1、str()  #转换成字符串类型
                    2、format() #参数是int或者float，返回str
                        1、把int转成二进制、八进制、十六进制，返回str
                        2、把小数float，保留几位小数，返回str
                    3、bytes() #把str转换成utf-8的字节
                        参数是str，返回的是字节（b开头的十六进制）
                    4、bytearray() #把字符串的字符取出来，转换成ascill数字
                        参数是str，返回的是数字（0-255之间的ascii数字）
                    5、ord() #把字符转换成ascii码或者数字
                        参数是字符，返回是0-255的ascii的数字及255以上的数字
                    6、chr() #把数字转换成字符
                        参数是0-65536之间的数字，返回的是字符（英文、中文及其他字符）
                    7、ascii() #判断字符是否在ascii表中
                        参数是字符，返回的是字符本身（如果是ascii中），如果不是在ascii中，就返回 \u 开头的
                    8、repr() #原封不动的输出, 引号和转义字符都不起作用
                        参数是字符串，返回的是字符串（带引号，转义字符不起作用）

'''

#哈希数
s = 'alex'
print(hash(s))  #可以是正数，也可以是负数，每次打印都不同
# -8039401401128360439
# 2405962226061413329
print('-----------1 哈希数')

#是否是可以被调用的
a = 123
print(callable(a))  #False

def func():
    pass
print(callable(func))  #True
#函数callable()可以用来区分函数名和普通变量的名字  函数名也属于变量
print('-----------2 是否是可以被调用的')

#进制转换
a=5
print(bin(a))  #0b101  二进制

a2 = 9
print(oct(a2))  #0o11  八进制

a3 = 16
print(hex(a3))  #0x10 十六进制
print('-----------3 进制转换')

print(round(4.12345,2))  #4.12 四舍五入保留2位小数
print(round(4.5))  #4  因为4.5在计算机中可能是4.49999999999
print(round(9.5))  #10 因为9.5在计算机中可能是9.50000000001
print('-----------4 四舍五入 保留几位小数')

li1 = [1,2,3]
s1 = '123'
print(sum(li1,3))  #9  #参数1必须是可迭代类型的-Iterable
print(sum(li1,3.1))  #9.1  #参数1的元素和参数2可以是int也可以是float
print(sum(li1))  #6  #参数2可以不写，默认是0
# print(sum(1,2))  #报错 TypeError: 'int' object is not iterable
print(s1,2)  #123 2
print('-----------5-1 求和')

#题目：计算li1=[1,2,3]和li2=[4,5,6]这两个列表中所有元素的和
#方法1  推荐 更简洁
li1=[1,2,3]
li2=[4,5,6]
print(sum(li1)+sum(li2))  #21
# print(6+15)  #21

#方法2
li1=[1,2,3]
li2=[4,5,6]
print(sum(li1,sum(li2)))  #21
# print(sum(li1,15))
# print(sum(6,15))
print('-----------5-2 求和')

print(max(1,2))
# max(iterable, *[, key, default])
# max(arg1, arg2, *args[, key])
# Return the largest item in an iterable or the largest of two or more arguments.
#如果是多个参数，则返回多个参数中，最大的值（多个参数建议是int|float ,不推荐用字符串）
#如果是1个Iterable参数，则返回其元素中最大的值
li1 = [1,2,3]
print(max(li1)) #3
# print(max(li1,4)) #报错 TypeError: '>' not supported between instances of 'int' and 'list'
print('-----------6-1 求最大值')

print(min(1,2,6))  #1
li2 = [5,3]
print(min(li2))  #3
print('-----------7 求最小值')

#和数据类型相关
#1 数据集合
#set和frozenset的区别  类似 列表和元组
'''
set是可变类型，可以增删改
frozenset是不可变类型，不能增删改

不可变类型（可哈希的）可以作为字典的key
可变类型（不可哈希的）不能作为字典的key

不可变数据类型：str int|float  bool tuple frozenset
可变数据类型：list dict set
'''

set1 = {'刘德华','刘德凯'}  #集合的本质是只有key的字典
# dic1 = {set1:'哈哈'}
# print(dic1)  #TypeError: unhashable type: 'set'  报错

set2 = {'刘德华','刘德凯'}  #集合的本质是只有key的字典
set3 = frozenset(set2)
dic2 = {set3:'哈哈'}
print(dic2)  #{frozenset({'刘德凯', '刘德华'}): '哈哈'}



















