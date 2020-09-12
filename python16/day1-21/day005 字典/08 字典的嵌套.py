#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
1、for循环的嵌套--双层for循环
2、列表的嵌套，列表中含有列表（列表的元素是列表）
3、字典的嵌套，字典中含有字典（字典的元素是字典）--json串也是这样
"""

#字典的嵌套
wangfeng = {
    "name":"汪峰",
    "age":48,
    "成名曲":"春天里",
    "wife":{
        "name":"章子怡",
        "age":39,
        "职业":"演员"
    },
    "children":[
        {
            "name":"汪一",
            "age":1
        },
        {
            "name": "汪二",
            "age": 3
        }
    ]
}  #内嵌有列表

wangfeng2 = {
    "name":"汪峰",
    "age":48,
    "成名曲":"春天里",
    "wife":{
        "name":"章子怡",
        "age":39,
        "职业":"演员"
    },
    "child1":
        {
            "name":"汪一",
            "age":1
        },
    "child2":
        {
            "name": "汪二",
            "age": 3
        }
}  #内嵌没有列表，都是字典

print(wangfeng)
#{'name': '汪峰', 'age': 48,
# 'children': [{'name': '汪一', 'age': 1}, {'name': '汪二', 'age': 3}],
#  'wife': {'name': '章子怡', 'age': 39, '职业': '演员'}, '成名曲': '春天里'}

print(wangfeng["children"][1]["age"]) #3
#输出第二个孩子的年龄

print(wangfeng2)
#{'age': 48,
# 'child1': {'name': '汪一', 'age': 1},
# 'wife': {'name': '章子怡', 'age': 39, '职业': '演员'},
#  'child2': {'name': '汪二', 'age': 3}, 'name': '汪峰', '成名曲': '春天里'}

#把wangfeng的wife的年龄增加10岁
wangfeng["wife"]["age"] = wangfeng["wife"]["age"] +10  #必须重新赋值才行
print(wangfeng)
#{'age': 48, 'children': [{'age': 1, 'name': '汪一'}, {'age': 3, 'name': '汪二'}],
#  '成名曲': '春天里', 'wife': {'age': 49, '职业': '演员', 'name': '章子怡'}, 'name': '汪峰'}
print("-------------1")

#课上练习
dic1 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}
# 1，将name对应的列表追加一个元素’wusir’。
dic1["name"].append("wusir")
print(dic1) #{'oldboy': {'alex': ['python1', 'python2', 100]},
# 'name': ['alex', 2, 3, 5, 'wusir'], 'job': 'teacher'}

# 2，将name对应的列表中的alex首字母大写。
dic1 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}
dic1["name"][0] = dic1["name"][0].title()  #对字符串的方法操作，对字符串本身没有修改，必须重新赋值才行
print(dic1)

# 3，oldboy对应的字典加一个键值对’⽼男孩’,’linux’。
dic1 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}
dic1["oldboy"]["老男孩"] = "linux"
print(dic1) #{'job': 'teacher',
# 'oldboy': {'老男孩': 'linux', 'alex': ['python1', 'python2', 100]},
#  'name': ['alex', 2, 3, 5]}

dic1["oldboy"].setdefault("老男孩2","linux2") #如果key不存在就是新增，存在就不操作（不覆盖）
print(dic1) #{'job': 'teacher', 'name': ['alex', 2, 3, 5],
# 'oldboy': {'alex': ['python1', 'python2', 100], '老男孩': 'linux', '老男孩2': 'linux2'}}

# 4，将oldboy对应的字典中的alex对应的列表中的python2删除。
#方法1
dic1 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}
dic1["oldboy"]["alex"].remove("python2") #del pop
print(dic1)  #{'name': ['alex', 2, 3, 5], 'job': 'teacher', 'oldboy': {'alex': ['python1', 100]}}

#方法2
dic1 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}
dic1["oldboy"]["alex"].pop(1)
print(dic1) #{'oldboy': {'alex': ['python1', 100]}, 'job': 'teacher', 'name': ['alex', 2, 3, 5]}

#方法3
dic1 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}
del dic1["oldboy"]["alex"][1]
print(dic1) #{'oldboy': {'alex': ['python1', 100]}, 'name': ['alex', 2, 3, 5], 'job': 'teacher'}






