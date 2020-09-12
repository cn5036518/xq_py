#!/usr/bin/env python

"""
设计接口自动化测试框架的步骤
1、整体构思-中心思想和提纲（不考虑具体的实现，即作文内容--和写作文的类比）
    比如：流程图 结构图 文字  （听的时候，思考少；写的时候，思考多）
2、目录规划
3、伪代码
4、写代码（硬编码，先能跑起来，小步迭代  比如：参数写死，功能最少demo）

一、整体构思
1主入口--2遍历接口--3发送请求--4得到返回--5对比结果--6测试报告--7发送邮件

二、目录结构
1、主入口的py文件--main
2、核心代码py文件夹--src
    遍历接口
    发送请求-得到返回
    对比结果

3、存放接口测试用例的文件夹--case
   存放形式：excel（推荐）或者数据库
   推荐excel的原因：
   1、维护excel简单
   2、数据库学习成本稍高
   3、简便性上excel占优

   excel的字段设计：
   1、url
   2、请求报文
   3、请求方式post还是get
   4、实际返回报文
   5、期望结果
   6、通过状态
   7、备注

4、存在公共函数的文件夹--commons
   公共函数：已经封装好的，比较独立的实现一个小功能，且不依赖别的部分
   例如：http的请求类
        发送邮件的类
        发日志的类

5、存放测试报告的文件夹--reports
   excel形式的报告（推荐）优于html的报告
   原因：
   1、excel的统计功能

6、放插件的文件夹--others
7、存放日志文件的文件夹--logs

三、课上练习
1、目前先把所有的py文件全不放在src核心文件夹
    等代码调通后，最后将py文件分发到其他目录中，从而避免开始就出现导包错误
2、http请求类就绪
3、接口请求类的编写：class Interface_test:
    调用请求类并对结果进行对比判断
    不用unittest的断言，而是使用re.search完成
    所有参数全部写死（不从excel进行读取）
4、保证上面的代码可以正常运行并且测试通过

四、课上练习伪代码
    class Interface_test:
        def 方法名(self):
            http请求类的调用
            发送请求
            获取响应
            re.search(检查点,响应内容)
            if re.search(error_code="0",请求类的整个返回r):
                print("xxx")
            else:
                print("xx")

#search函数 匹配字符串的全部，并且返回第一个符合条件的字符串（从左到右）
print(re.search("www","22wwwcom").group()) #www  扫描字符串全部
# 参数1是正则表达式，参数2是待匹配的字符串  group()是显示匹配后的结果,可视化
"""
import re
from http_class2 import Requests_Post1   #导入http请求文件的类

class Interface_test:
    def test(self):
        # 1定义参数     #注意：这里的参数是写死的
        self.url = "http://v.juhe.cn/laohuangli/d"
        self.params1 = {"key": "e711bc6362b3179f5a28de7fd3ee4ace",
                   "date": "2016-5-14"}  # 拼写错误，date而不是data  这个key是固定的，申请好的
        self.headers1 = {}

        # 2新建对象
        requests1 = Requests_Post1(self.url, self.params1,self.headers1)  # 传入实际参数

        # 3通过对象调方法
        result1 = requests1.requests_post2()

        print("post请求获取响应结果（python-字典类型）=", result1)  # 5输出整个返回内容（字典类型）
        print("错误码error_code是：", result1["error_code"])  # 6输出错误码error_code
        result2 = str(result1["error_code"])

        print(re.search('0',result2).group())  #注意：search的参数1和参数2的类型必须是字符串str，而不能是数字，字典
        #参数一必须是字符串或者是正则表达式
        # print(re.search(0,result2).group())  #注意：search的参数1和参数2的类型必须是字符串str，而不能是数字，字典
        #TypeError: first argument must be string or compiled pattern

#新建对象
test1 = Interface_test()

#对象调方法
test1.test()





















