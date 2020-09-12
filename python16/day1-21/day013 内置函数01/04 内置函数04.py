#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/19 17:32
#@author:wangtongpei

#eval  参数是字符串，返回的是去掉字符串两端的引号
#1 将字符串形式的列表，转换成列表
s1 = "['jack','tom']"  #字符串转换成了列表，去掉了两端的双引号
print(eval(s1))  #['jack', 'tom']

#2 将字符串形式的字典，转换成字典 应用场景：前后端传递数据的json串就是--字符串形式的字典
s2 = "{'name':'jack','age':123}"  #字符串转换成了字典，去掉了两端的双引号
print(eval(s2)) #{'name': 'jack', 'age': 123}

#3 将字符串形式的数字，转换成数字int
s3 = '12'
print(eval(s3)) #12
print(type(eval(s3))) #<class 'int'>

#4 将字符串形式的数字表达式，转换表达式的结果-int  应用场景：计算器
s4 = '1+2+3'
print(eval(s4)) #6
print(type(eval(s4))) #<class 'int'>
print('-------------------1 eval（）函数 参数是字符串，返回的是去掉字符串两端的引号')

#pycharm只是编辑工具，运行的是python解释器

#2 exec()  可以执行字符串的代码，只是执行，没有返回值（可以变相获得返回结果）
print(exec('''
for i in range(3):
    print(i)
'''))  #py3.7.4支持，py3.6是不支持的
print('-------------------2-1 exec（）函数 执行多行代码')

print(exec("for i in range(2): print(i)"))
print('-------------------2-2 exec（）函数 执行一行代码')

print(exec('1+2+3'))  #None  没有返回值，所以是None
print(exec('a=1+2+3')) #None 没有返回值，所以是None,但是'a=1+2+3' 相当于a=6  注意点
print(exec('a=6')) #None 没有返回值，所以是None,和上面等效  变相获取返回结果
print(a) #6
print('-------------------2-3 exec（）函数 变相获取返回结果')

'''
eval（）和exec()之间的区别
1、前者有返回值
2、后者没有返回值（部分情况，可以变相获得返回值）
'''

#3 compile()
'''
compile() 将字符串类型的代码编译. 代码对象能够通过exec语句来执行或者eval()进行求值

参数1：存放字符串类型的代码
参数2：py文件的文件路径，类型是str
       代码存放的⽂文件名, 当传⼊了第一个参数的时候, 这个参数给空就可以了
参数3：模式，一共是3个，类型是str
        1、模式1--eval模式，对应计算表达式，有返回值的，列表或者字典去掉双引号
        2、模式2--exec模式，没有返回值的，比如for循环
        3、模式3--single模式-交互模式，比如：含有input的

上述参数1和参数2是二选一的
如果用了参数1，参数2就是空字符串''

compile(source, filename, mode)
参数
source -- 字符串或者AST（Abstract Syntax Trees）对象。。
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
mode -- 指定编译代码的种类。可以指定为 exec, eval, single。

返回值
返回表达式执行结果
'''

code1 = '''
for i in range(2):
    print(i) #这里三引号中也需要写缩进，否则报错
def func():
    print('我是函数')
func()
'''
c = compile(code1,'','exec')  #将三引号-字符串中的代码进行编译后，存在一个变量
#注意点，参数2和参数3都是字符串
exec(c) #上面一行是编译，下面是执行，不要忘掉了
print('-------------------3-1 compile()函数+exec（）函数')

f1 =open('code1.py',mode='r',encoding='utf-8')
a1 = f1.read()  #将文件中的代码读出来后，进行执行

# c11 = compile('','code1.py','exec')  #这个写法输出是空白，待确认--nok
c11 = compile(a1,'','exec')  #如果参数2直接写文件，输出是空白；解决办法是想将文件的内容读出来，放在参数1，然后执行
exec(c11)
print('-------------------3-1-1 compile()函数+exec（）函数 执行py文件')

code2 = '1+2+3'
c2 = compile(code2,'','eval')  #将字符串中的代码进行编译后，存在一个变量
ret1 = eval(c2)  #由于eval()没有返回值，这里用一个变量变相返回
# eval(ret1 = c2)  #报错 TypeError: eval() takes no keyword arguments
print(ret1)  #6
print('-------------------3-2 compile()函数+eval（）函数')

# code3 = '''
# content = input('请输入你的姓名：')
# '''
# c3 = compile(code3,'','single')
# exec(c3)
# print(content)  #可以输出你输入的内容，这个pycharn的报错可以忽略
print('-------------------3-3 compile()函数+exel（）函数+single模式')


'''
小结：
compile()和---exec()、eval()的区别
1、前者多了多代码的编译，最后还是要用到后者
2、后者少了编译的动作，直接运行代码

'''

