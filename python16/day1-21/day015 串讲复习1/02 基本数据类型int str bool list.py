#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/8 8:21
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
1 python的定义
    是一门弱类型的解释性的高级编程语言
    这里的高级是相对低级（例如：汇编语言等）

    高级编程语言和低级编程语言的区别
    1、前者更接近于人的理解--字母组成的语法
    2、后者更接近于计算器的理解--字节码、二进制

2 python的特点
    人生苦短，我用python
    简洁

3 为什么学习python
    爱好，人工智能，机器学习，大数据

4 python第一个程序
    print('hello world')
    方式1：在cmd中输入python后，在交互命令行，输入上述语句，enter
    方式2：在本地d盘新建一个hello.py的文件，将上述语句复制到.py文件中，保存后
           在cmd中，进入到d盘， 执行命令 python hello.py
    方式3：将上述语句写入pycharm后，run

5 变量的概念
    变量是程序运行过程中产生的中间值--temp（暂存属性，开辟一个内存空间，用于保存值）
        1、内存空间的名字就是变量的名字
        2、内存空间保存的值就是变量的值
        比如： a=10  变量名字就是a 变量的值是10

6 变量的命名规则：
    1、组成：数字、字母、下划线组成
    2、开头：不能是数字开头
    3、关键字：不能是关键字，比如：list
    4、长度：不要太长
    5、中文：不要是中文
    6、有意义：要有意思（一看名字，就知道变量大概表示的意思）
    7、大小写：严格区分大小写
    8、写法：推荐下划线或者驼峰法命名
        下划线：hello_world（单词之间，下划线分隔开）
        驼峰法：helloWorld  (首字母不大写，第二个单词开始，首字母大写)

