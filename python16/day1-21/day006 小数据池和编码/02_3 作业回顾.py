#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 5、元素分类
# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}

li= [11,22,33,44,55,66,77,88,99,90]

#方法1：空字典{}  #好理解
dic1 = {}
li1 = []  #空列表必须放在for外面，否则每次循环，就置空
li2 = []
for i in li:
    if i > 66:
        li1.append(i)
    else:
        li2.append(i)
dic1["k1"] = li1  #添加键值对到字典
dic1["k2"] = li2
print(dic1)  #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}

#方法2：字典的雏形，内嵌空列表[]   代码行数最少
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {"k1":[],"k2":[]}  #空字典的雏形，内嵌列表
for i in li:
    if i >66:
        dic1["k1"].append(i)   #字典value的的2种表示方式  方式1  value   方式2 dic1[key]
    else:
        dic1["k2"].append(i)
print(dic1)  #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}

#方法3：setdefault方法应用   推荐1
#除了新增，还有将新增的value返回的功能
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {}
for i in li:
    if i > 66:
        ret1 = dic1.setdefault("k1",[])  #新增{"k1":[]},并且将[]作为value返回，下面再append  --关键点 很巧妙
        ret1.append(i)
        #第一次取值[77],第二次取值是[77,88],依次类推
    else:
        ret2 = dic1.setdefault("k2", [])
        ret2.append(i)
        # 第一次取值[11],第二次取值是[11,22],依次类推
print(dic1)  #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}

#方法4：get方法应用  推荐2
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {}
for i in li:
    if i  >66:
        if dic1.get("k1") == None:
            dic1["k1"] = [i]  #如果"k1"这个key不存在，就添加键值对("k1",[i])  #关键点1
        else:
            dic1["k1"].append(i) #如果"k1"这个key存在，就往列表dic1["k1"]中追加元素  #关键定2
    else:
        if dic1.get("k2") == None:
            dic1["k2"] = [i]
        else:
            dic1["k2"].append(i)
print(dic1) #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}












