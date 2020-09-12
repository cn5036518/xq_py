#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 4,请用代码实现：
# li = ["alex", "eric", "rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
#方法1  join方法拼接
li = ["alex", "eric", "rain"]
s1 = "_".join(li)  #这里"_"是连接符，join函数的参数是列表，返回的是字符串
print(s1)  #alex_eric_rain

#方法2  算法-累加_拼接   --重点
li = ["alex", "eric", "rain"]
str1 = ""  #空字符串
for i in li:
    str1 = str1 + i + "_"  #类似累加(类似1-100累加这种)，累加拼接_
    #i第一次取值是"alex_"，第二次取值是"alex_eric_",第三次取值是"alex_eric_rain_'   #思路过程 关键点
str1 = str1[:-1]  #切片去掉最后的"_"
print(str1)  #alex_eric_rain
print("-----------4")

# 5.利用for循环和range打印出下⾯列表的索引。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)): #要重点掌握和默写
#     print(i,li[i]) #2个参数i和li[i] 默认的分隔符是空格，end参数默认是换行"\n"
    #这里的i是索引号 li[i]是根据索引号取值（取出列表的每个元素）
    #关键点：要对列表本身进行修改，必须是通过li[i]的方式才行
    #总结：从实用的角度，通过for+range(len(li)) 通过li[i]比
    # for i in li 中的i要用的多   注意
    # print(value, ..., sep=' ', end='\n')

# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插⼊到⼀个新列表中。
li = []
for i in range(101):
    if i%2 == 0: #判断是否是偶数
        li.append(i) #是偶数的话，就将偶数依次添加都空列表
# print(li)

# 7.利用for循环和range 找出50以内能被3整除的数，并将这些数插⼊到⼀个新列表中。
li1 = []
for i in range(51):
    if i%3 == 0: #如果除以3的余数是0，就是被3整除
        li1.append(i) #将被3整除的数，依次添加到空列表中
print(li1) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# 8.利用for循环和range从100~1，倒序打印。
# for i in range(100,0,-1): #和切片类似，切片的分隔符是冒号:  range的分隔符是逗号,
#     print(i,end=" ") #默认end是换行，这里改成空格

# 9. 利用for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，然
# 后对列表的元素进⾏筛选，将能被4整除的数留下来。
li = []
for i in range(100,9,-2):  #限定范围，步长是-2就限定了偶数
    if i % 4 == 0:
        li.append(i)
print(li) #[100, 96, 92, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12]
"""
注意：
1、正向思路：
    被4整除的就留下
2、反向思路：（排除）
    不被4整除的就删除（注意点：列表在循环的时候，是不能删除的，原因后面会讲到）--注意点
"""

# 10，利用for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个
# 列表，将能被3整除的数改成*。  #涉及列表的修改，就要必须用range(len(li))取索引才行--关键点
# li = []
# for i in range(1,31):
#     li.append(i)
# print(li)
#
# for i in range(len(li)):
#     if li[i]%3 == 0:
#         li[i] = "*"  #这里修改列表的元素，必须是通过索引取值才行，不通过索引取值，只修改元素i的话，对列表没有任何修改 --关键点
# print(li)

# 11，查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并
# 以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
#   #涉及列表的修改，就要必须用range(len(li))取索引才行--关键点
#方法1
li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
li1 = []

for i in range(len(li)):  #涉及列表的修改，就要必须用range(len(li))取索引才行--关键点1
    #这里不涉及对原列表的修改，是可以不用取索引的方式的
    li[i] = li[i].replace(" ","")  #注意：直接repalce并没有对原列表进行修改，必须添加赋值动作=才行   关键点2
    # print(li[i])
    if (li[i].startswith("a") or li[i].startswith("A")) and li[i].endswith("c"):
        #小括号调整优先级  注意点 先or后and（用小括号）
        li1.append(li[i])
print(li) #['TaiBai', 'alexC', 'AbC', 'egon', 'riTiAn', 'WuSir', 'aqc']
print(li1)  #['aqc']   #
print("-------------11-1")

