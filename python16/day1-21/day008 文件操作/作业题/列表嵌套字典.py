#!/usr/bin/env python
#-*- coding:utf-8 -*-

dic1 = {'name':'jack'}
li1 = []
li1.append(dic1)
print(li1)  #[{'name': 'jack'}]

dic1['name'] = 'tom'   #修改了字典key对应的value
print(dic1)  #{'name': 'tom'}

li1.append(dic1) #再次把修改后的字典添加到列表   结果：列表中原来的字典也发生了变化   --关键点
print(li1)  #[{'name': 'tom'}, {'name': 'tom'}]

'''
小结：
列表嵌套字典（列表的元素是字典）

过程分析：
列表是 [{'name': 'jack'}]
当列表的元素-字典 变成 {'name': 'tom'}
再次往列表中增加一个元素字典 {'name': 'tom'}
列表会变成 [{'name': 'tom'}, {'name': 'tom'}] 而不是[{'name': 'jack'}, {'name': 'tom'}]

因为列表的元素字典{'name': 'jack'}已经变成了{'name': 'tom'}

即：列表的元素是字典的时候，当字典发生了变化，再次添加到列表的时候，列表中原来的字典也会随之发生变化
--关键点
'''












