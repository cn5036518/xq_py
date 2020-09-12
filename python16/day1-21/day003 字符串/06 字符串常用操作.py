#!/usr/bin/env python
#-*- coding:utf-8 -*-

#1 不可变的类型:字符串和数字
s = "太白金星"
s2 = s[::-1]  #这个例子,对字符串s进行了反转,但是反转后的字符串存在新的变量s2中了,原来的变量s没有任何改变
print(s)  #太白金星
#结论:对字符串进行操作,字符串本身是不会改变的
# 字符串是不可变的对象, 所以任何操作对原字符串是不会有任何影响的

#一 大小写转换  重点是upper()大写  忽略大小写用到(验证码,身份证号X结尾)
#1 首字母大写(将字符串中的首字母变成大写字母,注意只是首个字母大写,而不是每个单词的首字母大写)
s1 = "alex is a good man"
s2 =s1.capitalize()  #对原来的字符串进行内置方法的操作后,会产生新的字符串,原来的字符串没有任何变化
print(s2)  #Alex is a good man

#2 全部转成小写
s1 = "Alex is a Good man"
s2 = s1.lower()
print(s2)  #alex is a good man

#3 全部转成大写
s1 = "Alex is a Good man"
s2 = s1.upper()  #ALEX IS A GOOD MAN
print(s2)

#4 大小写互换
s1 = "Alex is a Good man"
s2 =s1.swapcase()
print(s2)  #aLEX IS A gOOD MAN

#应用场景  全部转成大写(小写),验证码(忽略大小写)
# while True:
#     content = input("请输入内容,输入Q退出:")
#     # if content == "Q" or content =="q":
#     if content.upper() == "Q":  #不管用户输入Q还是q,程序都会退出,忽略大小写
#         print("退出程序")
#         break
#     else:
#         print(content)

#验证码
# verify_code = "abCD"
# while True:
#     content = input("请输入验证码:")
#     # if content == "Q" or content =="q":
#     if content.upper() == verify_code.upper():  #验证码忽略大小写
#         print("验证成功")
#         break
#     else:
#         print("验证失败")

#5 全部小写
s1 = "БBß" # 分别代表俄美德3种语言的3个字符
s2 = s1.lower()  #区别是lower()对某些字符的支持不够好,但是casefold对所有的字母都有效,比如:东欧的一些字母
s3 =s1.casefold()
print(s1)  #БBß
print(s2)  #бbß
print(s3)  #бbss

#6 字符串中每个单词的首字母大写
s1 = "ale老男孩x is a go_od m1an"
s2 = s1.title()  #而capitalize只是首字母大写,而title是每个单词的首字母大写
print(s2)  #Ale老男孩X Is A Go_Od M1An
print("-----------大小写转换1")
#注意:单词的分隔符是非字母(空格\下划线\数字\中文)

#二 切来切去
#1 居中
s1 = "周杰伦"
s2 = s1.center(10,"*")  #参数1是指定字符串的长度,参数2是填充符号*,参数2默认是空格   #注意*星号 需要加上双引号
print(s2)  #***周杰伦****

#2 去掉空格    --重点2
s1 = "\t  jack tom  "  #这里的\t指的是tab-制表符
s2 = s1.strip()  #去掉字符串左右两端的空格\空白\tab(字符串中间的空格是不会去掉的),参数为空,默认是去掉左右两边的空格
print(s1)
print(s2) #jack tom

s1 = "  jack  "
s2 = s1.lstrip() #去掉字符串左边的空格
s3 = s1.rstrip() #去掉字符串右边的空格
print(s2)  #jack
print(s3) #  jack

s1 = "***jack***"
s2 = s1.strip("*")  #参数是星号*,就是去掉字符串左右两边的星号,参数为空,默认是去掉左右两边的空格
print(s2)  #jack

s7 = "abcdefgabc"
s8 = s7.strip("abc")  #指定删除字符串两边的"abc"
print(s8)  #defg
print("-----------去掉空白2")

