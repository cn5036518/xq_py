#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
文件IO
文件的基本操作
1、在python中你可以用file对象做大部分的文件操作
2、一般步骤为：
    1先用python内置的open()函数打开一个文件，2并创建一个file对象，3然后调用相关方法进行操作。
语法：
file_object=open(file_name[,access_mode][,buffering])
access_mode决定了打开文件的模式：只读、写入、追加等。这个参数不是必须的，默认文件访问模式是只读(r)


"""

# doc1="D:\xq_py\04函数模块文件\log.txt"   #报错-直接copy path 可能有转义符-\r\n  \t--tab等
# doc1="D:\\xq_py\\04函数模块文件\\log.txt" #正确1  双斜杠
# doc1=r"D:\xq_py\04函数模块文件\log.txt"   #正确2  路径前面加上r，表示不转义
doc1="D:/xq_py/04函数模块文件/log1.txt"    #正确3  好处是不用每次都写绝对路径，写变量名字即可
doc2="D:/xq_py/04函数模块文件/log2.txt"
doc3="D:/xq_py/04函数模块文件/log3.txt"

"""
路径注意事项：
1、避免中文路径
2、避免特殊字符路径，比如：-  中横杠
"""

f=open(doc1,"w") #写的模式创建一个文件
print("文件的名字是：",f.name)   #文件的名字是： D:/xq_py/04函数模块文件/log.txt （这里返回全路径+文件名字）
print("文件的打开模式是：",f.mode) #文件的打开模式是： w
print("文件是否关闭了：",f.closed) #文件是否关闭了： False
f.close()  #关闭文件，是否文件对象
print("文件是否关闭了：",f.closed) #文件是否关闭了： True

"""
f.name  f.mode  f.closed与f.close()的写法区别：
1、f.close(）带有小括号，是对象的内置方法，是一个动词，例如：关闭
2、f.name  f.mode  f.closed不带小括号，可以理解成对象的属性，是一个名词，例如：文件名字，文件打开方式等
3、对象名.方法名---方法后面有小括号     f.close()         --方法：动词，有小括号
   对象名.属性名---属性后面不带小括号   f.name  f.mode等  --属性：名词，无小括号
"""


#1 write写入字符串-汉字
#001   w模式，写入汉字字符串
f=open(doc1,"w",encoding="utf-8")  #如果是写入汉字到文件，第三个参数encoding="utf-8"必须添加，否则是乱码
f.write("你好，世界")  #写入1行
# f.write("hello")  #写入1行
# f.write("你好，世界1\n")  #写入2行
# f.write("你好，世界1\r\n") #写入3行
# f.write("hello")
f.close()

#002  w模式，写入英文字符串
f = open(doc3, "w", encoding="utf-8")  # 如果是写入汉字到文件，第三个参数encoding="utf-8"必须添加，否则是乱码
# f.write("你好，世界")  # 写入1行
f.write("hello")  #写入1行
# f.write("你好，世界1\n")  #写入2行
# f.write("你好，世界1\r\n") #写入3行
# f.write("hello")
f.close()

#003   wb模式 二进制模式写入
f=open(doc2,"wb")  #ValueError: binary mode doesn't take an encoding argument
# f.write("你好，世界")
# str1="hello"
str1="你好，世界2"  #写入1行
# str1="你好，世界2\n"  #写入2行
# str1="你好，世界2\r\n" #写入2行
bytes1=str1.encode(encoding="utf-8")  #字符串转换成bytes，二进制的写入，必须从str字符串类型encode转换成bytes类型才行
# f.write("hello")  #TypeError: 'str' does not support the buffer interface
f.write(bytes1)  #
f.close()

"""
一、w模式。写入汉字到文件的话，第三个参数encoding="utf-8"必须添加，否则是乱码
    r模式。读取文件中的汉字，第三个参数encoding="utf-8"必须添加，否则读取后是乱码
    如果不是读取或者写入汉字，第三个参数encoding="utf-8"就不需要添加了

二、wb模式。二进制模式写入
    rb模式 二进制模式读取
1、二进制方式下，第三个参数encoding="utf-8"不能添加，否则报错
    ValueError: binary mode doesn't take an encoding argument
2、二进制下，写入的字符串或者汉字，必须从str字符串类型encode转换成bytes类型才行
   python3.3否则报错  TypeError: 'str' does not support the buffer interface
   python3.5的报错提示不同，但是意思类似

   二进制下，读取文件中的字符串或者汉字，必须从bytes类型decode转换成字符串类型才行
3、注意：二进制方式wb创建的，必须二进制方式rb读取
        文本方式w创建的，必须文本方式r读取

三、1、只有文本方式写入或者读取汉字字符的时候，第三个参数encoding="utf-8"必须添加，否则是乱码
    2、文本方式写入或者读取英文字符的时候，第三个参数encoding="utf-8"添加或者不添加都可以的
    3、二进制方式写入或者读取英文或者汉字字符的时候，第三个参数encoding="utf-8"不能添加，否则报错
"""

#2 read读取
#001 读取英文字符串
f=open(doc3,"r+")  #r+表示可读可写
str1=f.read()
print("文件中内容是",str1) #文件中内容是 hello

#002 读取汉字字符串
f=open(doc1,"r+",encoding="utf-8")  #r+表示可读可写
#如果是读取文件中汉字，第三个参数encoding="utf-8"必须添加，否则是乱码
str1=f.read()
print("文件中内容是",str1) #文件中内容是 你好，世界

#003 读取二进制字符串（不管是英文还汉字字符串，都不能加第三个参数encoding="utf-8"，否则报错）
f=open(doc2,"rb+")  #r+表示可读可写  注意：二进制wb创建的，必须二进制rb读取
byte1=f.read()  #读取所有
str1=bytes1.decode()  #bytes类型decode转换成字符串类型
print("文件中内容是",str1) #文件中内容是 hello

print("\n=======================")
# tell seek的用法
"""
1、tell()方法 告诉你文件内的当前位置（光标所在的位置-文件指针）
    read()文件后，tell的话，光标是在文件的末尾
    注意：tell方法的返回值，用字节数来表示，一个英文字符是1个字节，一个汉字字符是3个字节

2、seek(offset[,whence])方法 改变光标所在的位置
    offset表示要移动的字节数
    whence 指定开始移动的参考位置（起点：从哪里开始向右移动？文件开头，文件结尾还是当前光标位置）
        0表示文件开始处 默认值
        1表示当前位置
        2表示文件结尾
        seek(0) 回到文件开头
        seek(0,0) 回到文件开头

3、read（[size]）--size是字符数（1个汉字字符是3个字节）
    size表示的字符数（课件上说的是字节数，不对，应该是字符数），一个英文字符是1个字节，一个汉字字符是3个字节
    如果文件中是  中国
    那么size=2的话，就是读取2个字符（就是前面2个字符-包含英文字符和中文字符）
    此时，tell的话，返回值是6个字节（一个英文字符是1个字节，一个汉字字符是3个字节）

4、truncate([size])--这里size是字节数（1个汉字字符是3个字节）
    size为空，表示从当前位置截断-删除
    size为3，表示保留前3个字节（1和英文字符是1个字节，一个汉字是3个字节），
            第四个字节及以后的字节全部删除（前提，先seek(0,0)到文件开头）

总结：
1、tell()返回字节数
2、truncate([size])  size是字节数
3、read([size])  size是字符数（1个汉字字符是3个字节）--特殊python3.3
"""

doc4="D:/xq_py/04函数模块文件/log4.txt"
f=open(doc4,"r+",encoding="utf-8")  #文件中有汉字，就需要写上参数3-encoding="utf-8"  ，否则报错
f.read() #读取文件所有的字符
positon1=f.tell()
print("当前的光标位置是",positon1)  #当前的光标位置是 6
f.seek(0,0) #回到文件开头
str1=f.read(2) #读取前面7个字符（包括英文字符和汉字字符  一个英文字符是1个字节，一个汉字字符是3个字节）

print(str1)  #中国
print("当前的光标位置是",f.tell())  #当前的光标位置是 6（这里一个汉字字符代表3个字节）
# 11=5+3+3
f.close() #关闭文件


