7 变量的数据类型
    1 int 整数  + - * / // bit_length()
    2 str 字符串
        1、表示方式 ' " \''' \"""   注意点：这里的\ 表示转义
            1 单引号''
            2 双引号""
            3 三个单引号 ''' '''
            4 三个双引号 """ """
        2、* 重复
        3、+ 拼接
        4、%s 格式化
        5、索引和切片
            s1[start:end:step]  左闭右开
            1 start 起始索引号-下标
            2 end   结束索引号-下标 （取不到）
            3 start 步长（不写，默认是1）

        6、常见内置方法
            1 upper()  转换成大写字母

            2 strip() 去掉字符串两端的空白
               strip('ab')  去掉字符串两端的'ab'

            3  replace(old,new,count)
                参数3 count表示从左到右替换的次数
                参数3不写，默认是全部替换

            4  split() 把字符串拆分成几个子字符串，每个子字符串作为列表的元素，返回的是列表
                默认分隔符是空格
                split('_') 分隔符是下划线

            5  '_'.join() 把参数iterable中的字符串通过连接符'_'拼接成字符串
                写法： '连接符'.join(iterable)
                注意点：
                    1 iterable中的元素必须是str，而不能是int
                    2 join不是字符串的内置方法

            6  startswith()
                写法：s1.startwith('a')
                作用：判断字符串是否以字母'a'开头

            7 find index count
                写法：s1.find('a')
                作用：从字符串s1中查找字符‘a’,返回索引号；如果找不到，就返回-1  --更健壮  推荐

                写法：s1.index('a')
                作用：从字符串s1中查找字符‘a’,返回索引号；如果找不到，就报错

                写法：s1.count('a')
                作用：从字符串s1中统计字符'a'出现的次数，返回出现的次数int
                    如果是0次，代表没有找到（也有查找的功能）
            8 isdigit()
                写法：s1.isdigit()
                作用：判断字符串是否是数字形式的，是的话，返回True

            9 len()
                写法：len(s1)
                作用：返回字符串的长度

        7、字符串是iterable
            for i in s1:
                循环体(break continue)
            else:
                pass

        8、字符串的编码方式
            1 ascii             8位 1个字节
            2 gbk 国标码 gb2312 16位 2个字节
            3 unicode 万国码    32位 4个字节
            4 utf-8 可变的unicode
                1 英文字符  8位 1个字节
                2 欧洲字符 16位 2个字节（德文、法文、西班牙文等字符）
                3 中文字符 24位 3个字节
            字符串编码后变成字节bytes
                编码-加密-压缩
            字节解码后变成字符串
                解码-解密-解压
                bytes.decode()  #解码

    3、bool 布尔类型
        取值：True False
        作用:用于判断的
        类型转换：
            False:0或者空('' [] () {} set() None)
                        空字符串、空列表、空元组、空字典、空集合、空None
                注意：空格、\r \n \t都是True
            True：除了上面的，其他都是True
            注意点：类型转换False可以直接用于判断
        备注：
            例子1
            content1 = input('请输入你的名字:')  #输入的是字符串
            if content1:  #判断空  如果不输入内容，直接回车，就提示-你没有名字 注意点：和下面行的结果不一样
            # if content1 == '':  #如果不输入内容，直接回车，就打印-你的名字是
                print('你的名字是 ',content1)
            else: #如果你什么都没有输入，这个content1就是空字符串
                print('你没有名字')

            例子2
            li1 = [1,2,3]
            if li1:  #这里就是在判断列表是否为空， 和下面行等效
            # if li1 == []:
                print(li1)
            else: #
                print('空列表')

    4、列表 list
        表示：[]，元素之间是逗号隔开
        概念：列表是一个容器，可以存放任意数据类型
            和其他开发语言的数组array类似
        特点：
            1、列表是可变的
            2、列表由索引和切片功能
        常见操作：
            1 增
                1 append(元素值)
                    在列表最后面追加元素
                2 insert(i,元素值)
                    在列表指定位置前插入元素
                3 extend(iterable)
                    把iterable中的元素依次添加到原列表
            2 删
                1 pop()
                    参数不写，默认是删除最后一个元素
                    参数也可以指定索引号，来删除
                2 remove
                    删除指定的元素值
                3 del
                    切片或者单个删除
                4 clear
                    清空元素
            3 改
                1 按照索引-下标修改
                    切片修改
                    单个索引号修改
            4 查
                1、单个索引号取值
                2、for循环遍历

                01列表-增加元素小结
                    1 append是末尾追加新元素--最常用
                    2 insert是指定位置前插入新元素
                    3 extend是将iterable中元素依次添加到原列表
                02列表-删除元素小结
                    1 pop
                        不带参数，默认删除列表最后一个元素，并且获取到被删除的最后一个元素
                        指定参数，删除指定位置-索引号的元素，并且获取到被删除的指定位置的元素
                    2 remove
                        参数：元素值（不是位置）
                        作用：删除指定元素值
                    3 del
                        1 参数：单个位置-索引号
                          写法：del 列表(位置)
                          作用：删除单个位置的元素
                        2、参数：切片
                          写法：del 列表(切片)
                          作用：切片删除多个位置的元素
                        3、参数：列表名
                           写法：del 列表名
                           作用：删除整个列表，回收内存空间（和清空clear是不同的）
                        4、参数：字典的key
                            写法：del 字典名[key]
                            作用：删除字典中指定key对应的键值对
                        综上，del的作用
                        1、可以删除单个位置的元素
                        2、可以切片删除多个元素
                        3、可以删除整个列表，回收内存空间
                        4、不仅是列表，也适用于字典
                    4 clear
                        参数：为空
                        写法：li1.clear()
                        作用：清空列表的元素，变成空列表
                             清空-列表的内存空间没有被回收（和del li1不一样）
                03列表-修改元素小结
                    1 单个位置修改--单个元素修改
                        写法：li3[1] = 'james'
                        作用：指定位置-索引号进行列表单个元素的修改

                    2、切片多个元素修改
                        1 2个元素改成1个元素
                            正确写法：li3[1:3] = ['james']
                            错误写法：li3[1:3] = 'james'   注意点

                        2 2个元素改成2个元素
                            写法：li3[1:3] = ['james','kevin']

                        3 2个元素改成3个元素
                            写法：li3[1:3] = ['james','kevin','lucy']
                04列表-查询元素小结
                    1 单个查询-单个取值-按照单个位置-索引号-下标
                    2 多个查询-多个取值-按照切片
                    3 全部查询-全部取值-for循环遍历

            5、其他常见操作
                1 count() 计数
                    计算某个元素在列表出现的次数
                2 index() 查找
                    返回某个元素在列表中的位置-索引号-下标
                3 sort() 排序
                    把列表的元素进行排序，默认升序，列表本身修改了
                4 reverse（）反转
                    把列表的元素反转，列表本身修改了

            6、列表在循环遍历的过程中，不能删除元素，因为涉及到元素的移动
               解决办法：
               把要删除的元素，添加到新的列表中，循环新列表，删除老列表

            7、深浅拷贝和赋值
                1、= 赋值，两个变量指向同一个内存地址，不同的变量只是同一个内存地址的不同别名
                2、浅拷贝，只拷贝第一层（第二层及以上还是指向同一个内存空间，没有实现拷贝）
                    li1.copy()
                    li1[:]
                    检验是否是一个内存空间的办法：看变量的id值
                3、深拷贝，不仅拷贝第一层，第二层及以上都拷贝
                    li1.deepcopy()
                扩展：在其他的编程语言（比如：java），叫做克隆，也分为深浅克隆

                浅拷贝和深拷贝的类比
                1、浅拷贝是第一层内存空间分开，第二层及以上内存空间是同一个
                         --第一层独立，第二层及以上是一变都变
                          第一层就是家庭夫妻财务AA
                          第二层就是家庭夫妻设立的共同账户
                2、深拷贝是第一层内存空间分开，第二层及以上内存空间也分开--每层完全独立
                          类比：家庭夫妻财务完全AA，没有设立共同账户

            8、列表推导式
                写法
                    [结果 for循环 if判断]
                例子：
                    li7 = [1,2,3]
                    #需求：将列表中的奇数，变成其平方数
                    li8 = [i*i for i in li7 if i%2 == 1 ]
                    print(li8)  #[1, 9]

'''

a=10
b=10
print(id(a))
print(id(b))
# 140728979583520
# 140728979583520

a='a'
b='a'
print(id(a))
print(id(b))
# 367204302448
# 367204302448