#去掉空格的应用场景,登录,去掉用户输入的多余的空格
#场景需求:用户输入的内容是无法保证是符合规则的,需要进行处理和判断(比如去掉空格--strip())

# username = "jack"
# passwd ="111"
# for i in range(1,4):#1-3  #给3次输入机会
#     username_input = input("请输入用户名:").strip()
#     passwd_input = input("请输入密码:").strip()
#     if username_input != username or passwd_input !=passwd:
#         print("输入的用户名或者密码不对")
#     else:
#         print("登录成功")
#         break

#strip()的用法总结:可以去掉字符串左右两边的空格,也可以去掉字符串左右两边指定的字符
#参数是空,默认去掉两边的空格\空白;参数不为空-"abc",就可以去掉字符串左右两边指定的字符"abc"

#3替换 replace()
s1 = "jack tom tom bob"
s2 = s1.replace("tom","james")  #参数1是old  参数2是new  参数3不给出,默认是None,指替换所有的old
print(s2)  #jack james james bob

s1 = "jack tom tom bob"
s2 = s1.replace("tom","james",1)  #参数1是old  参数2是new 参数3是1,表示值替换左边第一次出现的old
print(s2)  #jack james tom bob

s1 = "jack tom tom tom bob"
s2 = s1.replace("tom","james",2)  #参数1是old  参数2是new 参数3是2,表示只替换左边前2次出现的old
print(s2)  #jack james james tom bob
print("-----------替换3")

#4切割 split()    将字符串变成列表
s1 = "jack tom bob"
s2 = s1.split()  #参数是空,默认是以空白（空格、tab、回车换行\r\n）作为分隔符,
# 将字符串切割成子字符串,子字符串作为列表的元素,返回的是列表
print(s2)  #['jack', 'tom', 'bob']

s1 = "jack_tom_bob"
s2 =s1.split("_") #参数是"_"作为指定的分隔符,将大字符串切割成小字符串,小字符串作为列表的元素,返回的是列表
print(s2) #['jack', 'tom', 'bob']

s1 = "jack_tom_bob"
s2 =s1.split("_",1) #参数1是"_"作为指定的分隔符,将大字符串切割成小字符串,小字符串作为列表的元素,返回的是列表
# 参数2是指最大切割次数,这里的1代表最多切割一次,即从字符串左边第一个_作为分隔符,进行切割
print(s2) #['jack', 'tom_bob']

s1 = "jack tom bob"
s2 = s1.split(" ",1)  #参数1是空格,默认是以空格作为分隔符;参数2是最大分割次数1(左边第一次出现的空格作为分隔符),
# 返回的是列表(列表的元素是切割后的字符串)
print(s2)  #['jack', 'tom bob']
print("-----------分割4-1")

s1 = "jack\ntom"  #这里的\n是换行符    应用场景:这里的\n换行符主要用于切割日志文件
s2 = s1.split("\n")  #['jack', 'tom']
print(s1)
print(s2)

s1 = """jack
tom"""  #这里三引号中的换行符号是\n
s2 = s1.split("\n")  #['jack', 'tom']
print(s1)
print(s2)   #['jack', 'tom']
print("-----------分割4-2")


#切割的子字符串(分隔符),如果是开头,或者是结尾,或者是整个字符串,会出现空字符串--异常情况
s1 = "jack tom bob"
s2 = s1.split("bob")
print(s2)  #['jack tom ', '']  #注意1:切割的内容在边上(最后面). 会出现空字符串
print("-----------分割4-3")

s1 = "jack tom bob"
s2 = s1.split("jack")
print(s2)  #['', ' tom bob']  #注意1:切割的内容在边上(最前面). 会出现空字符串
print("-----------分割4-4")

s1 = "_jack_tom_bob_"
s2 = s1.split("_")
print(s2)  #['', 'jack', 'tom', 'bob', ''] #注意1:切割的内容在边上(最前面和最后面). 会出现空字符串
print("-----------分割4-5")

