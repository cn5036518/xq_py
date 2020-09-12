#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/11 7:25
#@author:wangtongpei
#@email: cn5036520@163.com

#新增
#方法1  dic[k] = v  先建空字典，然后单个键值对依次添加
dic1 = {}
dic1['name'] = 'jack'
dic1['age'] = 18
dic1['name'] = 'jack2' #注意点：key如果已经存在，就会覆盖value
print(dic1)  #{'name': 'jack2', 'age': 18}
print('----------------------------------------1 单个键值对依次添加')

#方法2 dic1={k1:v1,k2:v2}  一次新增多个键值对
dic2 = {'name':'jack','age':19}  #一次新增多个键值对，字典的定义
print(dic2)  #{'name': 'jack', 'age': 19}
print('----------------------------------------2 一次新增多个键值对')

#方法3 dic.setdefault(k,v)
dic3 = {}
ret1 = dic3.setdefault('name','tom')
dic3.setdefault('name','bob')  #注意点1：如果key已经存在，不会覆盖(和方法1中单个添加键值对会覆盖不同)
print(dic3)  #{'name': 'tom'}
print(ret1)  #tom  注意点2：添加键值对的同时，返回添加的value值（类似：pop的删除并获取）
#注意点3：必须新建一个空字典，或者用一个已经存在的字典来调用setdefault;调用后，对原字典进行了修改
print('----------------------------------------3 setdefault 内置方法 添加键值对并返回value')

#方法4  dic.fromkeys(iterable,v)
li1 = ['jack','tom','bob']
dic5 = dict.fromkeys(li1,19)  #注意点1：把参数1中，iterable中每个元素作为key，参数2作为value
# 注意点2： fromkeys是字典类或者字典对象的内置方法，可以用dict类直接调用
# 注意点3：字典对象本身不会改变；而是会新产生一个新的字典
print(dic5)  #{'jack': 19, 'tom': 19, 'bob': 19}
print('----------------------------------------4-1 fromkeys 内置方法 一次添加多个键值对 value相同')

li1 = ['jack','tom','bob']
dic4 = {}
dic5 = dic4.fromkeys(li1,19)  #注意点1：把参数1中，iterable中每个元素作为key，参数2作为value
# 注意点2： fromkeys是字典类或者字典对象的内置方法，
# 注意点3：如果是字典对象，字典对象本身不会改变；而是会新产生一个新的字典
print(dic4)  #{}
print(dic5)  #{'jack': 19, 'tom': 19, 'bob': 19}
print('----------------------------------------4-2 fromkeys 内置方法 一次添加多个键值对 value相同')
'''
字典新增小结：
1 单个键值对一个一个添加（先建立一个空字典）
2 一次性添加对个键值对--字典的定义
3 setdefault
    添加单个键值对，并且返回value（类似pop），原字典本身修改了（先建立一个空字典）
4 fromkeys
    dict.fromkey(iterable,v)   #类方法
    dic1.fromkey(iterable,v)
    参数1是iterable，把参数1中的元素作为key，参数2作为value,创建字典
    注意点：原字典（可以是字典对象、空字典对象，也可以是dict类）本身没有修改，产生了一个新的字典
'''

#删除
#方法1  pop 删除单个元素（指定key对应的键值对）
dic1 = {'name':'jack','age':18}
ret1 = dic1.pop('age') #参数是key
# 删除指定key对应的键值对,并且获取被删除元素的value
print(dic1) #{'name': 'jack'}
print(ret1) #18
print('----------------------------------------2-1 pop删除单个元素,并且获取被删除元素的value')

#方法2  popitem  随机删除一个键值对（写法上看起来是删除了最后一个键值对）
dic2 = {'name':'jack','age':18}
print(dic2) #{'name': 'jack', 'age': 18}  #表明上显示的和定义的键值对顺序一样
ret2 = dic2.popitem()   #没有参数，字典的元素-键值对是无序的，所以表面上是删除了最后一个键值对
#实际上，删除的键值对是随机的
print(dic2) #{'name': 'jack'}
print(ret2)  #('age', 18) #并且返回被删除的元素（键值对）-元组形式
print('----------------------------------------2-2 popitem删除单个元素，并且获取被删除元素（键值对）-元组形式')

