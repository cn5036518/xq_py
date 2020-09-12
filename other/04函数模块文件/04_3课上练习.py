#!/usr/bin/env python
#-*- coding:utf-8 -*-

#练习1：以w方式打开文件，通过write和writelines分别写入内容
#练习2：以w+方式打开文件，通过writelines一次写入两行，不关闭文件--seek(0,0)，然后读取全部文件内容
    #   因为写入2行后，光标就在文件最后，要读取全部文件前，需要将光标移到文件开头后才能读取--seek(0,0)

"""
write(str) 写入字符串
writelines(sequence) 写入列表，可以一次写入多行,通过\n换行
                     writelines(["jack\n","tom\n"])

read() 读取所有
read(7) 读取指定字符数
readline() 读取整行，包含行位的\n换行符
readlines() 将文件的每一行，作为列表的一个元素，包含行位的\n换行符
            读取所有行，变返回列表  返回 ['hello\n', 'jack\n', 'tom\n']
"""

doc1=r"D:\xq_py\04函数模块文件\log5.txt"
f=open(doc1,"w+")
str1="hello\n"
f.write(str1)   #写入字符串
li1=["jack\n","tom\n"]
f.writelines(li1)  #通过列表，一次写入多行，行末通过\n换行

f.seek(0,0)
str1_read=f.read() #读取所有
print(str1_read)

f.seek(0,0)
str2_read=f.read(7) #读取指定字符数
print(str2_read)

f.seek(0,0)
str3_readline=f.readline() #读取整行
print(str3_readline)

f.seek(0,0)
str4_readlines=f.readlines() #读取所有行到列表，列表的每一个元素就是一行，包含末尾的\n换行符
print(str4_readlines)  #['hello\n', 'jack\n', 'tom\n']

f.close()
print("==========")

#练习3 如何清空一个文件
#1 英文字符
doc2=r"D:\xq_py\04函数模块文件\log6.txt"
f=open(doc2,"w+")
str1="hello\n"
# str1="你好世界\n"
f.write(str1)   #写入字符串到文件

f.seek(0,0)  #光标回到文件开头
f.truncate(3) #参数为3，表示保留前3个字节，第四个字节及其后的字节全部删除
# f.truncate() #参数为空，从当前位置截断--删除

str1_read3=f.read(1)  #h
print(str1_read3)
f.close()

#2 中文字符
doc3=r"D:\xq_py\04函数模块文件\log7.txt"
f=open(doc3,"w+",encoding="utf-8")
# str1="hello\n"
str1="你好世界\n"
f.write(str1)   #写入字符串到文件

f.seek(0,0)  #光标回到文件开头
f.truncate(6) #你好   参数为6，表示保留前6个字节，第7个字节及其后的字节全部删除
                #这里1个汉字是3个字节
# f.truncate(1)  #会是乱码，因为一个汉字是3个字节，这里是1个字节，所以不到一个汉字
# f.truncate() #参数为空，从当前位置截断--删除
str1_read2=f.read(1)  #你  注意：这里的size表示字符数，而不是字节数
print(str1_read2)
f.close()

#3 中文-英文字符混合
doc4=r"D:\xq_py\04函数模块文件\log8.txt"
f=open(doc4,"w+",encoding="utf-8")
# str1="hello\n"
str1="hello你好世界\n"
f.write(str1)   #写入字符串到文件

# f.seek(0,0)  #光标回到文件开头
f.seek(5,0)  #光标回到文件开头，向右便宜5个字符
f.truncate(8) #hello你   参数为8，表示保留前8个字节，第9个字节及其后的字节全部删除
                #这里1个汉字是3个字节
# f.truncate(1)  #会是乱码，因为一个汉字是3个字节，这里是1个字节，所以不到一个汉字
# f.truncate() #参数为空，从光标当前位置截断--删除
str1_read2=f.read(1)  #你  注意：这里的size表示字符数，而不是字节数
print(str1_read2)
f.close()

















