#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
一、关于open函数的encoding参数
open函数中的encoding需要和文件的实际保存编码保持一致，否则会报错
1、在notepad++中，文件的实际保存编码是utf-8，这里encoding就是"utf-8"
2、在自带记事本中，文件的实际保存编码是gbk，这里encoding就是"gbk"
    (自带记事本和win10中文版操作系统的编码是一样的，gbk)

注意点：
1、open函数的encoding参数只能针对文本，对于非文本，是不存在encoding编码方式的
2、模式是r w a的时候，需要指定encoding
3、模式是rb wb ab的时候，指定encoding会报错
"""

# 1、模式是rb wb ab的时候，指定encoding会报错
# path11 = r"D:\xq_py\全栈16\day008 文件操作\ceshi4.png"
# path11 = r".\ceshi4.png"
# f = open(path11,mode="rb",encoding="utf-8")
#报错  ValueError: binary mode doesn't take an encoding argument

"""
二、相对路径
1  ./表示同级目录                         # path11 = r".\ceshi4.png"
2  ../表示当前文件所在目录的上一级目录     # path11 = r"..\ceshi4.png"
3  ../../表示当前文件所在目录的上二级目录  # path11 = r"..\..\ceshi4.png"
"""

#三 文件操作
#一、只读（不能写）
# 1 读全部或者指定大小   读全部容易出现内存爆了--不推荐
#001 文本只读
path1 = r".\2018-09-12.log"
f = open(path1,mode="r",encoding="utf-8")  #写完open之后，接着写close，养成良好习惯
content = f.read(3)  #这里的参数指定是3，表示读取3个字符（而不是字节） 在文本r模式下
content2 = f.read(3)  #读取3个字符后，光标就在第三个字符后
# 光标的移动，偏移量的单位是字节（utf-8下 一个中文字符是3个字节）
print(content)  #时间|
print(content2)  #名字|
f.close()

#002 字节只读
path1 = r".\2018-09-12.log"
# f = open(path1,mode="rb",encoding="utf-8")  #写完open之后，接着写close，养成良好习惯
#字节模式打开，不能指定encoding，否则报错
f = open(path1,mode="rb")  #写完open之后，接着写close，养成良好习惯
content = f.read(3)  #这里的参数指定是3，表示读取3个字节 在字节只读rb模式下
# 光标的移动，偏移量的单位是字节（utf-8下 一个中文字符是3个字节）
print(content)  #b'\xe6\x97\xb6'
f.close()
print("-------------1 read")

#2 读取一行
path1 = r".\2018-09-12.log"
f = open(path1,mode="r",encoding="utf-8")
content = f.readline()
content2 = f.readline()
#读取整行，包括 "\n" 字符。
print(content.strip())  #时间|名字|action  末尾有换行\n(strip可以去掉两端空白，包括换行 )
print(content2)  # 2018-09-11 00:00:01|刘伟|吃鸡
f.close()
print("-------------2 readline")

#3 读取多行到列表  读全部容易出现内存爆了--不推荐
path1 = r".\2018-09-12.log"
f = open(path1,mode="r",encoding="utf-8")
content = f.readlines()
# 3读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
print(content)
#['时间|名字|action\n', '2018-09-11 00:00:01|刘伟|吃鸡\n', '2018-09-11 00:00:02|王玉杰|打电话\n']
f.close()
print("-------------3 readlines")

#4 循环读取 ---推荐
# 这种⽅方式是最好的. 每次读取⼀行内容.不会产内存溢出的问题.
path1 = r".\2018-09-12.log"
with open(path1,mode="r",encoding="utf-8") as f:  #自动close flush
    for i in f:
        print(i.strip())  #去掉文件每行末尾的换行 \n
        # print(i,end="")  #去掉print的换行，保留文件的换行

#二 只写
#写的时候注意. 如果没有文件. 则会创建文件, 如果文件存在. 则将原件中原来的内容删除, 再写入新内容
#001 文本写
path1 = r".\002\2018-09-15.log"
with open(path1,mode="w",encoding="utf-8") as f:  #自动close flush
#写的时候，只能写，不能读
    f.write("写一行")

#002 非文本写
path1 = r".\002\2018-09-16.log"
# with open(path1,mode="wb",encoding="utf-8") as f:  #自动close flush
with open(path1,mode="wb") as f:  #自动close flush
#ValueError: binary mode doesn't take an encoding argument
#写的时候，只能写，不能读
    # f.write("写一行")  #报错 TypeError: 'str' does not support the buffer interface
    f.write("写一行".encode("utf-8"))
# wb模式下. 不能指定打开⽂件的编码. 但是在写文件的时候必须将字符串转化成utf-8的bytes数据（否则报错）

#三、只追加  (不会覆盖，会在文件末尾追加，适用于日志文件)
path1 = r".\002\2018-09-17.log"
with open(path1,mode="a",encoding="utf-8") as f:  #自动close flush
    f.write("追加模式，写一行\n")

#四、读写模式  r+ r+b  (顺序是先读后写)
path1 = r".\002\2018-09-18.log"
with open(path1, mode="r+", encoding="utf-8") as f:  # 自动close flush
    content = f.read()
    print(content)
    f.write("读写模式，写一行\n")
    # 读写模式，先把内容全部读取完后，再在文件末尾新写入内容

path1 = r".\002\2018-09-19.log"
with open(path1, mode="r+", encoding="utf-8") as f:  # 自动close flush
    content = f.read(1) #读取1个字符
    print(content)
    f.write("读写模式，写一行\n")
    # 读写模式，只要先读取了，哪怕只读取的了1个字符，再写的时候，也是在文件末尾写入内容
    #  这里并没有在光标所在处写入内容--特别注意点（忽略光标所在的情况很少，要特别记住）

path1 = r".\002\2018-09-20.log"
with open(path1, mode="r+", encoding="utf-8") as f:  # 自动close flush
    f.write("哈哈")
    content = f.read()  #
    print(content)
    # 注意点：读写模式，如果是先写后读，就是在文件开头，写入内容（写入“哈哈”2个字就会覆盖），然后在读取光标所在处的后面内容
# r+模式下. 必须是先读取. 然后再写入

#五 写读模式 w+ w+b
#先把原来的文件清空，先写入内容，写入完毕后，再从光标处就开始往下读，读取的是空
# 这个用法用的很少，了解即可
#01 正常方式，先写后读
path1 = r".\002\2018-09-21.log"
with open(path1, mode="w+", encoding="utf-8") as f:  # 自动close flush
    f.write("哈哈")
    content = f.read()  #
    print(content) #空白

#02 异常方式，先读后写 （读不到内容，写的时候，会将文件清空）
path1 = r".\002\2018-09-22.log"
with open(path1, mode="w+", encoding="utf-8") as f:  # 自动close flush
    content = f.read()  #
    print(content)  # 空白
    f.write("呵呵")

#六 追加读 a+ a+b
#不管是后读，还是先读，都是读不到内容的
#1 先追加 后读取
path1 = r".\002\2018-09-23.log"
with open(path1, mode="a+", encoding="utf-8") as f:  # 自动close flush
    f.write("呵呵2、追加\n")  #文件末尾追加（不清空）
    content = f.read()  #
    print(content)  # 空白

# 2 先读取 后追加
path1 = r".\002\2018-09-24.log"
with open(path1, mode="a+", encoding="utf-8") as f:  # 自动close flush
    content = f.read()  #
    print(content)  # 空白
    f.write("呵呵3、追加\n")  # 文件末尾追加（不清空）

"""
还有⼀一些其他的带b的操作. 就不多赘述了. 就是把字符换成字节. 仅此而已
1 不带b是针对文本，需要指定encoding
2 带b是针对非文本，不能写encoding参数，否则报错

注意点：
1、 读写模式和追加写模式，只要先读取了，哪怕只读取的了1个字符，再写的时候，也是在文件末尾写入内容
    这里并没有在光标所在处写入内容--特别注意点（忽略光标所在的情况很少，要特别记住）
2、r+ w+ a+ 用的比较少，有一些注意点

"""








