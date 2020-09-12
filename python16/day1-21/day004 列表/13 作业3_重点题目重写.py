#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2)将列表中的数字3变成字符串"100"（⽤两种⽅式）。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

#方法1
lis[3][2][1][-2]  = "100"
lis[1] ="100"
print(lis)  #[2, '100', 'k', ['qwe', 20, ['k1', ['tt', '100', '1']], 89], 'ab', 'adv']

#方法2
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][-2] = str(lis[3][2][1][-2]+97)
lis[1] = str(lis[1]+97)
print(lis) #[2, '100', 'k', ['qwe', 20, ['k1', ['tt', '100', '1']], 89], 'ab', 'adv']

#方法3  递归  --推荐
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
def forcase1(lis):
    for i in range(len(lis)):  #通过索引号的方式遍历列表
        if type(lis[i]) == list: #1 如果元素的类型是列表
            forcase1(lis[i])  #就递归，自己调用自己，参数是lis[i]
        else: #2 如果元素的类型不是列表
            if lis[i] == 3: #3判断元素的值是否是3，是的话，修改成"100"
                lis[i] = "100" #这里对lis[i]的重新赋值，就对原列表本身进行了修改
forcase1(lis) #调用函数，传入参数
print(lis)  #[2, '100', 'k', ['qwe', 20, ['k1', ['tt', '100', '1']], 89], 'ab', 'adv']
print("----------1")

# 4,请用代码实现：
# li = ["alex", "eric", "rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
#方法1  join方法
li = ["alex", "eric", "rain"]
s1 = "_".join(li)  #"_"是连接符号  参数是列表  返回的是字符串   目的：将列表的元素拼接成字符串
print(s1)  #alex_eric_rain

#方法2  累加拼接的算法(和1-100累加类似)
li = ["alex", "eric", "rain"]
s1 = "" #空字符串，用来拼接后，接收最后的结果
for i in li:
    s1 = s1+i+"_"
    #第一次取值 s1是"alex_",第二次取值s1是"alex_eric_",第三次取值s1是"alex_eric_rain_"
s1 = s1[:-1] #去掉最后多余的"_"
print(s1) #alex_eric_rain
print("--------------2")

# 12，开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中
# 包含特殊的字符：
# 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍⽼师就替换***），并添
# 加到⼀个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
#方法1  #只能是输入3个字或者5个字，才会做敏感词处理，例如：输入“哈哈苍老师”就没有做敏感词处理
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# li1 = []
# content = input("请输入评论：")
# if content in li:
#     content = content.replace(content,"*"*len(content))
#     #字符串的replace方法，并没有修改原字符串  #关键点
#     li1.append(content)
# else:
#     li1.append(content)
# print(li1)

#方法2  推荐
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
li1 = [] #空列表，用来存放用户输入内容的
for i in range(10):  #限定次数 10次
    content = input("请输入评论,输入q退出:")
    if content.upper() == "Q":
        break
    for i in li: #遍历敏感词
        if i in content: #判断敏感词是否在输入的内容中
            content = content.replace(content,"*"*len(content))
            #字符串的replace方法，并没有修改原字符串  #关键点1
    li1.append(content)  #这个不能写在内循环中，而应该写在外循环中，否则会出现每个元素添加四次的情况  关键点2
print(li1)
print("--------------3")

# 13，有如下列列表
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它⾥面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7,
# 8
# "taibai"
# 5
# ritian
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in li:
#     if type(i) == list:
#         for j in i:
#             if type(j) == str:
#                 print(j.lower())
#             else:
#                 print(j)
#     else:
#         if type(i) == str:
#             print(i.lower())
#         else:
#             print(i)
print("--------------4")

# 14 把班级学⽣数学考试成绩录入到⼀个列表中: 并求平均值.要求: 录入的时候
# 要带着人名录入, 例如: 张三_44
li = ["张三_33","李四_55"]
sum = 0
for i in li:
    name,score = i.split("_") #拆分
    score = int(score)  #分数需要从字符串转换成整数int
    sum = sum + score #累加
    #sum第一次取值是33，第二次取值是33+55
average_score = sum/len(li)
print(average_score) #44.0

# 15. 敲七游戏. 从0开始数数. 遇到7或者7的倍数要在桌上敲一下(遇到7或者7的倍数，就添加"咣当"到列表). 编程来完成敲七
# 敲七和钩子钩三张（遇到j，就赢取对方三张牌）
#方法1 3次交互输入
# li1 = []
# for i in range(10):#限定10次输入
#     num = input("请输入一个数，输入q退出游戏：") #输入的是字符串
#     if num.upper() == "Q":
#         break
#     if int(num)%7 == 0 or "7" in num:
#         li1.append("咣当")
#     else:
#         li1.append(num)
# print(li1)

#方法2 一次输出
# li1 = []
# n = input("请输入一个数n:") #输入的是字符串
# n = int(n)
# for i in range(1,n+1):
#     if i % 7 == 0 or "7" in str(i):
#         li1.append("咣当")
#     else:
#         li1.append(i)
# print(li1)  #[1, 2, 3, 4, 5, 6, '咣当', 8, 9, 10, 11, 12, 13, '咣当', 15, 16, '咣当', 18]






