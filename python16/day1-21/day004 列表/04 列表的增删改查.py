#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1列表的新增  append  insert   extend
li1 = []
li1.append("jack")  #在最后追加 用的最多，效率比较高
print(li1) #['jack']

li1.insert(0,"tom")  #在指定索引号之前插入元素，可能会出现列表中的元素移动（效率低于append，因为后面的所有元素都需要移动）
print(li1) #['tom', 'jack']

li1.extend("刘能") #参数必须是可迭代的类型   #注意：如果参数是字符串，就会把字符串的每个字符添加到列表中
print(li1) #['tom', 'jack', '刘', '能']

li1.extend(['刘能']) #迭代添加，将可迭代对象的元素依次添加到列表1
print(li1)  #['tom', 'jack', '刘', '能', '刘能']

li1.extend(["bob","tom"])  #可以用来合并2个列表--迭代添加
#迭代添加，将可迭代对象的元素依次添加到列表1
print(li1)  #['tom', 'jack', '刘', '能', 'bob', 'tom']
print("----------列表新增1")
"""
新增总结：
1、append追加-最常用，效率最高
    列表名.append("元素名")
2、insert在指定索引号前面，插入指定的元素，效率较低（因为后面的元素都要移动）
    列表名.insert(索引号,"元素名")
3、extend将列表2的元素合并到列表1，参数必须是可迭代对象（列表、字符串）
    参数是字符串的时候，会将字符串的每个字符一次添加到列表后面
    注意：extend支持给列表一次添加多个元素，其余append insert均不支持一次添加多个元素
    列表名.extend(列表名)
    列表名.extend(字符串名)
"""

#2 列表的删除 pop remove clear del
#删除 pop
li1 = ["jack","tom","bob","james"]
s1 = li1.pop() #参数是空白的时候，默认弹出最后一项，最后一项可以被另外一个变量接收
print(s1) #james
s2 = li1.pop()
print(s2) #bob
print(li1) #['jack', 'tom']

li1 = ["jack","tom","bob","james"]
s3 = li1.pop(-2) #参数是索引下标，弹出索引下标项，弹出项可以被另外一个变量接收(可以指定索引号删除)
# s3 = li1.pop(6) #IndexError: pop index out of range
print(s3) #bob
print(li1) #['jack', 'tom', 'james']

# li1 = []
# li1.pop()  #IndexError: pop from empty list
print("----------列表-删除2--pop1")

#删除 remove
li1 = ["jack","tom","bob","james"]
li1.remove("tom") #参数是指定的元素，将指定元素删除（和pop的区别，pop是指定索引号删除，remove是指定元素删除）
print(li1) #['jack', 'bob', 'james']

li1 = ["jack","tom","bob","tom","james"]
li1.remove("tom") #如果指定元素有多个，则删除列表中左边第一次出现的元素
print(li1) #['jack', 'bob', 'tom', 'james']

# li1.remove("fjja") #ValueError: list.remove(x): x not in list 删除不存在的元素会报错
print("----------列表-删除2--remove2")

#删除3 clear
li1 = ["jack","tom","bob","james"]
li1.clear() #将列表清空，变成空列表
print(li1) #[]
print("----------列表-删除3--clear3")

#删除4 del
li1 = ["jack","tom","bob","james"]
del li1[2] #通过索引号删除列表的元素，注意 del在最前面，是关键字，不是list的内置方法（list.是无法调出的）
print(li1) #['jack', 'tom', 'james']

li1 = ["jack","tom","bob","james"]
del li1[::2] #注意：通过索引号切片删除--一次删除多个  重要
#删除掉索引号是偶数的    del li1[1::2] #删除掉索引号是奇数的
print(li1) #['tom', 'james']
print("----------列表-删除4--del4")

# li1 = ["jack","tom","bob","james"]
# # s3 = li1.pop(0,1)  #不支持一次删除多个
# # li1.remove("jack","tom") #不支持一次删除多个
# print(li1)
"""
列表删除总结：
1 pop 默认删除最后一项，参数可以指定索引号删除元素，删除的元素可以存在另外一个变量
    列表名.pop()
    列表名.pop(-2)
2 remove 删除指定的元素（参数是元素的名子）
    列表名.remove("元素名字")
3 clear 清空列表
    列表名.clear()
4 del 关键字，而不是list的内置方法，删除一个元素（指定索引号）或者多个元素（切片删除）
    del 列表名字[索引号]
    注意：只有del可以一次删除多个元素（通过切片），其余方法均不支持一次删除多个元素
"""

#3 列表的修改
li1 = ["jack","tom","bob","james"]   #最常用
li1[2] = "jonson" #修改列表中的一个元素
print(li1) #['jack', 'tom', 'jonson', 'james']

li1 = ["jack","tom","bob","james"]  #不常用
li1[0:2]  = "jonson" #把列表中的前两个元素替换成 指定字符串的字符   注意1
print(li1) #['j', 'o', 'n', 's', 'o', 'n', 'bob', 'james']

li1 = ["jack","tom","bob","james"]  #不常用
li1[0:2]  = ["jonson"]  #把列表的前两个元素替换成 指定列表的一个元素  注意2
print(li1) #['jonson', 'bob', 'james']

li1 = ["jack","tom","bob","james"]   #不常用
li1[0:2]  = ["jonson","kevin"]  #把列表的前两个元素替换成 指定列表的2个元素
print(li1) #['jonson', 'kevin', 'bob', 'james']

li1 = ["jack","tom","bob","james"]   #不常用
# li1[0:5:2]  = ["jonson"]  #ValueError: attempt to assign sequence of size 1 to extended slice of size 2 报错
li1[0:5:2]  = ["jonson","rick"]  #如果切片步长不是1，那么指定的列表元素需要后切片后的元素个数保持相等，否则报错  注意3
print(li1) #['jonson', 'tom', 'rick', 'james']
print("----------列表-修改三")
"""
列表修改
1、一次修改一个元素      最常用
    列表名[索引号] = 元素名
2、一次修改多个元素      不常用
    注意：将新的列表名中的元素替换 目标列表中的切片元素（如果步长是默认的1，那么新的列表中的元素可以和切片后的元素个数不一致）
    列表名[start:end] = 新的列表名
    注意:如果切片步长不是1，那么新的列表中的元素必须和切片后的元素个数保持一致，否则报错
"""

#四 查询 循环遍历  列表是可迭代对象，可以通过for循环遍历-取值
li1 = ["jack","tom","bob","james"]
# for i in li1:
#     print(i)












