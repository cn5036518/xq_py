#!/usr/bin/env python
#-*- coding:utf-8 -*-

#4 while循环语句句基本结构？
# count=1
# while 条件：
#   代码块(循环体)
#   count+=1
#   break（跳出整个循环，当层的循环）
#   continue（跳出当次循环，进入下一次循环）
#else：  #当while后面的条件不满足的时候，执行；如果是break的话，else是不执行的（for循环类似）
    # pass

# 5、利⽤while语句写出猜⼤⼩的游戏：
# 设定一个理想数字比如：66，让⽤用户输入数字，如果比66大，则显示猜测
# 的结果⼤了；如果⽐66小，则显示猜测的结果小了;
# 只有等于66，显示猜测结果
# 正确，然后退出循环
# count = 1  #计数器
# result = 66  #预期结果
# while count<=3:  #给3次猜的机会
#     input1 = input("请输入数字：")
#     input1 = int(input1)  #字符串类型转换成整数，然后比较大小
#     if input1 > result:
#         print("大了，继续猜,还有%s次机会" % (3-count))
#     elif input1 < result:
#         print("小了，继续猜,还有%s次机会" % (3-count))
#     else:
#         print("猜对了，游戏结束")
#         break  #跳出整个循环
#     count += 1  #递增

    # 6、在5题的基础上进行升级：
    # 给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循
    # 环，如果三次之内没有猜测正确，则自动退出循环，并显示‘太笨了你....’。
count = 1  #计数器
result = 66  #预期结果
while count<=3:  #给3次猜的机会
    input1 = input("请输入数字：")
    input1 = int(input1)  #字符串类型转换成整数，然后比较大小
    if input1 > result:
        print("大了，继续猜,还有%s次机会" % (3-count))
    elif input1 < result:
        print("小了，继续猜,还有%s次机会" % (3-count))
    else:
        print("猜对了，游戏结束")
        break  #跳出整个循环
    count += 1  #递增
else:  #这个else就是while后面的条件不满足的时候，执行的，如果break，是不执行这个else的
    print("3次机会都没猜对，太笨了你")

# 7.使⽤用while循环输⼊入 1 2 3 4 5 6 8 9 10   不输出7
count=1  #计数器的初始值
while count<=10:  #限定范围  10
    print(count)
    count+=1  #自增

# 8 求1 - 100 的所有数的和  累加
# 1 while写法
count = 1
sum = 0  #存放最后的和
while count <= 100:  #限定范围
    # print(count)
    sum = sum +count
    #sum的第一次取值0+1 第二次取值0+1+2 第三次取值0+1+2+3  第四次取值0+1+2+3+4
    count+=1
print("while下",sum)  #5050

#2 for写法
sum = 0 #存放最后的和
for i in range(100): #0-99
    # print(i+1)  #1-100
    sum = sum +i+1
    # sum的第一次取值0+1 第二次取值0+1+2 第三次取值0+1+2+3  第四次取值0+1+2+3+4
print("for下",sum)  #5050

# 9.输出 1-100 内的所有奇数
# #1 while写法1
# count =1
# while count <=100:
#     print(count)  #输出奇数
#     count+=2

#1 while写法2
# count = 0  #计数器
# while count < 100: #限定范围
#       # 输出奇数
#     count += 1  #自增1
#     if count%2 == 0:  #  除以2的余数是0，就是偶数，偶数跳过continue
#         continue
#     print(count)

#2 for写法
for i in range(100):  #0-99
    pass
    i+=1
    if i%2 == 0:  #除以2的余数是0，就是偶数，偶数跳过continue,余下的就是奇数
        continue
    print(i)






