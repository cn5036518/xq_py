#!/usr/bin/env python
#-*- coding:utf-8 -*-

#默写
# 1，将列表的增删改查不同的方法全部写出来，
# 例如：增：有三种，append：在后⾯添加。Insert按照索引添加，
# extend：迭代着添加。

#列表的增删改查
#1增加
"""
append 追加
insert 插入
extend 迭代添加
"""
li1 = ["jack","tom","bob"]
#01 append 追加
li1.append("james")  #最常用，最搞笑
print(li1) #['jack', 'tom', 'bob', 'james']

#02 insert 插入
li1 = ["jack","tom","bob"]
li1.insert(1,"james") #在索引号是1的元素前面插入元素“james” 后面的元素的位置都会发生位移，效率不高
print(li1) #['jack', 'james', 'tom', 'bob']

#03 extend 迭代添加
li1 = ["jack","tom","bob"]
li1.extend(["james","kevin"]) #参数必须是可迭代对象（列表、字符串、元组）
#将可迭代对象的元素，依次添加到列表的最后面
print(li1) #['jack', 'tom', 'bob', 'james', 'kevin']

li1 = ["jack","tom","bob"]
li1.extend("james") #将字符串的元素-字符，依次添加到列表的末尾
print(li1) #['jack', 'tom', 'bob', 'j', 'a', 'm', 'e', 's']
print("--------------1 新增")

#2 删除 pop remove clear del
#01 pop 弹出，默认删除最后一个，可以指定索引号删除
li1 = ["jack","tom","bob"]
s1 = li1.pop()
print(s1) #bob  #参数是空，默认弹出最后一个，并且可以用变量将最后一个元素保存
print(li1) #['jack', 'tom']

li1 = ["jack","tom","bob"]
s1 = li1.pop(1)
print(s1) #tom  #删除指定索引号的元素，并且可以用变量将已经删除的元素保存
print(li1) #['jack', 'bob']
print("--------------2 删除1 pop")

#02 remove
#指定元素名称后，删除
li1 = ["jack","tom","bob"]
li1.remove("jack")
print(li1) #['tom', 'bob']

li1 = ["jack","tom","bob","tom"]
li1.remove("tom") #删除从左到右，第一次出现的"tom"
print(li1) #['jack', 'bob', 'tom']
print("--------------2 删除2 remove")

#03 clear 清空列表（内存空间还在，只是列表中没有元素，空列表）
li1 = ["jack","tom","bob"]
li1.clear()
print(li1) #[]

#04 del
#删除整个列表，释放内存空间
li1 = ["jack","tom","bob"]
del li1  #和pop remove clear不同，del不是列表的方法，而是关键字
# print(li1) #NameError: name 'li1' is not defined

s1 = "jack"
del s1 #del除了可以删除列表，还可以删除字符串，元组等其他数据类型，释放内存空间
# print(s1) #NameError: name 's1' is not defined

#del可以通过索引号删除列表的元素
li1 = ["jack","tom","bob"]
del li1[1]  #删除单个元素，通过指定列表的索引号
print(li1)  #['jack', 'bob']

li1 = ["jack","tom","bob"]
del li1[::2] #切片删除，一次删除多个元素，比如：删除索引号是偶数的元素
print(li1) #['tom']
print("--------------2 删除4 del")
"""
删除总结
pop remove clear del
1、clear是清空列表，变成空列表，内存空间还在
2、remove是指定元素名称进行删除
    (从左到右，删除第一个指定名称的元素)
3、pop默认删除最后一项，也可以通过指定索引号进行删除，可以用另外一个变量将删除的元素保存
4、del和前面3个不同，del是关键字，而不是列表的方法
    del可以删除整个列表（字符串、元组等其他数据类型），释放内存空间
    del还可以通过索引号，指定删除列表的元素
    del还可以通过切片，一次删除多个列表的元素（比如：删除列表中索引号是偶数的元素）
"""

#3 修改
#01 修改单个元素 最常用
li1 = ["jack","tom","bob"]
li1[1] = "james"  #直接给指定索引号的元素重新赋值即可
print(li1) #['jack', 'james', 'bob']

#02 修改多个元素 切片修改（2种情况）--了解（比如：一次将索引号是偶数的元素都修改了）
li1 = ["jack","tom","bob"]
li1[:2] ="james"  #注意：这里是拿字符串的元素--字符（而不是字符串本身），替换前面切片的元素  #注意点1
print(li1)  #['j', 'a', 'm', 'e', 's', 'bob']

li1 = ["jack","tom","bob"]
li1[:2] = ["james"]  #注意：这里是拿列表的元素，替换前面切片的元素
# 这里切片步长默认是1，,替换前后的个数可以不相等
print(li1)  #['james', 'bob']

li1 = ["jack","tom","bob"]
# li1[::2] = ["james"] #报错 ValueError: attempt to assign sequence of size 1 to extended slice of size 2
# # 这里的步长是2，元素替换的个数必须相等
# print(li1)

li1 = ["jack","tom","bob"]
li1[::2] = ["james","kevin"]  #一次修改多个元素 #注意：这里的步长是2（不是1），元素替换的个数必须相等
print(li1) #['james', 'tom', 'kevin']
"""
修改列表
1、单个元素的修改
2、一次修改列表的多个元素（通过切片实现）
    注意：切片的步长是1，替换前后的元素个数可以不相等
          切片的步长不是1，替换前后的元素个数必须相等，否则报错

归纳：
del可以切片，一次删除多个元素（比如：删除列表中索引号是偶数的元素）
修改列表也可切片，一次修改多个元素（比如：修改列表中索引号是偶数的元素）
"""
print("--------------3 修改")

#4 查询 通过for循环遍历
li1 = ["jack","tom","bob"]
# for i in li1:  #直接遍历列表的元素
#     print(i)

for i in range(len(li1)):  #修改原列表的元素，要用到这个
    print(i,li1[i],sep=",",end=" ")  #0,jack；1,tom；2,bob；
    #print函数  sep默认是空格（分割的是参数1和参数2，这里改成逗号,），end默认是"\n"换行（这里改成空格）
















