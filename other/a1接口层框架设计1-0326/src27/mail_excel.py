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

import smtplib   #1这四个包是固定需要导入的
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

# path1 = r"D:\PycharmProjects\xiaoqiang\base_181027\a1接口层框架设计1-0326\src26\testcase3.xlsx"
path1 = r".\testcase3.xlsx"

class Send_mail:
    def send_mail(self,title):  #这里邮件标题，发件人，收件人，邮件内容都可以在这里作为形参，
        # 实际调用的时候，填入实际参数即可
        msg = email.mime.multipart.MIMEMultipart() #2生成包含多个邮件体的对象
        msg["from"] = "cn5036520@163.com"
        msg["to"] = "cn5036520@163.com"
        msg["subject"] =title
        content = """
        hello world
        hello world2
        """
        #3邮件正文
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)

        #4 excel附件
        # xlsxpart = MIMEApplication(open("send_mail.xlsx","rb").read())
        xlsxpart = MIMEApplication(open(path1,"rb").read())
        xlsxpart.add_header("Content-Disposition","attachment",filename="接口测试报告.xlsx")
        # xlsxpart.add_header("Content-Disposition","attachment",filename="send_mail2.xlsx")  #附件可以重命名
        msg.attach(xlsxpart)

        #5 jpg图片附件

        #6 发送邮件
        smtp = smtplib
        smtp = smtplib.SMTP()   #SMTP_SSL的端口是465  SMTP的端口是25
        # smtp.set_debuglevel(1) #1 不是必须的，设置为调试模式，console中显示
        smtp.connect("smtp.163.com","25") #2 连接邮件服务器 smtp邮件服务器地址+端口(尽量用163或者126邮箱，qq邮箱可能有限制# )
        smtp.login("cn5036520@163.com","123456a") #3 登录  邮箱用户名+密码（注意：这个密码是客户端授权密码）
        # smtp.sendmail("cn5036520@163.com","cn5036520@163.com","str(msg)") #发送 from+to+内容  注意：str(msg)是不对的，邮件内容会是空白
        smtp.sendmail("cn5036520@163.com","cn5036520@163.com",msg.as_string()) #发送 from+to+内容  msg.as_string()才是对的
        smtp.quit()

mail = Send_mail()  #新建对象
mail.send_mail("hello3") #对象调方法
print("邮件发送成功")

# if __name__ == '__main__':   #主入口
#     sentemail()



















