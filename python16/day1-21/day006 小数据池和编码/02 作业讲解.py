#重点题目回顾和重写

# 5、元素分类
# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，
# 将所有大于 66 的值保存至字典的第一个key中，
# 将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}

#方法1 空字典{}  空列表   好理解
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {}
li1 = []
li2 = []
for i in li:
    if i > 66:
        li1.append(i)  #空列表追加
    else:
        li2.append(i)
dic1["k1"] = li1  #字典新增键值对
dic1["k2"] = li2
print(dic1)  #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}

#方法2  非空字典{}   #比较简洁，代码行数较少
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {"k1":[],"k2":[]}
for i in li:
    if i > 66:
        dic1["k1"].append(i)
    else:
        dic1["k2"].append(i)
print(dic1) #{'k2': [11, 22, 33, 44, 55, 66], 'k1': [77, 88, 99, 90]}

#方法3  字典的get方法
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {}
for i in li:
    if i > 66:
        if dic1.get("k1") == None: #1 如果key="k1"不存在，就新增
            dic1["k1"] = [i]  #注意点：这里必须是[i],而不能是i
        else:  #2 如果key=k1存在，就往value-列表中追加新元素
            dic1["k1"].append(i)
    else:
        if dic1.get("k2") == None:  #1 如果key="k2"不存在，就新增
            dic1["k2"] = [i] #注意点：这里必须是[i],而不能是i
        else:  #2 如果key=k2存在，就往value-列表中追加新元素
            dic1["k2"].append(i)
print(dic1)  #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}

#方法4  字典的setdefault方法
li= [11,22,33,44,55,66,77,88,99,90]
dic1 = {}
for i in li:
    if i > 66:
        ret1 = dic1.setdefault("k1",[])  #新增功能:"k1"之前不存在，就新增键值对；“k1”存在，就不操作（不覆盖）
                                        # 返回value--查询功能
        #注意：这里value必须是[],而不是[i]
        ret1.append(i) #往列表中追加新元素
        #ret1 第一次取值是[77]
        #ret1 第二次取值是[77,88]
        #ret1 第三次取值是[77,88,99]，依次类推--过程重要   不跳步骤，足够耐心
    else:
        ret2 = dic1.setdefault("k2", [])  # 新增:"k1"之前不存在，就新增键值对；“k1”存在，就不操作（不覆盖）  返回value
        ret2.append(i)  #往列表中追加新元素
print(dic1) #{'k2': [11, 22, 33, 44, 55, 66], 'k1': [77, 88, 99, 90]}
print("---------------1")

# 6、输出商品列表，用户输入序号，显示用户选中的商品(升级题)
#
# 商品列表：
goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10},
 {"name": "游艇", "price": 20}, {"name": "美女", "price": 998}, ]
#
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       		1 电脑 1999
# 	   		2 鼠标 10
#      		…
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。

#6-1 不打印序号
# for i in goods:
#     print(i["name"],i["price"])

#6-1 打印序号
for i in range(len(goods)):  #i 是0-3
    print(i+1,goods[i]["name"],goods[i]["price"])
print("---------------6-1")

#6-2  方法1  --不推荐
# 用户输入选择的商品序号，然后打印商品名称及商品价格
goods = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10},
 {"name": "游艇", "price": 20}, {"name": "美女", "price": 998}, ]

# for i in range(10):  #0-9 限定输入10次
# # while 1:  #不限定输入次数
#     content = int(input("请输入商品编号："))  #输入的是字符串，需要转换成int  #这里如果输入的不是字符串数字，就会报错
# #ValueError: invalid literal for int() with base 10: 'ss'
#     #商品编号-1 = 索引编号
#     if content>0 and content<=len(goods):
#         print(goods[content-1]["name"],goods[content-1]["price"])
#     else:
#         print("没有找到对应的商品，请重新输入")

#6-2 方法2  推荐
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序
while 1:
    content = input("请输入商品编号：") #输入的是字符串
    if content.upper() == "Q":
        print("退出程序")
        break
    elif content.isdigit():
        content = int(content)
        if content>0 and content <=len(goods):
            print(goods[content-1]["name"],goods[content-1]["price"])
        else:
            print("您输入的商品编号不存在，请重新输入")
    else:
        print("输入有误，请重新输入数字")












