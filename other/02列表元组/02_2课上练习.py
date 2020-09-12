#!/usr/bin/env python
#-*- coding:utf-8 -*-

#run的快捷键 Alt+shift+非0

#课上练习1
high=1.75
weight=80.5
BMI=weight/(high**2)
print(BMI)

if BMI<18.5:
    print("过轻")
elif BMI>=18.5 and BMI<25:
    print("正常")
elif BMI >= 25 and BMI < 28:
    print("肥胖")
else:
    print("严重肥胖")

#课上练习2
#输出元组的长度、最大值和最小值,转换成列表
tu1=(1,2,3)
print(len(tu1)) #3
print(max(tu1)) #3
print(min(tu1)) #1
print(list(tu1)) #[1, 2, 3]
















