#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
1 ascii： 8位-bit 1个字节-byte  英文字母（大小写）、数字、特殊字符等
2 GBK：   16位-bit 2个字节-byte 主要存中文（日文、韩文、繁体中文） 中文的特殊字符（比如：火星文）
3 unicode： 32位-bit 4个字节-byte（注意：存储和传输都用不了unicode-主要是因为unicode浪费硬盘的存储空间和带宽-流量费，
                                        unicode只用在内存中）
4 utf-8：可变长度的unicode
    英文：    8位-bit 1个字节-byte
    欧洲字符：16位-bit 2个字节-byte  比如:法文、德文、西班牙文、拉丁文等
    中文：    24位-bit 3个字节-byte

1、中文在gbk和utf-8中不能直接互换,因为：
中文一个汉字在gbk中是2个字节
中文一个汉字在utf-8中是3个字节

2、在python2中，1989年，只有ascii（那时候还没有gbk、unicode），所以默认的编码方式是ascii
              （python2程序在内存中运行的默认编码方式是ascii）
   在pythin3中，2008年，unicode是可以使用的。默认用的就是unicode
              （1  python3程序在内存中运行的默认编码方式是unicode，
                  --电脑内存目前基本是8G或者16G，内存中用unicode还是可以接受的，因为内存空间占用是临时的，经常可以回收
                  --内存中用unicode的原因：unicode是定长的，都是4个字节，32位
                     比如：计算len("alex是我们的领袖")，不管是英文字符还是汉字符都是4个字节，就很方便计算
                2  而代码是保存在py文件中，py文件用的是utf-8编码方式来存储的）
                  --py文件不是保存在内存，而是保存在电脑硬盘中
                   （如果用unicode存储-4个字节，相对utf-8存储-英文是1个字节，英文会浪费4倍存储空间；
                    硬盘空间不比内存空间，不是经常可以回收，是持久化的存储，比较浪费硬盘存储空间）

3、py文件是utf-8编码
s = "alex哈哈"  #a存储，用的是utf-8编码   但是看到的是unicode
print(s) #alex哈哈  #a输出倒控制台，在内存中用的是unicode编码

4、unicode和utf-8是可以互转的
   unicode和gbk也是可以互转的
   但是，gbk和utf-8是无法直接互转的，需要通过unicode中转才行
   类比一下：
   gbk是江苏话
   utf-8是四川话
   unicode是普通话

5、存储和传输都用不了unicode-主要是因为unicode浪费硬盘的存储空间和带宽-流量费，
    例如：01传输"abcd"如果用unicode传输，那么是16个字节-byte，而用utf8传输只是4个字节-byte
         相当于流量费是4倍，unicode下是utf-8的4倍
         02存储空间和传输类似，存储空间也是4倍，比如：utf-8存英文资料存了10G，如果换成unicode就需要存储40G
         03网络传输和数据存储都用的是utf-8,节约空间
    unicode只用在内存中

"""
# 6、编码的概念：就是把unicode转换成utf-8
s1 = "刘伟很皮" #这个在内存中是unicode方式，是16个字节；但是，传输或者存储是从unicode转换成utf-8
print(s1)  #刘伟很皮
print(s1.encode())    #传输或者存储是utf-8的方式，4个汉字是12个字节，这里b就是utf-8 bytes类型
#每个字节对应一个类似"xe5"的16进制
#b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae'
print(s1.encode("utf-8"))   #b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae'
print(s1.encode(encoding="utf-8"))   #b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae'
#参数不写，默认是utf-8编码;返回的类型是bytes
#s1是字符串类型，s1.encode()就是bytes类型
print("-----------utf-8编码1")

# 7、解码的概念：就是把utf-8转换成unicode
b1 = b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae'  #utf-8下的bytes
print(b1.decode())  #刘伟很皮
#把utf-8方式下的bytes变成字符串，参数不写，默认的解码方式是utf-8
#  unicode-utf-8是编码过程
#  unicode是明文，utf-8是密文，是加密的过程

print(b1.decode("utf-8"))  #刘伟很皮 注意点：用什么方式编码的，就用什么方式解码（类比用什么密钥加密，就用什么密钥解密）
print(b1.decode(encoding="utf-8"))  #刘伟很皮
print("-----------utf-8解码2")

"""
网络传输的过程
1、同学a想把s1 = “刘伟很皮”这个字符串传输给同学b
2、由于在内存（临时存在内存）中是unicode方式，传输和存储（永久存储在硬盘）都是utf-8方式
3、第一步：a把s1这个字符串从unicode转换成utf-8（这个过程是编码-动词）
4、第二步：s1变成b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae'    bytes类型（utf-8方式）
    传到了b，b拿到bytes类型后（utf-8）后，是读不懂的
