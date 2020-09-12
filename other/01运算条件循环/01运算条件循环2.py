#!/usr/bin/env python
#-*- coding:utf-8 -*-

#一、循环语句 while for 嵌套
#循环控制 break continue
#break是跳出整个循环，循环结束
#continue是跳出当次迭代，进入下次迭代

#1continue的用法
#01、打印1~9之间的偶数
count=0
while count<9:
    count+=1
    if count%2==1:
        continue  #当次迭代结束，进入下一个迭代，奇数就不输出了
    print("偶数",count)
print("======")

#02、打印1~9之间的奇数
count=0
while count<9:
    count+=1
    if count%2==0:  #%书取上的榆树
        continue  #当次迭代结束，进入下一个迭代，偶数就不输出了
    print("奇数",count)
print("======")

#02 break的用法
i=0
while 1:  #0或者null是false，其余非0或者非空nul都是true
    print(i)  #输出0 1 2 3
    i+=1
    if i>3:
        break #跳出整个while循环，整个循环结束
print("=======")

#03 while...else
i=0
while i<5:
    print(i,"小于5")
    i+=1
else: #这里的else是while循环结束后，才执行的； i=5的时候，就跳出整个while循环了，5就接着执行else这个
    print(i, "大于等于5")  #打印0 1 2 3 4小于5， 5大于等于5
print("======-")


#二 for循环
#1 range
for i in range(0,3): #等价于rang(3)  左闭右开
    print(i)    #打印0 1 2
print("======-for1")

#range len  li1[i]循环取出列表的元素
i=0
li1=["jack","tom","bob"]
for i in range(len(li1)):
    print(li1[i])  #遍历输出列表的所有元素
print("======--for2")

#range函数
for i in range(5):
    print(i) #01234
print("======--for3")
for i in range(1,5):
    print(i) #1234
print("======--for4")
for i in range(1,5,2):
    print(i) #1 3
print("======--for5")