# 11，查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并
# 以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
#   #如果涉及到原列表的修改，就要必须用range(len(li))取索引才行，这里不涉及原列表的修改，可以不用索引--关键点
#方法2  #推荐
li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
li1 = []  #空列表存放新的元素
for i in li:  #这里不涉及对原列表的修改，所以不需要用到索引  --关键点1
    i  = i.replace(" ","") #去掉所有的空格用replace，strip只能去掉中间的空格
    #注意：直接repalce并没有对原列表进行修改，必须添加赋值动作=才行   关键点2
    if (i.startswith("A") or i.startswith("a")) and i.endswith("c"):
        li1.append(i)
print(li1) #['aqc']
for i in li1:
    print(i) #aqc

# 方法3
li = ["TaiBai ", "ale xC", "AbC ", "egon", " ri TiAn", "WuSir", " aqc"]
li1 = []  # 空列表存放新的元素
for i in li:  # 这里不涉及对原列表的修改，所以不需要用到索引  --关键点1
    i = i.replace(" ", "")  # 去掉所有的空格用replace，strip只能去掉中间的空格
    # 注意：直接repalce并没有对原列表进行修改，必须添加赋值动作=才行   关键点2
    if i.upper().startswith("A")  and i.endswith("c"):  #这里和方法2有不同
        li1.append(i)
print(li1)  # ['aqc']
for i in li1:
    print(i)  # aqc
print("-------------11-3")

# # 12，开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中
# # 包含特殊的字符：
# # 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结衣"]
# # 则将用户输入的内容中的敏感词汇替换成等长度的*（苍⽼师就替换***），并添
# # 加到⼀个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# #方法1  #只实现了用户输入3个字或者5个字的时候，做了替换，但是用户输入“哈哈苍老师”就没有实现"哈哈***"的替换
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]  #直接复制pdf，可能不对，最好自己手敲一次  注意1
# li1 = []
# content = input("请输入评论内容：")
# # print("苍老师" in li)
# if content in li:
#     content = content.replace(content,"*"*len(content))
#     #注意2：对字符串的操作不会对原字符串有任何改变，replace后，需要给原字符串重新赋值  关键点
#     # print(content)
#     li1.append(content)
# else:
#     li1.append(content)
# print(li1)

# 12，开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中
# 包含特殊的字符：
# 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结衣"]
# 则将用户输入的内容中的敏感词汇替换成等长度的*（苍⽼师就替换***），并添
# 加到⼀个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# #方法2 推荐
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# li1 = []
# for i in range(10):
#     content = input("请输入评论内容，输入q退出：")
#     if content == "q":
#         break #跳出外循环
#     for i in li:
#         if i in content:
#             content = content.replace(i,"*"*len(i))
#     li1.append(content)
# print(li1) #['哈', '哈***']
# print("---------------12")

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
#方法1 推荐
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in li:#for循环遍历列表
#     if type(i) == list: #判断元素的类型是否是列表list
#         for j in i: #循环遍历子列表
#             if type(j) == str:
#                 print(j.lower()) #字符串变成小写 （int变成小写会出现报错）
#             else:
#                 print(j)
#     else: #如果元素的类型不是列表
#         if type(i) == str:
#             print(i.lower()) #字符串变成小写
#         else:
#             print(i)
# print("-------------13-1")

#方法2 不推荐（因为索引号4是写死的）
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in range(len(li)):
#     # if i != -3:  #注意：这个结果是不对的
#     if i != 4:#1 当索引号不是4的时候，就打印其余索引号的值
#         print(li[i])
#     else: #2 当索引号是4的时候，就再次循环li[4]
#         for j in li[4]:
#             print(j)
# print("-------------13-2")

# 14.
# 把班级学⽣数学考试成绩录入到⼀个列表中: 并求平均值.要求: 录入的时候
# 要带着人名录入, 例如: 张三_44
# li = []
# for i in range(10):  #限定输入次数0-9 一共是10次
#     score = input("请输入学生的姓名_数学成绩,输入完毕，请输入q:")
#     if score == "q":
#         break
#     li.append(score)
# print(li)  #['zs_33', 'lisi_44']
#方法1
li = ['zs_33', 'lisi_44']  #本来是用户输入的，这里写定义死
li1 = []
for i in li:
    # print(i)
    name,score_math = i.split("_") #将数学成绩分数存入遍历score_math,将学生姓名存入变量name
    # print(int(score_math))
    li1.append(int(score_math))  #必须把分数从字符串转换成int，后面才能求和，否则报错
    # li1.append(score_math)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(li1) #[33, 44]

