#!/usr/bin/env python
#-*- coding:utf-8 -*-

''''''
'''
一、字典的定义
	1、由{}表示，每个键值对由逗号，分开；键值对的key和value是冒号：分开；
	2、查询效率非常高，通过key来查询
	3、字典的key是不可变类型（字符串、int、元组、bool等），可哈希（不可变）
		内部使用key来计算内存地址，然后将键值对key-value保存在这个内存地址（暂时这么理解）
	4、key是唯一且不可变的（不可变的原因是为了准确计算其内存地址）
		value没有要求，和list一样，可以保存任意类型的数据
	5、不可变的类型（可哈希）：int str bool tuple
	      可变的类型（不可哈希）: list dict set
	6、字典的键值对是无序的，键值对的存储不是按照添加顺序添加的，而是按照hash表进行存储的，
	     而hash表不是连续的，所以字典不能进行切片操作，是通过key来高效取值value的

二、字典的增删改查
	1、新增
		dic1["新key"] = value  #如果key不相同，就是新增；如果key相同，就是覆盖之前的value
		dic1.setdefault(key,value)  #如果ket相同，则不新增

	2、删除
		dic1.pop(key)  #删除指定的key，并且获取该key对应的值
		dic1.popitem() #随机删除一个key，并且获取该key对应的值
		del dic1[key]
		dic1.clear()

	3、修改
		dic1[key]= value
		dic1.update(dic2) #如果key不相同，就是新增；如果key相同，那么就是覆盖之前的value

	4、查询
		dic1[key]
		dic1.get(key,[tishi])  #如果key不存在，默认是返回none;
						 #如果参数2指定了，那么如果key不存在，就返回参数2
		dic1.setdefault(key,value) #如果key不相同，在新增键值对的时候，同时返回value
						#注意：一个方法实现新增和查询2个流程（和pop的写法有类似-删除和查询）

三、字典的操作
	print(dic1.keys()) ##获取所有的key的集合，返回的像列表，但是不是列表，也不是set集合
	dic1.values()  #获取所有的value的集合，可以遍历
	dic1.items()  #获取所有的键值对的集合，返回的是元组的形式
	a,b = (10,20)  #解包，必须数目是相等的，一一对应

四、遍历字典
	方法1
	for i in dic1:  #直接遍历字典本身，因为字典是可迭代类型
		print(i)  #打印key
		print(dic[i])  #打印value

	方法2
	for k,v in dic1.items():
		print(k) #打印key
		print(v) #打印value

五、嵌套字典




'''














