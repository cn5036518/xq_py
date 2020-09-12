 #!/usr/bin/env python
#-*- coding:utf-8 -*-

# fromkeys是一个类方法，应该通过类名来访问（作用是创建新的字典）
#1 基本用法--创建新的字典（
 # 普通方式是先创建空字典、然后一个个键值对添加；
 # 这个fromkeyskey一次添加多个键值对，值都是相同的，不写默认是None）
dic1 = {}
dic2 = dic1.fromkeys("jack","tom")  #参数1是可迭代对象（字符串、列表、字典），参数2不写默认是None
 # dict.fromkeys(S[, v]) -> New dict with keys from S and values equal to v.
 # v defaults to None.
 # 将参数1迭代取值后，作为k1，将参数2作为v1，依次添加到新的字典中，对原来的字典没有任何改变
print(dic1)  #{}
print(dic2)  #{'a': 'tom', 'j': 'tom', 'c': 'tom', 'k': 'tom'}

#2 重点用法
dic3 = dic1.fromkeys(["娃哈哈","爽歪歪"],[])
print(dic3)  #{'爽娃娃': [], '娃哈哈': []}
print(id(dic3["娃哈哈"]),id(dic3["爽歪歪"]))  #36175304 36175304
#这2个对象的id是相等的，说明引用的是同一个对象

dic3["娃哈哈"].append("张无忌")
"""
1、因为dic3["娃哈哈"]和dic3["爽歪歪"]对应的id是相等的，说明引用的是同一个对象
2、既然引用的是同一个对象，那么dic3["娃哈哈"]修改后，dic3["爽歪歪"]也随之修改
总结：
1、由于所有的key共用的同一个列表
2、所有修改其中一个列表，另外的列表也会随之改变
"""
print(dic3)  #{'爽歪歪': ['张无忌'], '娃哈哈': ['张无忌']}   #关键点












