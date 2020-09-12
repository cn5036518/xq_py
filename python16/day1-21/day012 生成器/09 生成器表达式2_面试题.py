#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/7 11:25
#@author:wangtongpei

#面试题-笔试题1

def add(a, b): #计算和
    return a + b

def test(): #生成器函数
    for r_i in range(4): #0,1,2,3
        yield r_i #依次返回 0,1,2,3

g = test()  #生成器
# print(g)

# for n in [2, 10]:  #这里没有range 注意  将这循环拆分
#     g = (add(n, i) for i in g)

n =10
g = (add(n, i) for i in (add(n, i) for i in g)) #生成器表达式


# # n=2
# # g = (add(n, i) for i in g)  #生成器表达式2，产生生成器2
# n=10  #惰性机制，不到最后10，是不取值的
# # g = (add(n, i) for i in g)  #关键点  将上面的g = (add(n, i) for i in g) 代入最右边的g
# # g = (add(n, i) for i in (add(n, i) for i in g))  ##生成器表达式2，产生生成器3   #生成器表达式
# # g = (add(n, i) for i in (add(10, i) for i in g))  ##生成器表达式2，产生生成器3
# # g = (add(n, i) for i in (10,11,12,13))  ##生成器表达式2，产生生成器3
# g = (add(10, i) for i in (10,11,12,13))  ##生成器表达式2，产生生成器3
# #先看最右边的for
# # 第一步：n=10 代入右边的for  此时 g = (add(n, i) for i in (add(10, i) for i in g))
# # 第二步：i 依次取值是0,1，2,3,
# # 第三步：(add(10, i) for i in g)就是(10,11,12,13)  此时 g = (add(n, i) for i in (10,11,12,13))
# # 第四步：n=10 代入左边的for    此时 g = (add(10, i) for i in (10,11,12,13))
# # 第五步 [20,21,22,23]

print(list(g))  #[20, 21, 22, 23] #把生成器表达式2产生的生成器3，转换成列表---
# 就是将生成器表达式中for循环的结果，依次添加到空列表[]   关键点
print('----------------1')

#面试题-笔试题2

def add(a, b): #计算和
    return a + b

def test(): #生成器函数
    for r_i in range(4): #0,1,2,3
        yield r_i #依次返回 0,1,2,3

g = test()  #生成器
# print(g)

for n in [2, 10,5]:  #这里没有range 注意  将这循环拆分
    g = (add(n, i) for i in g)

n=2
g = (add(n, i) for i in g)
n=10
g = (add(n, i) for i in (add(n, i) for i in g))
n=5
g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in g)))  #生成器表达式
g = (add(n, i) for i in (add(n, i) for i in (add(5, i) for i in g)))
g = (add(n, i) for i in (add(n, i) for i in (5,6,7,8)))
g = (add(n, i) for i in (add(5, i) for i in (5,6,7,8)))
g = (add(n, i) for i in (10,11,12,13))
g = (add(5, i) for i in (10,11,12,13))
# [15,16,17,18]

print(list(g))  #[15,16,17,18] #把生成器表达式2产生的生成器3，转换成列表---
# 就是将生成器表达式中for循环的结果，依次添加到空列表[]   关键点
print('----------------2')

#面试题-笔试题3

def add(a, b): #计算和
    return a + b

def test(): #生成器函数
    for r_i in range(4): #0,1,2,3
        yield r_i #依次返回 0,1,2,3

g = test()  #生成器
# print(g)

# for n in [2, 10,5]:  #这里没有range 注意  将这循环拆分
#     g = (add(n, i) for i in g)

# n = 2
# g = (add(n, i) for i in g)
# n =10
# g = (add(n, i) for i in (add(n, i) for i in g))
n =5
g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in g)))   #生成器表达式 记录的是代码  关键点1
# g = (add(n, i) for i in (add(n, i) for i in (add(10, i) for i in g)))   #生成器表达式
# g = (add(n, i) for i in (add(n, i) for i in (10,11,12,13)))   #生成器表达式
# g = (add(n, i) for i in (add(10, i) for i in (10,11,12,13)))   #生成器表达式
# g = (add(n, i) for i in (20,21,22,23))   #生成器表达式
# g = (add(10, i) for i in (20,21,22,23))   #生成器表达式
# g = (30,31,32,33)   #生成器表达式
# [30,31,32,33]
n=10  #惰性机制, 不到最后不会拿值-取值

print(list(g))  #[15,16,17,18] #把生成器表达式2产生的生成器3，转换成列表---    在这里，生成器才开始取值（执行）  关键点2
# 就是将生成器表达式中for循环的结果，依次添加到空列表[]   关键点
print('----------------3')











