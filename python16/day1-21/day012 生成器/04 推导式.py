#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/10/6 16:31
#@author:wangtongpei

#题目。输出一个列表，列表的元素依次是python1期，python2期。。。python5期
#方法1  for循环
li1 = []  #1创建列表
for i in range(1,6):  #2循环遍历1-16
    li1.append('python %s 期' % i)  #3装数据
print(li1)
print('------------------------1')

li2 =  [i for i in range(1,6)]  #列表推导式，定义一个列表，其元素是1-5
print(li2)  #[1, 2, 3, 4, 5,]

li3 =  ['python %s期' % i for i in range(1,6)]  #列表推导式的写法是：中括号中有for循环，一行代码
# li3 =  ['python',i for i in range(1,6)]  #必须是占位符%s,不能是逗号
#列表推导式，定义一个列表，其元素是python1期到python5期
print(li3) #['python 1期', 'python 2期', 'python 3期', 'python 4期', 'python 5期']
print('------------------------2 列表推导式')

'''
列表推导式小结：
1、写法：中括号[]中有for循环，一行代码
2、适用场景：生成一个列表，列表的元素是1-5等-等差数列相关的
3、好处：简洁（一行搞定）
4、注意：列表推导式的基础还是for循环，只不过把上述的3行精简成了1行
         逻辑是一样的，写法做了精简

列表推导式步骤：
1、创建一个空列表，先写中括号[]
2、循环遍历，把for i in range(1,6)放入空列表中--中括号[]
3、装数据，省略append，把append()小括号中的'python %s 期' % i放在空列表--中括号[]内的前半部分
4、如果有条件筛选，就把if条件写在中括号内[]的最后（不是必须）
5、保存在一个变量中，把列表推导式用变量保存

列表推导式的格式：  变量名= [结果 for循环 if条件筛选]
'''
li = [i for i in range(1,6)]
li1 = [i for i in range(1,6) if i<3]  #条件筛选，只取小于3的
li2 = ['python %s 期' % i for i in range(1,6)]
print(li)  #[1, 2, 3, 4, 5]
print(li1) #[1, 2]
print(li2) #['python 1 期', 'python 2 期', 'python 3 期', 'python 4 期', 'python 5 期']
print('------------------------2-2 列表推导式')

li1 = []  #1创建列表
for i in range(1,6):  #2循环遍历1-16
    if i>2:
        break
    li1.append(i)  #3装数据
print(li1)  #[1, 2]

li2 = [i for i in range(1,6) if i<3]  #将上述的5行精简成了1行
print(li2)  #[1, 2]
print('------------------------2-3 列表推导式 条件筛选')

#题目2 输出[1,3,5...99],即100及以内的奇数数列
#方法1
li1 = []  #1创建列表
for i in range(1,100):  #2循环遍历1-16
    if i%2==0: #如果除以2的余数是0--表示偶数  （排除法，先排除不符合条件的）
        continue  #跳过当前迭代-小循环，进入下一次小循环
    li1.append(i)  #3装数据
print(li1)  #[1, 2]
#
#方法2  推荐1
li3 = []  #1创建列表
for i in range(1,100):  #2循环遍历1-16
    if i%2==1: #如果除以2的余数是1--表示奇数 （先筛选符合条件的）--比排除法更直接一些，分析  注意点
        li3.append(i)  #3装数据
print(li3)  #[1, 2]
#
#方法3 列表推导式  推荐2
li2 = [i for i in range(1,100) if i%2==1]
#这里是把方法2的4行代码精简成了1行
print(li2)
print('------------------------2-4 列表推导式 条件筛选2 奇数数列')
'''
列表推导式：
1、如果能直接写列表推导式，就直接写
2、如果写不出来，就按传统的for循环的思路，空列表append写完后，再翻译成列表推导式即可
'''












