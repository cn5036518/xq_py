#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
总结：
字典的增删改查
1、新增
    1直接新增键值对
    2setdefault方法

2、删除
    1、pop方法-删除指定的key，并返回对应value
    2、popitem方法-随机删除
    3、clear-清空字典
    4、del指定删除或者删除整个字典

3、修改
    1、直接修改，对已经有的key
    2、update方法，合并2个字典，key存在，就覆盖，key不存在，就新增

4、查询
    1、直接根据key查询value
    2、get方法-健壮性
    3、setdefault方法，除了新增外，还能返回新增的value
"""

# 1、新增
#     1直接新增键值对
#     2setdefault方法
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
#方式1 直接新增键值对
dic1["罗贯中"] = "三国演义"
print(dic1)  #{'曹雪芹': '石头记', '罗贯中': '三国演义', '吴承恩': '西游记'}
#dic1[key] = value #key在原字典不存在，就是新增；存在就是覆盖-修改
print("---------新增1-1")

#方式2 setdefault方法
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
ret1 = dic1.setdefault("金庸")  #参数1是key 参数2是value，不写默认是None key不存在就是新增，且返回的是None（存在变量中）
ret2 = dic1.setdefault("金庸","倚天屠龙记") #key存在，就不操作（不覆盖）
print(dic1)  #{'曹雪芹': '石头记', '吴承恩': '西游记', '金庸': None}
print(ret1)  #None
print(ret2) #None
print("---------新增1-2")

# 2、删除
#     1、pop方法-删除指定的key，并返回对应value
#     2、popitem方法-随机删除
#     3、clear-清空字典
#     4、del指定删除或者删除整个字典
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
#     1、pop方法-删除指定的key，并返回对应value
ret1 = dic1.pop("曹雪芹")
print(ret1) #石头记
print(dic1) #{'吴承恩': '西游记'}

dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
# ret1 = dic1.pop("曹雪芹1")  #KeyError: '曹雪芹1'  当没有指定参数2，就保存
ret1 = dic1.pop("曹雪芹1","曹雪芹1不存在")  #参数1是key 如果key不存在，参数2没写的话，就报错;参数2写了，就返回参数2
print(ret1) #曹雪芹1不存在
#ret1 = dic1.pop(key[,key不存在的提示])
#ret1 key存在就是返回key对应的value，key不存在，就返回参数2-友好提示
print("---------删除2-1 pop方法")

#     2、popitem方法-随机删除
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
dic1.popitem()  #随机删除一个键值对，随机不可控，用的少；并且返回已经删除的键值对
print(dic1)
print("---------删除2-2 popitem方法")

#     3、clear-清空字典  内存空间还在
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
dic1.clear()
print(dic1)  #{}
print("---------删除2-3 clear方法")

#     4、del指定删除或者删除整个字典  和pop popitem clear不同，不是内置方法
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
# del dic1["曹雪芹1"]  #KeyError: '曹雪芹1'  删除不存在的key，报错
del dic1["曹雪芹"]  #指定key进行删除，删除单个键值对
print(dic1) #{'吴承恩': '西游记'}

dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
# del dic1  #删除整个字典，回收内存空间
print(dic1) #NameError: name 'dic1' is not defined
print("---------删除2-4 del方法")

# 3、修改
#     1、直接修改，对已经有的key
#     2、update方法，合并2个字典，key存在，就覆盖，key不存在，就新增
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
#方式1 直接修改，对已经有的key
dic1["曹雪芹"] = "红楼梦"   #key不存在就是新增，key存在就是修改
print(dic1)  #{'曹雪芹': '红楼梦', '吴承恩': '西游记'}
print("---------修改3-1 直接修改")

#方式2  update方法 合并字典（类似的列表的extend 迭代添加）
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
dic2 = {'曹雪芹': '红楼梦', '罗贯中': '三国演义'}
dic1.update(dic2) #key之前不存在，就新增；key之前存在，就覆盖value
print(dic1)  #{'吴承恩': '西游记', '罗贯中': '三国演义', '曹雪芹': '红楼梦'}
print("---------修改3-2 update合并字典")

# 4、查询
#     1、直接根据key查询value
#     2、get方法-健壮性
#     3、setdefault方法，除了新增外，还能返回新增的value
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
#方式1  直接根据key查询value
print(dic1["曹雪芹"])  #石头记
#值有2种表示方式
#  1 值=value
#  2 值=dic1[key]

#方式2 get方法  和字典pop删除的写法有类似，都是key不存在，就返回参数2
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
print(dic1.get("吴承恩"))  #西游记
print(dic1.get("吴承恩1"))  #None
print(dic1.get("吴承恩1","吴承恩1不存在"))  #吴承恩1不存在
"""
查询的get方法和pop删除的写法有类似，都是key不存在，就返回参数2
不同点是：
1 get方法查询的时候，key不存在，参数2不写，默认返回None
2 pop方法删除的时候，key不存在，参数2不写，就会报错（参数2需要指定才行）
"""
print("---------查询4-2 get方法")

# 方式3 setdefault方法，除了新增外，还能返回新增的value
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}  #
ret1 = dic1.setdefault("罗贯中","三国演义") #三国演义  参数1是key 参数2是value(参数2不写默认是None)
ret2 = dic1.setdefault("施耐庵") #None   #key之前不存在，就是新增；key之前存在，就不操作（不覆盖）
ret3 = dic1.setdefault("施耐庵","水浒传") #None   #key之前不存在，就是新增；key之前存在，就不操作（不覆盖）
print(dic1)  #{'施耐庵': None, '吴承恩': '西游记', '曹雪芹': '石头记', '罗贯中': '三国演义'}
print(ret1)  #三国演义
print(ret2) #None
print(ret3) #None
#ret1 = dic1.setdefault(key[,value])
print("---------查询4-3 setdefault方法")
"""
查询小结
1、字典新增setdefault方法是key之前存在，就不操作（不覆盖）
2、字典修改update方法是key之前不存在，就新增；key存在，就覆盖
"""











