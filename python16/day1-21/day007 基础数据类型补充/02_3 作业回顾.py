#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 4.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量.
cars = ["鲁A 10086", "黑A 45678", "黑C 12345", "京B 00001", "京C 78912", "京A 66666"]
locations = {"鲁": "山东", "黑": "黑龙江", "京": "北京", "沪": "上海"}
# 要求输出  {"山东":1,"黑龙江":2,"北京":3}

"""
思路：
1、新建空字典dic1
2、循环遍历列表cars
3、判断如果i在dic1中不存在，--not in,get方法，setdefault方法
    i = i[0]  #获取省的简称
    k1 = locations[i]
    dic1[k1]=1 #给初始值1
4、如果1已经存在于dic1中
    dic[k1]+=1
"""
#方法1  not in   #推荐 好理解  必须掌握
dic1 = {}
for i in cars:
    i = i[0]  #1获取省的简称
    # print(i)
    k1 = locations[i]  #2根据省的简称，获取省的全称
    # print(k1)
    if k1 not in dic1:#3判断省的全称是否在空字典，不在的话，设置初始值1
        dic1[k1] = 1
    else: #省的全称已经在字典，就自增1
        dic1[k1] += 1
print(dic1)  #{'北京': 3, '黑龙江': 2, '山东': 1}

#方法2  get方法1-字典   #推荐 好理解
dic1 = {}
for i in cars:
    i = i[0]  #1获取省的简称
    # print(i)
    k1 = locations[i]  #2根据省的简称，获取省的全称
    # print(k1)
    if dic1.get(k1) == None: #3判断省的全称是否在空字典，不在的话，设置初始值1
    # if k1 not in dic1:#3判断省的全称是否在空字典，不在的话，设置初始值1
        dic1[k1] = 1
    else: #省的全称已经在字典，就自增1
        dic1[k1] += 1
print(dic1)  #{'北京': 3, '黑龙江': 2, '山东': 1}

#方法3  get方法2-字典
dic1 = {}
for i in cars:
    i = i[0]  #1获取省的简称
    k1 = locations[i]  #2根据省的简称，获取省的全称
    v1 = dic1.get(k1,0)#3判断省的全称是否在空字典，不在的话，设置初始值0
    v1 += 1  #数目自增1
    dic1[k1] = v1  #把k1（省的全称）和数目（v1），依次添加到字典
print(dic1)  #{'北京': 3, '黑龙江': 2, '山东': 1}

#方法4  get方法3-字典  最简洁 行数最少
dic1 = {}
for i in cars:
    i = i[0]  #1获取省的简称
    k1 = locations[i]  #2根据省的简称，获取省的全称
    dic1[k1] = dic1.get(k1, 0) +1 #3判断省的全称是否在空字典，不在的话，设置初始值0
    #get方法的用法：
    # 如果k1不存在，就取0,加1后作为v1
    # 如果k1存在，就取k1的值（忽略参数2 0） ,加1后作为v1   #关键点
    #把省的全称当做k1，数目当做v1，添加到空字典中
print(dic1)  #{'北京': 3, '黑龙江': 2, '山东': 1}

#方法5  setdefault方法-字典
dic1 = {}
for i in cars:
    i = i[0]  #1获取省的简称
    k1 = locations[i]  #2根据省的简称，获取省的全称
    dic1[k1] = dic1.setdefault(k1, 0) +1 #3判断省的全称是否在空字典，不在的话，设置初始值0
    #setdefault方法的用法：
    #如果k1不存在，就取value=0，进行新增键值对，返回0（加1）
    # 如果k1存在，就不操作（不覆盖，不新增），返回k1对应的value（加1）
    #把省的全称当做k1，数目当做v1，添加到空字典中
print(dic1)  #{'北京': 3, '黑龙江': 2, '山东': 1}
print("----------------------方法5")

"""
总结：
方法4和方法5，虽然简洁，但是要求对get方法和setdefault方法能够熟练掌握
1、dic1.get(key,[提示])
    好处是：如果key不存在，则默认返回None，不会报错，健壮性更好
            如果key不存在，也可以返回指定的参数2
            如果key存在，就返回对应的value值
2、dic1.setdefault(key,value)
    1、如果key已经存在了，则不执行新增
        key对应的value也保存在另外一个变量，返回--注意点
    2、如果key不存在，则执行新增键值对
        且把新增的key对应的value存在另外一个变量，返回--类似pop的获取
"""

dic = {}
for car in cars: # 每个车牌子 鲁A 10086
    paitou = car[0] # 鲁
    # if dic.get(locations[paitou]) == None:   #方法1 好理解  必须掌握
    #     dic[locations[paitou]] = 1  #1 如果key在字典不存在，设置初始值1
    # else:  #如果key在空字典已经存在，就每出现一次，就自增1
    #     dic[locations[paitou]] = dic[locations[paitou]]+1

    # 省份 # "山东": 1, "黑龙江":1   #方法2 过度方法  get方法的运用（考虑get方法的返回值）
    # num = dic.get(locations[paitou], 0) #如果key存在，就取对应的value；如果key不存在，value就是0
    # num = num + 1  #自增1
    # dic[locations[paitou]] = num  #3把省的全称作为k1，数目作为v1，添加到新的字典

    dic[locations[paitou]] = dic.setdefault(locations[paitou], 0) + 1  #方法3 最简洁
    # setdefault方法的运用（重点是setdefault方法返回值）
    #1、如果key在空字典不存在，就执行新增键值对，且返回0，k1是省的全称，v1是1，添加到空字典
    #2、如果key在空字典存在，就不操作（不覆盖，不新增），返回key对应的value（数目），数目+1后
    #    k1是省的全称，v1是数目自增1，添加到空字典（替换之前的k1，其实只是数目自增1了，key不变）
print(dic)












