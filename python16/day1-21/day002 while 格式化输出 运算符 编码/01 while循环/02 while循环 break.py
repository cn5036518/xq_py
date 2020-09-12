#!/usr/bin/env python
#-*- coding:utf-8 -*-

# while True:
#     s1 = input("请输入你要说的话，输入Q，就结束:")
#     print(s1)
#     if s1 == "Q":
#         # exit(0)  #退出整个程序  exit(0)
#         break   #退出当前的整层循环（退出当前的while或者for循环）
#         # continue  #退出当次的循环，进入到下次的循环（当次循环后续的代码就不执行了）

# while True:
#     while True:
#         s1 = input("请输入你要说的话，输入Q，就结束:")
#         print(s1)
#         if s1 == "Q":
#             # exit(0)  #退出整个程序  exit(0)
#             break   #退出当前的整层循环（退出当前的while或者for循环）  #退出的是内层while循环，外层的while循环依旧
#     break  #退出的是外层循环，内层的while循环依旧
#            ····································

#continue的应用场景：
# 比如：记录日志的时候，出现了一条不完整的日志记录--脏数据，此时在读取日志文件的时候，读取到脏数据的时候
# 就可以用continue，跳过脏数据，继续读取下面的正常日志记录

#while--else    for---else
# count = 1
# while count<=10:
#     print(count)
#     if count == 3:
#         break  #注意：当break的时候，是退出整个循环，此时while后面的else是不执行的，for循环同理
#     count+=1
# else:  #只有当while后面的条件不成立的时候，才会执行else，比如：count=11的时候，就是条件不成立
#     print("hello")

for i in range(10):#0-9
    print(i+1)
    if i+1 == 3:
        break  #注意：当break的时候，是退出整个循环，此时for循环之外，后面的else是不执行的
else: ##只有当循环的条件不成立的时候，才会执行else，比如：i=10的时候，就是条件不成立
    print("hi")

# #in的用法，敏感词
# minganci = "金三胖"
# content = input("请输入你的评论信息：")
# if minganci in content:    #这里的in就是判断  一个字符串是否是另外一个字符串的子字符串   即：aaa是否出现在bbb中
#     print("对不起，您的评论包含敏感词")
# else:
#     print("ok")

count =1
while count<=11:
    if count==3:
        # break
        pass
    else:
        print(count)
    count += 1
else: ##只有当循环的条件不成立的时候，才会执行else，比如：i=10的时候，就是条件不成立   #如果break了，else是不执行的
    count += 1
    print(count)  #13