s1 = " jack tom bob "
s2 = s1.split(" ")
print(s2)  #['', 'jack', 'tom', 'bob', ''] #注意1:切割的内容在边上(最前面和最后面). 会出现空字符串
print("-----------分割4-6")

s1 = " jack tom bob "
s2 = s1.split()
print(s2)  #['jack', 'tom', 'bob'] #注意1:切割的分隔符是默认的空格(split的参数是空白). 是不会出现空字符串,
# 即split()和split(" ")不一样,前者是不会出现空字符串,后者是会出现空字符串
print("-----------分割4-7")

s1 = "jack tom bob"
s2 = s1.split("jack tom bob")
print(s2)  #['', ''] #注意1:切割的分隔符是字符串本身,就会出现2个空字符串
print("-----------分割4-8")

#5 连接  将列表的元素连接成字符串(和分割对应,可逆过程)
s1 = "jack_tom_bob"
li1 =s1.split("_")  #1 将大字符串拆分成小字符串,返回列表,列表的每个元素就是小字符串
print(li1)  #['jack', 'tom', 'bob']
s3 = "_".join(li1)  #2 将列表中的元素,通过连接符连接后,拼接成大字符串
# 这里的"_"是连接符  join()的参数传入的是列表
print(s3) # "jack_tom_bob"
print("-----------连接5")

#三\格式化输出
# 的4种方式
print("我叫%s,我%s岁了,我喜欢%s" % ("alex",18,"python"))  #我叫alex,我18岁了,我喜欢python   最简洁 推荐
print("我叫{},我{}岁了,我喜欢{}".format("alex",18,"python"))
print("我叫{1},我{0}岁了,我喜欢{2}".format("alex",18,"python")) #我叫18,我alex岁了,我喜欢python
print("我叫{name},我{age}岁了,我喜欢{hobby}".format(name="alex",age=18,hobby="python"))
# 我叫alex,我18岁了,我喜欢python
print("-----------格式化输出3")

#四 查找
s1 ="jacktombob"
s2 = s1.startswith("j")  #判断字符串是否以xx开头 xx是参数
s3 = s1.startswith("ja")
print(s2)  #True
print(s3)  #True

s1 ="jacktombob"
s2 = s1.startswith("j",2,5)  #在切片范围2-4(索引号)  判断字符串是否以xx开头 xx是参数
print(s2)  #False
print("-----------startswith")

s1 ="jacktombob"
s2 = s1.endswith("b")   #判断字符串是否以xx结尾  xx是参数
s3 = s1.endswith("ob")
print(s2)  #True
print(s3)  #True

s1 ="jacktombob"
s2 = s1.endswith("b",2,5)   #在切片范围2-4(索引号),判断字符串是否以xx结尾  xx是参数
print(s2)  #False
print("---------endswith")

s1 ="jacktombob"
s2 = s1.count("b")  #统计字符b在字符串出现的次数
print(s2)  #2

s1 ="jacktombob"
s2 = s1.count("b",2,9)  #统计字符b在字符串(切片索引号是2-8之间)出现的次数
print(s2)  #1
print("---------count")

s1 ="jacktombob"
s2 =s1.find("tom")  #返回tom在字符串中的索引号4
s3 =s1.find("tom1")  #如果tom1在字符串中,查找不到,就会返回索引号-1
print(s2) #4
print(s3) #-1

s1 ="jacktombobtom"
s2 =s1.find("tom",5,13)  #切片找,就是在索引号是5-14之间,查找tom的索引号
#参数2和参数3是切片的起始索引号
print(s2) #10
print("---------find")

s1 ="jacktombob"
s2 =s1.index("tom")  #返回tom在字符串中的索引号4
# s3 =s1.index("tom1")  #返回tom1在字符串中的索引号,如果找不到,程序会报错,所以用find比index要好
#ValueError: substring not found
print(s2) #4
# print(s3)

s1 ="jacktombobtom"
s2 =s1.index("tom",5,13)  #切片找,就是在索引号是5-14之间,查找tom的索引号
#参数2和参数3是切片的起始索引号
print(s2) #10
print("---------index")



