#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/11 6:54
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
变量的数据类型
int str bool list
5、字典 dict
    定义和写法：由{}表示，每个元素是key:value的键值对形式，元素间是逗号隔开
    特点：
        1、key是可哈希的-不可变类型（比如：int str tuple bool）
            value的类型是不限制的，可以存放任意数据类型
        2、字典是无序的，没有索引和切片
    常见操作：
        增
            1、dic[key] = value   #单个键值对添加，先建立一个空字典
            2、dic = {k1:v1,k2:v2} #一次添加多个键值对-字典的定义
            3、ret= dic.setdefault(key,value) #如果key已经存在，不会覆盖
               #添加键值对，返回添加的value
            4、dic2 = dic.fromkeys(iterable,value) #iterable中每个元素共用一个value
               dic2 = dict.fromkeys(iterable,value)  #类方法
                #注意点1：会新产生一个新字典，原字典本身不会改变
                #注意点2：fromkeys是一个类方法

        删
            1、pop
                参数是key，删除key对应的元素-键值对，并且获取被删除元素的value
            2、popitem
                参数是空，随机删除一个元素-键值对，并且获取被删除元素-键值对
                注意：从表面看，是删除了字典的最后一个键值对，但是字典的key是无序的，所有还是随机的
            3、del
                1、参数是key，删除key对应的元素-键值对
                2、还可以直接删除整个字典，回收内存空间
            4、clear
                清空字典的元素-键值对，变成空字典
        改
            1 dic[key] = 新value
                根据key获取到字典的value，对value进行重新赋值
            2 update
                dic1.update(dic2)
                把字典2的元素依次添加到字典1
                注意:如果字典2的key和字典1的key有相同的，会出现value的覆盖
        查-取值
'''
'''
            1 dic[key]
                根据自定的key取value值，如果key不存在，就报错
            2 get
                写法:字典.get(key[,value])
                参数1是key，参数2是默认返回值（不写默认是None）
                1、如果key存在，就返回字典中key对应的value
                2、如果key不存在，不会报错，会返回参数2（参数2不写默认是None）
                    这一点上，健壮性强于dic[key]来取值
            3 setdefault  添加元素，并取值元素的value（key如果已经存在，不会覆盖）
                写法:字典对象.setdefault(key1,value1)
                参数1是新增加元素的key，参数2是新增加元素-键值对的value
                1、将参数1和参数2作为新元素-键值对添加到字典对象
                    原字典对象添加了一个新元素-键值对
                2、返回者是参数2，即获取新增加的value作为返回值-这个返回value1就是取值
                    （和pop的删除并返回被删除值有类似之处，
                      setdefault是添加并返回添加的value）
                3、如果key1已经在原字典对象中存在了，新的键值对将无法添加，原字典对象保持不变
                    这里不会覆盖原字典对象的value
                    注意点：不会覆盖这个点和dic[key]=value，如果key已经存在，会覆盖，是不同的

        字典for循环：
            1、iterable
                dic1 dic1.keys() dic1.values()
            2、for i in dic1:
                   print(i,dic1[i])

                for i in dic1.keys():
                    print(i,dic1[i])  #用的比较少

                for i in dic.values():
                    print(i)  #适用场景:比如求value的平均值

                for i in dic1.items():
                    print(i)  #这里返回是列表，列表的元素是键值对元组 (k1,v1)

                for k,v in dic1.items():
                    print(k,v)

6 元组--tuple
    1、元组是只读的，不可变
        不可变的是元组的第一层
        如果元组的元素是列表，列表是可以添加删除元素的
    2、操作方法比较的少
        count()
        index()
        len()
    3、iterable-可迭代的
        支持for循环
        （for循环的取值速度：dict>set>list>tuple）
    4、元组是没有元组推导式的

7 集合-set
    1、集合的概念：只有key的字典
    2、特点：
        无序
        去重
        元素是不可变的（可哈希的）--因为字典的key是不可变的
    3、支持for循环，iterable
    4、可冻结的集合 frozen
        特点：frozen本身是不可变的（可哈希）
    5、操作
        两个集合之间可以& | -  (交集&、并集|、差集)等
    6、备注：
        set不能作为字典的key
        frozetkey作为字典的key
'''














