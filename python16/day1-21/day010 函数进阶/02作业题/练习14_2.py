#!/usr/bin/env python
#-*- coding:utf-8 -*-

# (此题有坑)下面代码打印的结果分别是_________,________,________.
# def extendList(val,list=[]):
#     	list.append(val)
#     	return list
# 	list1 = extendList(10)
# 	list2 = extendList(123,[])
# 	list3 = extendList('a')
#
# 	print('list1=%s'%list1)
# 	print('list2=%s'%list2)
# 	print('list3=%s'%list3)

# (此题有坑)下面代码打印的结果分别是_________,________,________.
def extendList(val,list=[]):#默认值在内存中只会产生一份  关键点
    list.append(val)
    return list
list1 = extendList(10)  #[10]  #list1=[10, 'a'] 这里list1和list3是同一个内存地址，取的默认值参数
list2 = extendList(123,[]) #[123]  #list2=[123] list2和list1不是同一个内存地址，覆盖了默认值参数
list3 = extendList('a') #['a'] #list3=[10, 'a']

print('list1=%s'%list1)
print('list2=%s'%list2)
print('list3=%s'%list3)
print('------------------------1')

# list1=[10, 'a']
# list2=[123]
# list3=[10, 'a']

def extendList2(val,list=[]):#默认值在内存中只会产生一份  关键点
    list.append(val)
    return list
list1 = extendList2(10)  #[10]  #list1=[10] 这里list1和list3是同一个内存地址，取的默认值参数
print('list1=%s'%list1)

list2 = extendList2(123,[]) #[123]  #list2=[123] list2和list1不是同一个内存地址，覆盖了默认值参数
print('list2=%s'%list2)

list3 = extendList2('a') #['a'] #list3=[10, 'a']  这里list1和list3是同一个内存地址，取的默认值参数
print('list3=%s'%list3)
print('------------------------2')
# list1=[10]
# list2=[123]
# list3=[10, 'a']
print(id(list1))  #39897736  list1和list3是同一个内存地址，id的值是一样的
print(id(list2))  #39897672
print(id(list3))  #39897736













