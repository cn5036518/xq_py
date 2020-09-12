#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 1)字典的增删改查。
#一、新增
#方法1  #直接新增键值对（和列表元素的修改写法有点类似）
dic1 = {}
dic1["吴承恩"] = "西游记"
dic1["曹雪芹"] = "红楼梦"  #key没有，就是新增键值对
print(dic1) #{'曹雪芹': '红楼梦', '吴承恩': '西游记'}

dic1["曹雪芹"] = "石头记"  #key已经存在，就是替换value
print(dic1) #{'曹雪芹': '石头记', '吴承恩': '西游记'}

#方法2 setdefault()
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
dic1.setdefault("施耐庵")  #参数2默认是None，参数1是key，参数2是value
print(dic1)  #{'施耐庵': None, '曹雪芹': '石头记', '吴承恩': '西游记'}
dic1.setdefault("罗贯中","三国演义") #key不存在，就是新增
print(dic1)  #{'施耐庵': None, '罗贯中': '三国演义', '曹雪芹': '石头记', '吴承恩': '西游记'}
dic1.setdefault("罗贯中","三国演义2") #key已经存在，就不操作不覆盖
print(dic1)  #{'吴承恩': '西游记', '罗贯中': '三国演义', '施耐庵': None, '曹雪芹': '石头记'}
print("---------------新增1")

"""
新增总结
1、直接新增键值对，key不存在，就是新增，key存在，就替换value
2、setdefault(key,[value])  value不写默认是None
    key不存在，就是新增，key存在，就不操作（不替换value）
"""

#二、删除
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
#方式1 pop
value1 = dic1.pop("曹雪芹")  #必须指定key，否则报错；删除指定的key对应的键值对，并返回已经删除key的value，存在另外一个变量
print(value1) #石头记
print(dic1) #{'吴承恩': '西游记'}

dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
# dic1.pop("施耐庵") #KeyError: '施耐庵 报错，删除不存在的key
value1 = dic1.pop("施耐庵","施耐庵不存在") #删除指定的key，当key不存在，就返回参数2提示
print(value1) #施耐庵不存在
print(dic1) #{'吴承恩': '西游记', '曹雪芹': '石头记'}
print("---------------删除pop2-1")

#方式2 popitem
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
value2 = dic1.popitem()  #随机删除一个键值对，不可控，用的少,并且返回已经删除的键值对
print(dic1)
print(value2)
print("---------------删除popitem2-2")

#方式3 clear
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
dic1.clear() #清空字典，但是内存空间还在
print(dic1)  #{}
print("---------------删除clear 2-3")

#方式4 del
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
del dic1["曹雪芹"]  #删除指定的key
print(dic1) #{'吴承恩': '西游记'}

#删除不存在的key，会报错
# del dic1["曹雪芹2"]  #KeyError: '曹雪芹2'

# del dic1 #删除整个字典，内存空间释放
# print(dic1) #NameError: name 'dic1' is not defined
print("---------------删除del 2-4")

"""
字典删除总结
1 pop
  1、删除指定的key，并且返回已经删除key对应的value， 存在另外一个变量
  2、如果指定的key，不存在的话，key指定参数2，就会返回参数2（友好提示），并且存在另外一个变量
     如果参数2没有指定，就会报错

2 popitem
  随机删除一个键值对，并且返回已经删除的value，参数是空，随机不可控，用的较少

3 clear
    清空字典，变成{},内存空间还在

4 del
    del dic1[key]  删除指定的key
    del dic1  删除整个字典，内存空间释放
"""

#三、修改
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
#方法1  修改单个key
dic1["曹雪芹"] = "红楼梦"  #指定key，重新赋值value
print(dic1)  #{'吴承恩': '西游记', '曹雪芹': '红楼梦'}

#方法2 update()
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
dic2 = {'曹雪芹': '红楼梦', '罗贯中': '三国演义'}
dic1.update(dic2) #把dic2中的键值对合并到dic1中
# 如果key不存在，就是新增；如果key存在，就是替换覆盖
print(dic1) #{'吴承恩': '西游记', '罗贯中': '三国演义', '曹雪芹': '红楼梦'}
print("---------------修改3")