def average(li1):
    print(sum(li1)/len(li1))
    #sum(li1)是对列表中的元素进行求和（平均值是和除以个数）
average(li1) #38.5
print("-------------14-1")
"""
思路1：
1、获取分数，通过拆分，将分数从字符串转换成int后，依次添加到空列表
2、计算列表中数字的和
3、计算列表中元素的个数
4、平均数= 和/元素的个数
"""

#方法2  推荐
li = ['zs_33', 'lisi_44']  #本来是用户输入的，这里先定义死
sum = 0
for i in li:
    name,score_math = i.split("_") #将数学成绩分数存入遍历score_math,将学生姓名存入变量name
    score_math = int(score_math) #转换成int
    sum = sum + score_math   #累加
print(sum) #77
print("平均成绩是:%s" % (sum/len(li)))
print("-------------14-2")
"""
思路2：
1、获取分数，通过拆分，将分数从字符串转换成int后
2、计算分数的累加  sum = sum + score_math
3、平均数 = 累加和/列表的长度（元素的个数）
"""

# 15. 敲七游戏. 从0开始数数. 遇到7或者7的倍数要在桌上敲一下(遇到7或者7的倍数，就添加"咣当"到列表). 编程来完成敲七
# 敲七和钩子钩三张（遇到j，就赢取对方三张牌）
# #方法1  有用户多次输入的交互过程
# li = []
# for i in range(100): #0-99 限定范围100下
#     num = input("请输入数字，输入q退出:") #
#     if num == "q":
#         break  #跳出整的for循环，跳出当层
#     elif int(num)%7 == 0 or "7" in num:
#         #除以7的余数是0，就是被7整除  #输入的是字符串，将字符串转换成int
#         #17中包含7，也满足要求，需要换成咣当
#         li.append("咣当")
#     else:
#         li.append(int(num))  # #输入的是字符串，将字符串转换成int
# print(li)

#方法2  #一次性输出列表-老师
# n = int(input("请输入数字n:"))  #输入的是字符串，转换成数字
# li = []
# for i in range(1,n+1):
#     if i % 7 == 0 or "7" in str(i): #如果被7整除或者字符"7"是在字符串中（例如：17 27）
#         li.append("咣当")
#     else:
#         li.append(i)
# print(li)


# 16. (升级题) 编写程序. 完成⼼动⼥⽣的筛选. (升级题)
#         首先. 程序会提示用户录入10位⼼仪⼥生的姓名. 然后把10位⼥生的名
# 字和序号展示出来. 由用户选择心动⼥生. 此时⽤户可以选择3个⼼动⼥生. 把用
# 户选中的三个⼼动⼥生的名字打印出来. 供⽤户继续选择. 这一次选择. 只能选
# 择一名⼥生. 然后输出用户的⼼动⼥生是xxx

# li = []
dic = {}
for i in range(1,4):  #限定3次输入
    name = input("请输入心仪女生的姓名:")
    # li.append((i+1,name))
    dic[i] = name   #依次给空字典添加元素
print(dic) #{1: 'zs', 2: 'ls', 3: 'ww'}

# dic = {1: 'zs', 2: 'ls', 3: 'ww'}
dic2 = {}
for j in range(2):  #限定2次输入
    choice = int(input("请输入2个心仪女生的编号:"))  #注意：这里必须把字符串转换成int，否则报错
    dic2[choice] = dic[choice]  #添加键值对到新的空字典2
print(dic2)  #{1: 'zs', 3: 'ww'}

# dic2 = {1: 'zs', 3: 'ww'}
dic3 ={}
for j in range(1):  #限定1次输入
    choice = int(input("请输入1个心仪女生的编号:"))  #注意：这里必须把字符串转换成int，否则报错
    dic3[choice] = dic2[choice]  ##添加键值对到新的空字典3
print(dic3)

"""
思路：
1、通过空字典，添加键值对的方式来实现
    编号是key，姓名是value
2、3次选择，对应3个for循环，不是嵌套的，而是平行的
    第一次输入，输入3个女生姓名
    第二次选择，从3个女生中，选择其中2个心仪女生
    第三次选择，从2个心仪女生中，选择1个心仪女生
"""















