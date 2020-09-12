#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
2，有如下文件，t1.txt,里面的内容为：

葫芦娃，葫芦娃，
一根藤上七个瓜
风吹雨打，都不怕，
啦啦啦啦。
我可以算命，而且算的特别准:
上面的内容你肯定是心里默唱出来的，对不对？哈哈

分别完成下面的功能：
a,以r+的模式打开原文件，判断原文件是否可读，是否可写。
    readable()
    writable()
b,以r的模式打开原文件，利用for循环遍历文件句柄。
c,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历readlines(),并分析b,与c 有什么区别？
   深入理解文件句柄与readlines()结果的区别。
d,以r模式读取‘葫芦娃，’前四个字符。
    read()参数是字符
    光标的参数是字节（seek()）

e,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
f,以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。
g,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。
h,截断原文件，留下内容：‘葫芦娃’
'''

# f = open('t1.txt',mode='r+',encoding='utf-8')
# print(f.readable()) #True  判断是否可读
# print(f.writable()) #True  判断是否可写
#
# s1 = f.read()
# print(s1)
# f.write("hello\n")
# f.close()
# print('-----------1 a,以r+的模式打开原文件，判断原文件是否可读，是否可写。')

# f = open('t1.txt',mode='r',encoding='utf-8')
# for i in f:  #推荐
#     print(i,end='')   #默认end='\n'  end=''去掉了空行
# f.close()
# print('-----------2 b,以r的模式打开原文件，利用for循环遍历文件句柄。')

# f = open('t1.txt',mode='r',encoding='utf-8')
# li1 = f.readlines()  #不推荐
# print(li1) #['葫芦娃，葫芦娃，\n', '一根藤上七个瓜\n', '风吹雨打，都不怕，\n', '啦啦啦啦。\n']
# for i in li1:
#     print(i,end='')  ##默认end='\n'  end=''去掉了空行
# f.close()
# print('-----------3 c,以r的模式打开原文件，利用for循环遍历文件句柄。')

'''
深入理解文件句柄与readlines()结果的区别。
1、文件句柄是一次读取一行--推荐
2、readlines（）是一次把所有的内容读取到列表，每一行作为列表的一个元素
   如果文件的内容大小大于4G，电脑的内存是4G，就会出现内存撑爆--不推荐
'''

# f = open('t1.txt',mode='r',encoding='utf-8')
# s4 = f.read(4)  #这里的参数是表示字符数，而不是字节数
# print(s4)  #葫芦娃，
# f.close()
# print('-----------4 d,以r模式读取‘葫芦娃，’前四个字符。')

# f = open('t1.txt',mode='r',encoding='utf-8')
# for i in f:
#     print(i.strip())  #strip() 去掉多余的空行
#     if i.endswith("\n"):  #当遇到第一个换行符\n的时候，就跳出整个循环
#         break
# f.close()
# print('-----------5-1 e,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。')

# f = open('t1.txt',mode='r',encoding='utf-8')
# s5 = f.readline().strip()  #读取第一行，去掉两边的空格
# print(s5)
# f.close()
# print('-----------5-2 e,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。')

# f = open('t1.txt',mode='r',encoding='utf-8')
# n =0  #计数器
# for i in f:
#     if i.endswith("\n"):  #当遇到第一个换行符\n的时候，就跳出整个循环
#         n += 1
#         if n > 2:  #从第三行开始打印
#             print(i.strip())   #strip() 去掉多余的空行
# f.close()
# print('-----------6-1 f,以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。')

# f = open('t1.txt',mode='r',encoding='utf-8')
# f.readline()   #连续读取2行，不要用seek()去数光标的字节，r模式是可以的  --关键点
# f.readline()
# s6 = f.read()
# print(s6)
# f.close()
# print('-----------6-2 f,以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。')

f = open('t1.txt',mode='a+',encoding='utf-8')
print(f.tell())  #a+模式，光标默认是在文件末尾
f.write('老男孩教育\n')  #这个是追加到文件末尾
f.seek(0)
s7 = f.read()
print(s7)
f.close()
print('-----------7 g,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。')

# f = open('t1.txt',mode='r+',encoding='utf-8')
# f.seek(9,0)  #光标移动到第9个字节后面（即第3个汉字后面）
# f.truncate()  #光标后面的内容全部截断
# f.seek(0)
# s8 = f.read()
# print(s8)
# f.close()  #葫芦娃
# print('-----------8-1 h,截断原文件，留下内容：‘葫芦娃’')

# f = open('t1.txt',mode='r+',encoding='utf-8')
# print(f.tell())   #0 光标默认在文件开头
# f.truncate(9)  #保留前9个字节（前3个汉字），之后的全部截断
# f.seek(0)
# s8 = f.read()
# print(s8)
# f.close()  #葫芦娃
# print('-----------8-2 h,截断原文件，留下内容：‘葫芦娃’')







