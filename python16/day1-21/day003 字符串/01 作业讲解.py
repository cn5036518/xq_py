#!/usr/bin/env python
#-*- coding:utf-8 -*-

from random import randint    #引入随机数
from random import randrange

# 5、利利⽤用while语句句写出猜⼤大⼩小的游戏：
# 设定⼀一个理理想数字⽐比如：66，让⽤用户输⼊入数字，如果⽐比66⼤大，则显示猜测
# 的结果⼤大了了；如果⽐比66⼩小，则显示猜测的结果⼩小了了;只有等于66，显示猜测结果
# 正确，然后退出循环。

# # result = 66
# result = randint(0,10)  #这里randint返回的是0-10之间的整数,左闭右闭
# # result = randrange(0,1)  #这里的参数是左闭右开
# print(result)
# while True:
#     num = input("请猜数:")
#     num = int(num) #字符串转换成数字
#     if num > result:
#         print("猜大了")
#     elif num <result:
#         print("猜小了")
#     else:
#         print("猜对了,游戏结束")
#         break  #退出整层循环

# 6、在5题的基础上进⾏行行升级：
# 给⽤用户三次猜测机会，如果三次之内猜测对了了，则显示猜测正确，退出循
# 环，如果三次之内没有猜测正确，则⾃自动退出循环，并显示‘太笨了了你....’。

#扩展,如何每次猜完后,给出提示,缩小猜数范围
# count=1   #计数器的初始值
# result = 66
# li = []
# while count<=10:  #限定范围
#     num = input("请猜数,范围是1-100:")
#     num = int(num) #字符串转换成数字
#     li.append(num)
#     li = sorted(li)
#     if num > result:
#         if len(li) == 1:
#             print("猜大了,请猜数%s-%s,你还有%s次机会" % (1, li[-1]-1, (10 - count)))  #1
#         elif len(li) >= 2:
#             print("猜大了,请猜数%s-%s,你还有%s次机会" % (li[-2]+1, li[-1] - 1, (10 - count)))
#     elif num <result:
#         if len(li) ==1:
#             print("猜小了,请猜数%s-%s,你还有%s次机会" % (li[-1]+ 1, 100, (10 - count)))
#         elif len(li) >=2:
#             print("猜小了,请猜数%s-%s,你还有%s次机会" % (li[-1] + 1, li[-2]-1, (10 - count)))
#     else:
#         print("猜对了,游戏结束")
#         break  #退出整层循环
#     count+=1  #自增1
# else:  #这个else的执行条件是,while后面的条件不满足了,才会执行,比如count=4的时候,当break的时候,else是不执行的
#     print("太笨了,3次还没有猜对")

# count = 1  # 计数器的初始值
# result = 66
# while count <= 3:  # 限定范围
#     num = input("请猜数:")
#     num = int(num)  # 字符串转换成数字
#     if num > result:
#         print("猜大了,你还有%s次机会" % (3 - count))
#     elif num < result:
#         print("猜小了,你还有%s次机会" % (3 - count))
#     else:
#         print("猜对了,游戏结束")
#         break  # 退出整层循环
#     count += 1  # 自增1
# else:  # 这个else的执行条件是,while后面的条件不满足了,才会执行,比如count=4的时候,当break的时候,else是不执行的
#     print("太笨了,3次还没有猜对")



'''
66
20  如果猜小了, 21-100   即num+1 100
76  如果猜大了, 1-75     即1-(76-1)  1-(num-1)    [76]
70  如果猜大了, 1-69     即1-(70-1)   1-(num-1)   [70,76]

30  如果猜小了, 31-69    即(30+1) - (70-1)    num+1 li[-2]-1      [30,70,76]
50  如果猜小了, 51-69    即(50+1) - (70-1)    num+1 li[-2]-1      [30,50,70,76]
65  如果猜小了, 66-69    即(65+1) - (70-1)    num+1 li[-2]-1      [30,50,65,70,76]
68  如果猜大了, 66-67    即(65+1) - (68-1)    li[-4]+1 num-1      [30,50,65,68,70,76]
67  如果猜大了, 66-66    即(65+1) - (67-1)    li[-5]+1 num-1      [30,50,65,67,68,70,76]

'''
# lis = []
# guess_num = 66
# for i in range(1,11):
#     num = int(input("请输入你猜的数字:"))
#     lis.append(num)
#     lis = sorted(lis)
#
#     index = lis.index(num)
#     if num > guess_num:
#         if index == 0:
#             print("猜大了,请猜数%s-%s" % (1, num - 1))
#         else:
#             print("猜大了,请猜数%s-%s" % (lis[index-1]+1, num - 1))
#
#     elif num < guess_num:
#         if lis[-1] == num:
#             print("猜小了,请猜数%s-%s" % (num + 1, 100))
#         else:
#             print("猜小了,请猜数%s-%s" % (num+1, lis[index+1]-1)) #[50,60]
#     else:
#         print("猜对了")
#         break


# result = 66
# count = 1
# li = []
# while count <= 10:  # 限定猜10次
#     guess_num = input("请猜数:")
#     guess_num = int(guess_num)
#     li.append(guess_num)
#     li.sort()  # 元素排序，列表本身修改了
#     # print(li)
#     if guess_num > result:
#         if len(li) == 1:
#             print(li)
#             print("猜大了,请猜%s-%s" % (1, guess_num - 1))  # 1
#         elif len(li) >= 2:
#             print(li)
#             # if guess_num<li[-1]:
#             print("猜大了2,请猜%s-%s" % (li[li.index(guess_num) - 1] + 1, guess_num - 1))  # 1
#     elif guess_num < result:
#         if len(li) == 1:
#             print(li)
#             print("猜小了,请猜%s-%s" % (guess_num + 1, 100))  # 1
#         elif len(li) >= 2:
#             print(li)
#             print("猜小了2,请猜%s-%s" % (guess_num + 1, li[li.index(guess_num)+1 ] - 1))  # 1
#     else:
#         print("猜对了，游戏结束")
#         break



#二分查找法
lis = [3,5,6,7,2]
start = 0
end = len(lis)-1  #4

def find(lis, guess_num,start,end):
    while start < end:
        mid = (start+end)//2
        if lis[mid] == guess_num:
            print("猜对了")
            break
        elif guess_num > lis[mid] :  #说明在列表的右侧
            start=mid+1
        else:   #说明在列表的左侧
            end=mid-1

# find(lis,2,start,end)