5、第三步：b把收到的bytes类型后（utf-8）转换成unicode，就能读懂了

总结：
1、a把s1转成utf-8方式后，传递给b，b拿到utf-8形式的s1-bytes类型后，转换成unicode后，就能看明白了
2、编码的概念：从unicode转换成utf-8是编码的过程（这里编码动词 encode），utf-8是bytes形式-b开头的16进制
    4个汉字在utf-8下，bytes下是12个字节，就是12个x开头的16进制
3、解码的概念：从utf-8转换成unicode是解码的过程（解码是动词 decode）
4、内存中用的是unicode方式
    传输或者存储（永久存储在硬盘）是utf-8方式

类比：
编码过程（加密过程）：unicode转utf-8 就是把明文"刘伟很好"转成bytes b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae'
这个过程，就类似于，传输数据的时候，先把明文加密变成密文--这个加密就类比编码过程（编码是动词）

解码过程（解密过程）：utf-8转unico 就是把bytes b'\xe5\x88\x98\xe4\xbc\x9f\xe5\xbe\x88\xe7\x9a\xae' 转成明文“刘伟很好”
这个过程，就类似于，b同学接到数据的时候，先把密文解密变成密文--这个解密就类比解码过程

数据传输的过程中，1、加密，密文传输是为了数据安全
                2、编码（从unicode转成utf-8）是为了节省带宽和流量费，缩短传输时间
                  （四个汉字，16个字节变成12个字节，也相当于压缩文件）
                3、压缩：1G的文件，传输前，先打包压缩变成500M，再传输，也是为了减少流量费，缩短传输时间

bytes是str字符串的另外一种表现形式
str是在内存中，即unicode方式下--str是汉字明文
bytes是在传输或者硬盘存储中，即utf-8或者gbk方式下--bytes是字节（16进制）密文

扩展：
文本文件或者py文件，读取到内存后，都是str字符串
1、bytes除了是str字符串的另外一种表现形式
    还是电影视频、音频、图片等的另外一种表现形式
2、读取文本文件或者py文件后，读取到内存，都是str字符串
   但是电影、音频、图片读取大内存后，就不是str字符串了，而是bytes了（编码方式就不是utf-8 gbk了）

"""

#二、GBK和unicode的转换
#1 编码  就是把unicode转换成GBK
s1 = "赵瑞鑫"  #代码中看到的都是unicode
print(s1.encode("GBK"))  #GBK方式下，每个汉字是2个字节，3个汉字一共是6个字节   返回bytes类型
#b'\xd5\xd4\xc8\xf0\xf6\xce'
print(s1.encode("utf-8"))
#b'\xe8\xb5\xb5\xe7\x91\x9e\xe9\x91\xab'
print("-----------gbk编码")

#2 解码  就是把GBK转成unicode
b1 = b'\xd5\xd4\xc8\xf0\xf6\xce'  #字节类型的
print(b1.decode("GBK"))  #赵瑞鑫
# 注意点：用gbk方式编码的，就必须用GBK方式解码才行，不能gbk方式编码的，采用utf-8方式来解码
print("-----------gbk解码2")

#三、如何把gbk转换成utf-8
#思路：先把gbk转成unicode（解码-解密），然后unicode转成utf-8（编码-加密）
b1 = b'\xd5\xd4\xc8\xf0\xf6\xce'    #gbk的方式
s1 = b1.decode("GBK")
print(s1)  #赵瑞鑫  字符串是unicode  gbk转unicode（解码）  bytes-etr

b2 = s1.encode("utf-8")
print(b2)  #b'\xe8\xb5\xb5\xe7\x91\x9e\xe9\x91\xab'  #bytes  utf-8方式
#将unicode转成utf-8（编码-加密）











