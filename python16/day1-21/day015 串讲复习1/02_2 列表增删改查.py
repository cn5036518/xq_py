#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/10 5:59
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
列表的增删改查
方法论小结：
1、先写预期输出结果，然后运行看实际输出结果
   验证我的预期结果，注意顺序

'''
li1 = [1,2,3]
#一 增加
#1 append--追加
li1.append(4)  #追加一个元素到原列表末尾
print(li1)  #[1, 2, 3, 4]
print('----------------------1-1 增加-追加 append')

#2 insert--指定位置前插入元素
li2 = [1,2,3]
li2.insert(2,4) #把元素4插入到索引号是2的元素前面
#参数1是索引号-下标
#参数2是目标元素
print(li2)  #[1, 2, 4, 3]
print('----------------------1-2 增加-插入 insert')

#3 extend--迭代添加iterable中的元素
li3 = [1,2,3]
s1 = 'abc'
li4 = [4,5]
li3.extend(s1) #把iterable中（这里是字符串）每一个元素依次添加到原列表的末尾
#参数iterable
print(li3)  #[1, 2, 3, 'a', 'b', 'c']

li3 = [1,2,3]
li4 = [4,5]
li3.extend(li4)#把iterable中（这里是列表）每一个元素依次添加到原列表的末尾
print(li3) #[1, 2, 3, 4, 5]
print('----------------------1-3 增加-迭代添加 entend')
'''
列表-增加元素小结
1 append是末尾追加新元素--最常用
2 insert是指定位置前插入新元素
3 extend是将iterable中元素依次添加到原列表
'''

#二 删除
#1 pop
li1 = [1,2,3]
ret1 = li1.pop() #参数不写，默认删除最后一个元素
print(li1) #[1, 2]
print(ret1) #3 获取到被删除的元素
print('----------------------2-1-1 删除-删除最后一个 pop')

li1 = ['jack','tom','bob']
ret2 = li1.pop(1) #参数是索引号，删除指定索引号位置的元素
print(li1) #['jack','bob']
print(ret2) #tom 获取到被删除的元素  注意点
print('----------------------2-1-2 删除-删除指定位置 pop')

#2 remove
li2 = ['jack','tom','bob']
li2.remove('tom') #参数是列表的元素，将指定元素值从原列表中删除
print(li2)  #['jack', 'bob']
print('----------------------2-2 删除-指定元素值删除 remove')

#3 del  不仅仅是列表，字典也适用
li2 = ['jack','tom','bob']
del li2[1]  #参数是索引号 将指定索引号位置的元素删除--单个元素删除
print(li2) #['jack', 'bob']
print('----------------------2-3-1 删除-删除指定位置-单个位置元素删除 del')

li2 = ['jack','tom','bob']
del li2[1:3]  #参数是切片，将指定切片位置的元素删除--多个元素删除
print(li2) #['jack']
print('----------------------2-3-2 删除-删除指定位置-多个位置元素切片删除 del')

# s1 = 'jack'
# del s1[1]  #参数是索引号 将字符串-指定索引号位置的元素删除  会报错-不允许
# print(s1) #报错 TypeError: 'str' object doesn't support item deletion

dic1 = {'name':'jack','age':19}
del dic1['age']  #参数是key，将字典的指定key所在的键值对删除
print(dic1) #{'name':'jack'}
print('----------------------2-3-3 删除-删除指定位置键值对-字典 del')

# li3 = ['jack','tom','bob']
# # del li3  #将整个列表删除了，内存空间回收了
# print(li3) #或报错 NameError: name 'li3' is not defined
print('----------------------2-3-4 删除-删除整个列表，内存空间回收了 del')

#4 clear
li4 = ['jack','tom','bob']
li4.clear()  #将列表中的元素清空，变成空列表
print(li4) #[]
print('----------------------2-4 清空元素 clear')
'''
列表-删除元素小结
1 pop
    不带参数，默认删除列表最后一个元素，并且获取到被删除的最后一个元素
    指定参数，删除指定位置-索引号的元素，并且获取到被删除的指定位置的元素
2 remove
    参数：元素值（不是位置）
    作用：删除指定元素值
3 del
    1 参数：单个位置-索引号
      写法：del 列表(位置)
      作用：删除单个位置的元素
    2、参数：切片
      写法：del 列表(切片)
      作用：切片删除多个位置的元素
    3、参数：列表名
       写法：del 列表名
       作用：删除整个列表，回收内存空间（和清空clear是不同的）
    4、参数：字典的key
        写法：del 字典名[key]
        作用：删除字典中指定key对应的键值对
    综上，del的作用
    1、可以删除单个位置的元素
    2、可以切片删除多个元素
    3、可以删除整个列表，回收内存空间
    4、不仅是列表，也适用于字典
4 clear
    参数：为空
    写法：li1.clear()
    作用：清空列表的元素，变成空列表
         清空-列表的内存空间没有被回收（和del li1不一样）
'''

#三 修改
#1 修改单个元素
li3 = ['jack','tom','bob']
li3[1] = 'james'
print(li3) #['jack','james','bob']
print('----------------------3-1 修改单个元素')

#2 切片修改多个元素
li3 = ['jack','tom','bob']
li3[1:3] = 'james'  #字符串
#注意点：将字符串-iterable的每一个字符 修改原来的元素
#期望结果不是 ['jack','james'],而是['jack', 'j', 'a', 'm', 'e', 's']
print(li3) #['jack', 'j', 'a', 'm', 'e', 's']
print('----------------------3-2-1 切片修改多个元素')

li3 = ['jack','tom','bob']
li3[1:3] = ['james']  #列表  注意：这里是列表，而不是字符串
print(li3)  #['jack', 'james']
print('----------------------3-2-2 切片修改多个元素 2个元素改成1个元素')

li3 = ['jack','tom','bob']
li3[1:3] = ['james','kevin']
#注意点：等号右边是列表-iterable
print(li3) #['jack', 'james', 'kevin']
print('----------------------3-2-3 切片修改多个元素 2个元素改成2个元素')

li3 = ['jack','tom','bob']
li3[1:3] = ['james','kevin','lucy']
#注意点：等号右边是列表-iterable
print(li3) #['jack', 'james', 'kevin','lucy']
print('----------------------3-2-4 切片修改多个元素 2个元素改成3个元素')
print('----------------------3-2 切片修改多个元素')
'''
列表-修改元素小结
1 单个位置修改--单个元素修改
    写法：li3[1] = 'james'
    作用：指定位置-索引号进行列表单个元素的修改

2、切片多个元素修改
    1 2个元素改成1个元素
        正确写法：li3[1:3] = ['james']
        错误写法：li3[1:3] = 'james'   注意点

    2 2个元素改成2个元素
        写法：li3[1:3] = ['james','kevin']

    3 2个元素改成3个元素
        写法：li3[1:3] = ['james','kevin','lucy']
'''

#四 查询-取值
#1单个查询-单个取值--根据位置-索引号-下标
li4 = ['jack','tom','bob']
print(li4[1])  #tom
print('----------------------4-1 查询-单个取值')

#2多个查询-多个取值-切片
li4 = ['jack','tom','bob']
print(li4[1:3])  #['tom', 'bob']
print('----------------------4-2 查询-多个取值-切片')

#3全部查询-全部取值-for循环遍历
li4 = ['jack','tom','bob']
for i in li4:
    print(i)
print('----------------------4-3 查询-全部取值-for循环遍历')
'''
列表-查询元素小结
1 单个查询-单个取值-按照单个位置-索引号-下标
2 多个查询-多个取值-按照切片
3 全部查询-全部取值-for循环遍历
'''





