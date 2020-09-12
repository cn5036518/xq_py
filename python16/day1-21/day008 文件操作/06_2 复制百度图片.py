#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests

# ret1 = requests.get("https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1561243170&di=870bf7f93e68ba10340ad6a59ae1e2e3&src=http://y3.ifengimg.com/a/2016_03/6154e935f8a0fc6.jpg")
ret1 = requests.get("http://pic.netbian.com/uploads/allimg/190619/223632-15609549928786.jpg")
#src="/uploads/allimg/190619/223632-15609549928786.jpg"   #右键图片，审查元素 前面拼接 http://pic.netbian.com
#get请求，参数是url（图片的地址）
# 扩展：爬虫

f = open("百度图片.jpg",mode="wb")  #1 新建文件，模式必须是wb，二进制模式
f.write(ret1.content) # 2 写入 get请求获取的变量的内容
f.flush() #3 刷新写的内容 （write后 经常要做的）
f.close() #4 关闭文件（有打开，必须对应的有关闭，良好习惯）















