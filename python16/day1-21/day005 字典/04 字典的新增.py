#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1 字典的新增
#新增方式1  用的更多，添加键值对的方式--推荐
#添加作者和书名到空字典   "吴承恩":"西游记"   "施耐庵":"水浒传"
dic1 ={}
dic1["吴承恩"] = "西游记"  #直接给字典的key-“吴承恩”赋值-"西游记"即可
dic1["施耐庵"] = "水浒传" #如果字典中不存在这个key，就是新增，存在key的话，就是替换value值
print(dic1)  #{'吴承恩': '西游记', '施耐庵': '水浒传'}

dic1["施耐庵"] = "元末明初人" #字典的key已经存在，会替换原来的value--修改
#相同的key，最后一个value值会覆盖之前的value
print(dic1) #{'施耐庵': '元末明初人', '吴承恩': '西游记'}
#新增2个key一样的键值对，后面的value会覆盖前面的value，属于修改的范畴

# 对比
li1 = ["jack","tom"]
li1[0] = "bob"
print(li1)  #['bob', 'tom']
"""
1、字典中新增键值对和修改列表的元素，写法类似
    1、字典新增键值对： dic1["吴承恩"] = "西游记"  这里的中括号中是key
    2、修改列表的元素：li1[0] = "bob"  这里的中括号中是索引号
"""

#新增方式2  setdefault
dic1.setdefault("曹雪芹")  #参数1是key，参数2是value 默认是None
dic1.setdefault("曹雪芹","红楼梦") #对于已经存在的key，不会执行value的修改
#注意：如果key相同，后面的value是不会覆盖之前的value  和新增方式1添加键值对是不同的   --关键点1

ret1 =dic1.setdefault("罗贯中","三国演义")  #参数1是key，参数2是value，如果不写，默认就是None
print(ret1)  #三国演义   返回value
# （# 类似pop的用法，删除并获取；setdefault是添加key-value并获取value）
dic1.setdefault("吴敬梓","儒林外史")  #参数1是key，参数2是value，如果不写，默认就是None
print(dic1)  #
#{'吴承恩': '西游记', '罗贯中': '三国演义', '曹雪芹': None, '吴敬梓': '儒林外史', '施耐庵': '元末明初人'}

"""
总结：
1、字典的新增
    方式1：dic1[key]=value  --用的多，推荐  （写法和修改列表的元素有类似）  li1[索引号]=value
    方式2：dic1.setdefault(key,[value=None])
上述2个方式的不同点：
方式1: 相同的key，后面的value会替换前面的value
方式2：相同的key，后面的value不会替换前面的value

"""