#方法3  del  删除单个元素或者删除整个字典-内存空间回收
dic3 = {'name':'tom','age':19}
del dic3['name']  #参数是key，删除指定key所在的键值对
print(dic3) #{'age': 19}
print('----------------------------------------2-3-1 del删除单个元素')

dic31 = {'name':'tom','age':21}
del dic31 #删除整个字典
# print(dic31) #报错 NameError: name 'dic31' is not defined
print('----------------------------------------2-3-2 del删除整个字典')

#方法4 clear
dic4 = {'name':'james','age':20}
dic4.clear()
print(dic4)  #{}
print('----------------------------------------2-4 清空字典')

'''
字典删除小结：
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
'''

#3修改
#方法1  通过dic[key]获取字典的value，然后给value重新赋值
#   dic[key]=新value
dic31 = {'name':'bob','age':31}
dic31['age'] = 15
print(dic31)  #{'name': 'bob', 'age': 15}
print('----------------------------------------3-1 修改字典')

#方法2  update方法  把字典2的元素合并到字典1
dic32 = {'name':'bob','age':31}
dic33 = {'name':'kevin','age':21}
dic32.update(dic33)
print(dic32)  #{'name': 'kevin', 'age': 21}
#注意点1：这里字典2和字典1的key是一样的，所以字典2会替换字典1
print('----------------------------------------3-2 修改字典 update 覆盖')

#方法3  update方法
dic32 = {'name':'bob','age':31}
dic33 = {'name2':'kevin','age2':21}
dic32.update(dic33)
print(dic32)  #{'name': 'bob', 'age': 31, 'name2': 'kevin', 'age2': 21}
#注意点2：这里字典2和字典1的key是不一样的，所以字典1会把字典2的元素合并进来
print('----------------------------------------3-3 修改字典 update 新增元素')

'''
字典修改小结：
1 dic[key] = 新value
    根据key获取到字典的value，对value进行重新赋值
2 update
    dic1.update(dic2)
    把字典2的元素依次添加到字典1
    注意:如果字典2的key和字典1的key有相同的，会出现value的覆盖
'''

#4查询-单个取值(多个取值用for循环遍历)
#方法1 根据key取值
dic41 = {'name':'lucy','age':11}
print(dic41['name']) #lucy
print('----------------------------------------4-1 查询 根据key取值')

#方法2：get
dic41 = {'name':'lucy','age':11}
print(dic41.get('age')) #11
print(dic41.get('age1')) #None  #如果key不存在，不会报错，会返回None（这个方面，get方法取值比dic[key]更健壮）
print(dic41.get('age1','没找到')) #没找到
#参数1是key，参数2是如果key不存在，默认返回值
print('----------------------------------------4-2 查询 get')

#方法3：setdefault
dic43 = {'name':'lucy','age':11}
dic44 = dic43.setdefault('age2',17)  #
#参数1是key 参数2是value  添加一个键值对，并且返回新增的value
print(dic43) #{'name': 'lucy', 'age': 11, 'age2': 17}
print(dic44)  #17
print('----------------------------------------4-3-1 查询 setdefault')

dic43 = {'name':'lucy','age':11}
dic44 = dic43.setdefault('age',17)  #
#参数1是key 参数2是value  添加一个键值对，并且返回新增的value
#注意点：如果新增的key已经存在，那么value不会覆盖
#这个层面上，setdefault方法，key存在的话，就是根据key进行取value值
#key之前不存在的话，就是根据新key进行取新value值
print(dic43) #{'name':'lucy','age':11}
print(dic44)  #11
print('----------------------------------------4-3-2 查询 setdefault')
'''
字典查询小结：
1 dic[key]
    根据自定的key取value值，如果key不存在，就报错
2 get
    写法:字典.get(key[,value])
    参数1是key，参数2是默认返回值（不写默认是None）
    1、如果key存在，就返回字典中key对应的value
    2、如果key不存在，不会报错，会返回参数2（参数2不写默认是None）
        --这一点上，健壮性强于dic[key]来取值
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
'''

