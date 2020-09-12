#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@author: jack
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: cn5036520@163.com
@software: sign
@file: 0319-5发邮件.py
@time: 2019/1/6 6:06
@desc:
'''

"""
思路：
0、导包
    导入4个包
1、类名
    普通方法，参数列表（发件人、收件人、邮件标题、邮件正文）
2、邮件正文
3、邮件附件
    1、excel附件
    2、jpg截图附件
4、发送邮件

注意点：
1、发送邮件的时候，163邮箱用的是客户端授权码，而不是邮箱的登录密码
"""

import yagmail
# yag = yagmail.SMTP(user="cn5036520@163.com", password="123456a", host='smtp.163.com')
# contents = ['This is the body, and here is just text http://somedomain/image.png',
#             'You can find an audio file attached.', '/local/path/song.mp3']
#
# # s = smtplib.SMTP(server)
# # print(yag)
#
# yag.send(to= "cn5036520@163.com")



#
# yag = yagmail.SMTP(user='15210122517@126.com', password='amigo675', host='smtp.126.com')
# print(1)
# yag.send(to = '15210122517@126.com', subject='cn5036519', contents="hahaha")
# print(2)

# yag = yagmail.SMTP(user='cn5036518@126.com', password='123456a', host='smtp.126.com')
# print(1)
# yag.send(to = 'cn5036518', subject='biaoti', contents="hahaha")
# print(2)

yag = yagmail.SMTP(user='15210122517@126.com', password='amigo675', host='smtp.126.com', smtp_ssl=True,port=465,soft_email_validation=False,)
yag.send(to=['15210122517@126.com'], subject='19100203 cn5036519', contents="hahaha")


















