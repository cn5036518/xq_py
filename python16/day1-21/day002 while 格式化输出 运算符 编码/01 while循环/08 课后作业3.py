#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 9.输出 1-100 内的所有偶数
#while写法
# count=1
# while count<=100:
#     count+=1
#     if count%2==1:
#         continue
#     print(count)

#for写法
# for i in range(100):  #0-99
#     # print(i+1)  #1-100
#     if (i+1)%2 == 1:   #如果除以2的余数是1，说明是奇数，就跳过continue，余下的就是偶数
#         continue
#     print(i+1)

    # 明⽇日默写代码：
    # 1.    求1 - 100    之间所有的数的和
    #1 while写法
count = 1
sum = 0  #存放最后的和--结果
while count<=100:  #2 限定范围
    # print(count)
    sum = sum + count
    # sum第一次取值0 第二次取值0+1 第三次取值0+1+2 第四次取值0+1+2+3
    count+=1  #3 自增1
print(sum)  #5050

#2 for写法
sum = 0  #存放最后的和-结果
for i in range(100):  #0-99
    # print(i+1) #1-100
    sum = sum +i+1
    #sum第一次取值0 第二次取值0+1 第三次取值0+1+2 第四次取值0+1+2+3
print(sum)  #5050

    # 2.    And or not的含义和特征
"""
1、运算顺序
    ()>not>and>or
2、and--逻辑与
    含义：必须都是True，结果才是True
    1 0是Fasle，其余的数字都是True
    2 1是True
    3 第一个数是True，就取值第二个数
    4 第一个数是False，就取值第一个数
3、or--逻辑或
    含义：只要有一个是True，结果就是True
    1 0是Fasle，其余的数字都是True
    2 1是True
    3 第一个数是True，取值第一个数
    4 第一个数是False，取值第二个数
"""

    # 3.    break    continue的含义.有什么区别
"""
1\ break 是退出当层的整个循环
    break后，while或者for循环外面的else就不执行
    else是while后面的条件不满足后，才执行，break后，else是不执行的
    02 如果是2层嵌套循环，break只能一次退出一层循环，而不能一次退出2层循环，比如退出内循环

2、continue是退出当次循环，进入到下一次循环
    应用场景：输出某范围内的奇数或者偶数
"""

# 12.用户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
# 思路：猜数，3次猜数机会，显示剩余错误次数
# #1 while写法
# result = 66
# count =1
# while count<=3:
#     # print(count)
#     result1 = input("请猜数:")
#     result1 = int(result1)  #字符串转换成整数
#     if result1>66:
#         print("猜大了,你还有%s次机会"%(3-count))
#     elif result1 <66:
#         print("猜小了,你还有%s次机会" % (3 - count))
#     else:
#         print("答对了,游戏结束")
#         break  #跳出整个循环
#     count+=1

# #2 for写法
# result = 66
# for i in range(3): #0-2
#     # pass
#     # print(i+1)  #1-3
#     guess = input("请猜数:")
#     guess = int(guess)
#     if guess > result:
#         print("猜大了,你还有%s次机会"%(3-i-1))
#     elif guess < result:
#         print("猜小了,你还有%s次机会"%(3-i-1))
#     else:
#         print("答对了,游戏结束")
#         break #跳出整个循环

# #3 while写法  用户名和密码
# user = "jack"
# passwd = "123"
# count = 1
# while count<=3:
#     user1 = input("请输入用户名:")
#     passwd1 = input("请输入密码:")
#     if user!=user1 or passwd1!=passwd1:
#         print("你输入的用户名或者密码错误,你还有%s次输入机会"%(3-count))
#     else:
#         print("输入正确,登录成功")
#         break  #退出整个循环
#     count+=1

#4 for写法  用户名和密码
user = "jack"  #先写死  这里应该是从数据库取出来的(或者至少是从文件中读取出来的)
passwd = "123"
for i in range(1,4):  #限定范围 1-3
    # print(i+1)  #1-3
    user_input = input("请输入用户名:")
    passwd_input = input("请输入密码:")
    if user!=user_input or passwd !=passwd_input:
        print("你输入的用户名或者密码错误,你还有%s次输入机会"%(3-i))
    else:
        print("输入正确,登录成功")
        break  #退出整个循环