#5 for循环遍历
#1 keys() 列出字典所有的key，返回的是列表，列表的元素是字典的key
#2 values() 列出字典所有的value，返回的是列表，列表的元素是字典的value
#3 items() 列出字典所有的元素-键值对，返回的是列表，列表的元素是键值对元组(k1,v1)
dic51 = {'name':'lily','age':12}
print(dic51.keys())  #dict_keys(['name', 'age'])
print(type(dic51.keys())) #<class 'dict_keys'>
print('__iter__' in dir(dic51.keys())) #True  说明dic51.keys()是iterable
print(list(dic51.keys()))  #['name', 'age']

print(dic51.values()) #dict_values(['lily', 12])
print(dic51.items())  #dict_items([('name', 'lily'), ('age', 12)])
print('----------------------------------------5-0 keys values items')

for i in dic51:
    print(i) #注意点1：直接遍历循环字典，输出的是key，而不是键值对
# name
# age
print('----------------------------------------5-1-1 直接循环遍历字典')

for i in dic51:   #常用1
    # print(i,dic51(i)) #报错：TypeError: 'dict' object is not callable
    print(i,dic51[i]) #报错：TypeError: 'dict' object is not callable
# name lily
# age 12
print('----------------------------------------5-1-2 循环遍历字典')

for i in dic51.keys():
    print(i)
# name
# age
print('----------------------------------------5-2-1 循环遍历dic.keys()')

for i in dic51.keys():
    print(i,dic51[i])
# name lily
# age 12
print('----------------------------------------5-2-2 循环遍历dic.keys()')

for i in dic51.values():
    print(i)
# lily
# 12
print('----------------------------------------5-3 循环遍历dic.values()')

for i in dic51.items():  #常用3
    print(i)
# ('name', 'lily')
# ('age', 12)
print('----------------------------------------5-4-1 循环遍历dic.items()')

for k,v in dic51.items():  #常用2
    print(k,v)
# name lily
# age 12
print('----------------------------------------5-4-2 循环遍历dic.items()')

'''
字典for循环小结：
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
'''

#6 字典的长度（元素的个数-键值对的个数）
dic61 = {'name':'jack','age':13}
print(len(dic61))  #2
print('----------------------------------------6-1 字典的长度')

#7 如何在循环遍历字典的时候，删除元素
#思路：不能直接删除，
# 1需要先把字典的key都存放到列表，
# 2然后循环列表，根据列表的元素作为key来删除
dic7 = {'name':'tom','age':14,'hobby':'run'}
li1 = list(dic7.keys())
print(li1) #['name', 'age', 'hobby']

for i in li1:  #1循环遍历列表
    del dic7[i] #2
print(dic7)  #{}
print('----------------------------------------7-1 字典的循环删除 ')

#8 字典推导式
# dic8 = {k1:v1 for循环 条件}
#需求1 将字典的key和value对调
dic8 = {'name':'bob','age':15}
dic9 = {dic8[i]:i for i in dic8}  #{'bob': 'name', 15: 'age'}
# i是字典的key dic[i]是字典的value
print(dic9)
print('----------------------------------------8-1 字典推导式 key和value对调')

#需求2 将列表1的元素作为key，列表2的元素作为value
li1 = ['jack','tom']
li2 = [1,2]
dic82 = {li1[i]:li2[i] for i in range(len(li1))}
#这里 li1[i]是字典的key  li2[i]是字典的value
# for i in range(len(li1)  #根据列表的索引号来取值
print(dic82)  #{'jack': 1, 'tom': 2}




















