#!/usr/bin/env python
#-*- coding:utf-8 -*-

path1 = r".\ceshi.txt"
path2 = r"D:\xq_py\全栈16\day008 文件操作\01 今日内容大纲"   #绝对路径
path3 = r".\01 今日内容大纲"   #相对路径  点表示的当前同一级目录

#1 打开文件
f = open(path1,mode="r",encoding="utf-8")   #注意点1：只读模式，只能读，不能写write，写会报错
# f = open(path1,mode="r",encoding="gbk")
"""
# 这里path1 = r".\ceshi.txt"  是用notepad++编辑保存的，notepad++的编码是utf-8   --注意点1
# 如果把notepad++的编码方式改成GB2312，open的参数就必须改成encoding="gbk"

# 如果path1 = r".\ceshi.txt"  是用自带记事本编辑保存的，自带记事本的编码是gbk（和中文操作系统保持一致）   --注意点2
# 这时候，open的参数就必须改成encoding="gbk"

总结：
1、自带记事本编辑的文件，自带记事本编码方式是gbk（和中文操作系统一样），open的参数，encoding="gbk"
2、notepad++编辑的文件，notepad++编码方式是utf-8（可以自己设置），open的参数，encoding="utf-8"
3、open的参数，encoding不写，默认和当前中文操作系统（gbk）的保持一致

open函数中的encoding需要和文件的实际保存编码保持一致，否则会报错
1、在notepad++中，文件的实际保存编码是utf-8，这里encoding就是"utf-8"
2、在自带记事本中，文件的实际保存编码是gbk，这里encoding就是"gbk"
    (自带记事本和win10中文版操作系统的编码是一样的，gbk)

注意点：
1、open函数的encoding参数只能针对文本，对于非文本，是不存在encoding编码方式的
2、模式是r w a的时候，需要指定encoding
3、模式是rb wb ab的时候，指定encoding会报错

编码和解码
open函数打开的文件，文件存在硬盘中方式是utf-8（notepad++）或者gbk（自带记事本），为了省空间
读取后，存在f对象后，就是存在内存中了（utf-8转换成unicode  解码-解密-解压  decode("utf-8"）
读取后，存在f对象后，就是存在内存中了（gbk转换成unicode  解码-解密-解压  decode("gbk"）
"""

#path1：路径是必选参数
# 模式不写默认是r 只读
# 编码不写默认是当前操作系统的编码方式，中文操作系统的编码方式是gbk
# encoding is the name of the encoding used to decode or encode the
#     file. This should only be used in text mode. The default encoding is
#     platform dependent, but any encoding supported by Python can be
#     passed.  See the codecs module for the list of supported encodings.

#2 读取文件
# 01  读取文件全部
content = f.read()  #一次把文件的内容全部读取到内存，返回字符串
# 参数是空，默认读取文件的全部内容到内存，返回字符串
print(content)
print(type(content))  #<class 'str'>
print("--------2-1 读取全部")
"""
read()方法  全部读取的缺点  （用的比较少）
# 缺点1：读取大文件的时候，会出现内存溢出（内存爆了）  加载到内存的内容大小-30G，大于内存本身的大小-8G
# 比如：文件大小是30G，电脑内存大小是8G，就会出现内存溢出）
# 缺点2：全部读取到内存，是一个很大的字符串，不方便操作，最好是一行行读取，比较方便操作
（用的比较少）
"""

# 02  读取指定字符大小的文件
f = open(path1,mode="r",encoding="utf-8")
content = f.read(3)  #
# 参数是3，读取文件的3个字符到内存，返回字符串
print(content)  #杰克   3注意点：3个字符=2个中文字符+换行\n字符
print("--------2-2 读取指定字符的文件")

# 03 读取行
#001 读取一行
f = open(path1,mode="r",encoding="utf-8")
content1 = f.readline()  #读取第一行到内存，返回字符串，每次读取一行
content2 = f.readline()  #读取第二行到内存，返回字符串
# print(content1)  #杰克
# print(content1,end=" ")  #杰克  #将print函数的\n换行（空行）去掉，换成空格   --去掉空行 方法1
print(content1.strip())  #杰克  #通过字符串的内置函数 strip去掉两端的空白（1空格、2换行\n 3制表符tab \t） --去掉空行 方法2
print(content2)  #jack
print("--------2-3 读取文件的一行")
# 杰克
#
# jack
"""
问题：
1、读取一行的时候，为什么会有空行？  --readline方法  后面没有s
    原因是：文件的第一行 杰克 后面也有一个换行\n---第一个换行
            print本身就默认自带一个换行        ---第二个换行（空行）
    所以，杰克后面有2个换行（表现形式是：1个换行+一个空行）
"""

#002 读取多行
f = open(path1,mode="r",encoding="utf-8")
li1 = f.readlines()  #参数是空，返回的是列表，将读取内容的每一行（包括行尾的换行符\n），作为一个元素，依次添加到列表
#也是全部加载到内存（坏处：文件太大，会引起内存溢出，内存爆了）--列表中（用的比较少）
# Read and return a list of lines from the stream
print(li1)  #['杰克\n', 'jack\n', 'tom\n', 'bob\n']
print("--------2-4 读取文件的多行到列表")

#04  循环遍历整个文件
#文件是可迭代对象
f = open(path1,mode="r",encoding="utf-8")   #重点1 必须掌握
# f = open(path1,mode="r")   #重点1 必须掌握
# f = open(path1,mode="r",encoding="gbk")   #重点1 必须掌握
for i in f:  #内部其实调用的是readline()方法
    print(i,end="")   #end默认是换行\n，这里是空字符串，文件本身每行之后都有换行\n，所以要去掉print的换行，
    # 从而避免多一个空行的情况
#好处：一行一行的读取，就会避免一次读取所有内容到内存，文件太大引起内存溢出
f.close()   #关闭文件   #打开文件，处理文件完毕后，关闭文件
print("--------2-5 读取文件，循环遍历读取，一行一行读取")


"""
总结
1、open打开文件，参数1:文件路径  模式不写默认只读，编码不写默认是操作系统的编码方式（中文操作系统是gbk）
2、close关闭文件

读取文件的4种方式：
3、read读取所有内容到内存，字符串--坏处：容易引起内存溢出，用的少
4、readline一行一行读取到内存，字符串，每次读取一行
5、readlines读取所有内容，每一行包含换行符作为列表的一个元素，返回列表--坏处：容易引起内存溢出，用的少
6、循环遍历文件对象f，打印每一行，注意print函数的end=""，去掉多余空行--关键点
    内部调用的方法是readline
"""

# 3、模式是rb wb ab的时候，指定encoding会报错
# path11 = r"D:\xq_py\全栈16\day008 文件操作\ceshi4.png"
# path11 = r".\ceshi4.png"
# f = open(path11,mode="rb",encoding="utf-8")
#报错  ValueError: binary mode doesn't take an encoding argument







