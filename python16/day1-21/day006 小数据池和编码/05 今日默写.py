#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 今日默写：
# 	== 和is的区别
# 	Unicode，gbk，utf-8的转化。

# 1	== 和is的区别
"""
1 ==比较的是值
2 is比较的是两个变量的内存地址，比较的是id(变量名)是否相等，如果id相等，代表2个变量引用的是同一个内存地址（同一个对应）
   即如果id(a) == id(b) 则a is b返回的是True

# 二 	Unicode，gbk，utf-8的转化。

ascii    8位-bit 1个字节 包含大小写英文字母、数字、特殊符号
gbk     16位-bit 2个字节 包含中文、日文、韩文、繁体中文等，兼容ascii
unicode 32位-bit 4个字节 包含全世界所有国家的文字字符
utf-8   可变长度的unicode
        英文字符  8位 1个字节byte
        欧洲字符 16位 2个字节  包括德文、法文、西班牙文、拉丁文等
        中文字符 24位 3个字节

unicode内存中使用  str   python3用的unicode python用的ascii
utf-8在传输和存储在硬盘使用-节约空间  bytes

1编码
unicode转成utf-8是编码过程 （编码-加密-压缩）  str--bytes(bytes是str的另外一个表示方式)
s1 = "祖国"  #看到的是unicode
b1 = s1.encode("utf-8")  #参数不写，默认是“utf-8”
print(b1)  # b开头的，每个字节都是x开头的16进制
# 在utf-8方式下，一个汉字是3个字节，2个汉字，一共第6个字节

2解码
utf-8转成unicode是解码过程 （解码-解密-解压）  bytes--str
b2 = b'\xe7\xa5\x96\xe5\x9b\xbd'
s2 =b2.decode("utf-8")  #参数不写，默认是“utf-8”
print(s2) #祖国

3编码
unicode转成gbk是编码过程 （编码-加密-压缩）  str--bytes(bytes是str的另外一个表示方式)
s1 = "祖国"
b1 = s1.encode("gbk")  #参数不写，默认是“utf-8”
print(b1)  # b开头的，每个字节都是x开头的16进制
# 在gbk方式下，一个汉字是2个字节，2个汉字，一共是4个字节

4解码
gbk转成unicode是解码过程 （解码-解密-解压）  bytes--str
b2 = b'\xe7\xa5\x96\xe5\x9b\xbd'
s2 =b2.decode("gbk")  #参数不写，默认是“utf-8”
print(s2) #祖国

#utf-8转gbk 无法直接转换，可以通过unicode中转
#01 utf-8先转成unicode

utf-8转成unicode是解码过程 （解码-解密-解压）  bytes--str
b5 = b'\xe7\xa5\x96\xe5\x9b\xbd'
s5 =b2.decode("utf-8")  #参数不写，默认是“utf-8”
print(s2) #祖国

#02 unicode再转成gbk
unicode转成gbk是编码过程 （编码-加密-压缩）  str--bytes(bytes是str的另外一个表示方式)
b6 = s5.encode("gbk")
print(b6)  #b'\xd7\xe6\xb9\xfa'

重点是掌握编码的概念， 方向验证下即可
unicode转utf-8就是编码过程   （str-bytes，明文到密文，压缩过程，encode）   （编码-加密-压缩）
#4个汉字，16字节-unicode变12字节-utf-8，就是压缩过程

utf-8转unicode就是解码过程    （bytes-str，密文到明文，解压过程，decode）  （解码-解密-解压）
#4个汉字，12字节-utf-8变16字节-unicode，就是解压过程
"""

















