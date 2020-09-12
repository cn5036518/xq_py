#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/11/9 16:02
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
三种格式化输出：
1、%s  推荐
2、format 用的很少
3、f   新的用法 py3.6以上
'''
name = 'jack'
age = 18

print('姓名是 %s,年龄是 %s' % (name,age))  #姓名是 jack,年龄是 18
print('姓名是 {name},年龄是 {age}'.format(name=name,age=age))  #format的参数是关键字参数
#姓名是 jack,年龄是 18
s3 = f"姓名是 {name},年龄是 {age}"  #这里的f是format的意思，但是不能直接写format
# 第三种写法只能在py3.6以上才能使用
# 注意点：f提示的pycharm报错，是不对的，可以忽略
print(s3)  #姓名是 jack,年龄是 18













