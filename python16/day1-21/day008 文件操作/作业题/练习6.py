#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
6，文件t6.txt内容(升级题)

序号     部门      人数      平均年龄      备注
1       python    30         26         单身狗
2       Linux     26         30         没对象
3       运营部     20         24         女生多
.......

通过代码，将其构建成这种数据类型：
[{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
......]
'''

f = open('t6.txt',mode='r',encoding='utf-8')
# s6 = f.read()
# print(s6)
li1 = []
# dic1 = {}   #不能放在for循环外面，必须放在for循环里面  --关键点1
#如果放在外面，就只能添加最后一个键值对到字典了
lst1 = f.readline()
# print(lst1)  #序号     部门      人数      平均年龄      备注
# print(type(lst1))  #<class 'str'>
se1,dep1,num1,avg_age1,commont1=lst1.split()
print(se1,dep1,num1,avg_age1,commont1)  #序号 部门 人数 平均年龄 备注

for i in f:
    # print(i.strip())
    a,b,c,d,e =i.strip().split()  #空白作为分隔符进行拆分，分包
    # print(a)
    # dic1 = {se1: a, dep1: b}  # 一行来构造字典  构造字典方法2
    dic1 = {}  #必须放在for循环内部  关键点1
    dic1[se1] = a  #单个键值对一个一个添加  构造字典方法1
    dic1[dep1] = b
    dic1[num1] = c
    dic1[avg_age1] = d
    dic1[commont1] = e
    li1.append(dic1)

# print(dic1)
print(li1)
# [{'平均年龄': '26', '人数': '30', '部门': 'python', '序号': '1', '备注': '单身狗'},
#  {'平均年龄': '30', '人数': '26', '部门': 'Linux', '序号': '2', '备注': '没对象'},
#  {'平均年龄': '24', '人数': '20', '部门': '运营部', '序号': '3', '备注': '女生多'}]

# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
# ......]

'''
伪代码思路
1、先用readline读取第一行，获取到序号、部门、人数、平均年龄、备注（后面用作字典的key）
2、从第二行开始，循环遍历文件对象f
3、空白来作为分隔符，进行拆分
4、构造字典  dic1[se1] = a
5、将字典依次追加到空列表

小结：
1、可以先将序号、部门、人数、平均年龄、备注作为字典的key写死
   等字典构造出来后，再考虑写死的这5个值，如何写活
2、这5个值通过读取文件第一行--readline进行写活

关键点：
dic1 = {}   #不能放在for循环外面，必须放在for循环里面
#如果放在外面，就只能添加最后一个键值对到字典了
'''

















