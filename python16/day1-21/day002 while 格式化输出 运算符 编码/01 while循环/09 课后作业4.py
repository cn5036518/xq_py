#!/usr/bin/env python
#-*- coding:utf-8 -*-


# 14. 输入⼀个广告标语. 判断这个⼴告是否合法. 根据最新的⼴告法来判断. ⼴
# 告法内容过多. 我们就判断是否包含'最', '第⼀', '稀缺', '国家级'等字样. 如果包
# 含. 提示, ⼴告不不合法
#          例如, 1. ⽼男孩python世界第⼀.  ==> 不合法
#               2. 今年过年不收礼啊. 收礼只收脑⽩⾦.  ==> 合法
#while写法
# count=0
# while count<3:#限定范围3次
#     content = input("请输入广告内容:")
#     count += 1
#     if "最" in content or "第一" in content or "稀缺" in content or "国家级" in content:
#         print("广告不合法,比还有%s次输入机会"%(3-count))
#         continue  #跳出当次循环,进行下一次循环
#     else:
#         print("广告合法,游戏结束")
#         break  #跳出整个循环

#for写法
for i in range(1,4): #1-3
    # print(i+1)  #1-3
    content = input("请输入广告内容:")
    if "最" in content or "第一" in content or "稀缺" in content or "国家级" in content:
    # if "最"  or "第一"  or "稀缺"  or "国家级" in content:   #注意:这个写法错误,无论你输入什么,都为真
        print("广告不合法,比还有%s次输入机会" % (3 - i))
        # continue  # 跳出当次循环,进行下一次循环  #这个continue是不需要的
    else:
        print("广告合法,游戏结束")
        break  # 跳出整个循环