"""
字典的修改：
1、对字典的key进行重新赋值
   dic1["曹雪芹"] = "红楼梦"  #当key不存在，就是新增
                            key是"曹雪芹" value是"红楼梦"
                            （注意：dic1[key]和value是等效的，即字典的值有2种表示方式）
                            方式1：值=value
                            方式2：值=dic1[key]
   dic1["曹雪芹"] = "石头记"  #当key已经存在，就是修改
2、通过update()内置方法
    dic1.update(dic2)
    将字典2的键值对合并到字典1，合并规则是：
    1、字典2中的key，字典1中没有的话，就是新增
    2、字典2中的key，字典1中有的话，就是覆盖修改
    总结：如果key不存在，就是新增；如果key存在，就是替换覆盖
"""

#四、查询
"""
1、直接通过key取值value--直接 用的最多
2、通过get内置方法--健壮性
3、setfefault方法
"""
#方法1 直接通过key取值
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
print(dic1["曹雪芹"]) #石头记  #通过key获取value值  #dic1[key]
#如果key不存在，会报错
# print(dic1["曹雪芹1"])  #KeyError: '曹雪芹1'
print("------------------查询4-1")

#方法2 get方法
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
print(dic1.get("吴承恩")) #西游记  1如果key存在，就返回对应的value
print(dic1.get("吴承恩1")) #None  2如果key不存在，就默认返回None（参数2不写的话）
print(dic1.get("吴承恩1","吴承恩1不存在")) #吴承恩1不存在
#3如果key不存在，就返回参数2（友好提示）
print(dic1.get("吴承恩","吴承恩111不存在")) #西游记  #4如果key存在，就返回对应的value，参数2就忽略
#小结：get用法
# dic1.get(key[,tips]) #如果key不存在，参数2不写默认是None，参数2写了，就返回提示
print("------------------查询4-2 get方法")

#方式3 setdefault方法
dic1 = {'曹雪芹': '石头记', '吴承恩': '西游记'}
ret1 = dic1.setdefault("金庸","倚天屠龙记") #参数1是key，参数2是value，如果key没有，就是新增
ret2 = dic1.setdefault("金庸") #参数2默认是None，但是key已经存在，所有不操作（不覆盖）
 # #注意：如果key已经存在，就不操作（不会覆盖） 这里和修改的update方法是不同的（update是key存在就覆盖）
ret3 = dic1.setdefault("古龙")  #参数2默认是None
print(dic1) #{'古龙': None, '吴承恩': '西游记', '曹雪芹': '石头记', '金庸': '倚天屠龙记'}
print(ret1) #倚天屠龙记  返回key对应的value  和列表和字典的pop方法类似(弹出指定值，并且获取指定值保存到变量)
print(ret2) #倚天屠龙记  返回key对应的value--这里不是None  注意
print(ret3) #None       返回key对应的value--这里是None
"""
小结：
setdefault
1、除了新增外，还能将新增的value返回保存在变量，类似列表的pop方法
2、参数1是key 参数2是value，参数2不写默认就是None
3、ret1 = dic1.setdefault(key[,value]) #这里的ret1要么是参数2value，要么是None，要么是key对应的value
"""

"""
总结：
字典的增删改查
1、新增
    1直接新增键值对
    2setdefault方法

2、删除
    1、pop方法-删除指定的key，并返回对应value
    2、popitem方法-随机删除，并返回已经删除的键值对
    3、clear-清空字典
    4、del指定删除或者删除整个字典

3、修改
    1、直接修改，对已经有的key
    2、update方法，合并2个字典，key存在，就覆盖，key不存在，就新增

4、查询
    1、直接根据key查询value
    2、get方法--健壮性，如果key不存在，就返回参数2（参数2不写就是None）
    2、setdefault方法，除了新增外，还能返回新增的value
"""











