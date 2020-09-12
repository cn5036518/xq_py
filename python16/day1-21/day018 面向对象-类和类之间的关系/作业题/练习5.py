#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2019/12/28 10:54
#@author:wangtongpei
#@email: cn5036520@163.com

''''''
'''
2. 完成网上商城订单的功能. 写出基本结构和基本操作即可. 把结构一定列出来, 操作可
以没有, 想清楚各个类之间的关系应该是什么样的.(升级题)
每个用户都有一堆订单. 每个订单有一堆订单明细. 每个明细对应一个商品

    用户
        信息: 用户编号, 昵称, 用户名, 密码, 电话, email, 家庭住址, 身份证号
    订单
        信息: 订单编号, 流水号, 所属用户编号, 收货地址. 邮费. 订单状态(0:是
        否发货, 1:是否收货, 2: 是否退货), 评价编号.
    评价
        信息: 评价编号, 评价分数, 评价内容, 评价显示(0:显示, 1:不显示), 评价
        类型(1: 物流评价, 2: 服务评价, 3: 商品评价)
    订单明细
        信息: 明细编号, 小流水号, 商品购买时价格, 购买数量. 商品编号.
    商品
        信息: 商品编号, 商品名称, 商品描述, 商品价格, 商品库存.

'''

class User:
    def __init__(self,userid,nickname,username,password,phone,email,address,id_number):
        self.userid = userid
        self.nickname = nickname
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.address = address
        self.id_number = id_number
        self.order_list = []

    def buy(self,order):  #参数是订单对象
        self.order_list.append(order) #依次下多个订单  一对多  关键点
        #把订单对象作为元素追加到订单列表中（这个订单list和日常说的app上订单列表就对上了）

    def dispaly(self):
        for i in self.order_list:
            print(i.orderid)  #打印订单的编号--订单号

class Order:
    def __init__(self,orderid,serialno,user,receive_address,postage,order_status,evaluation_no):
        self.orderid = orderid
        self.serialno = serialno
        self.user = user
        self.receive_address = receive_address
        self.postage = postage
        self.order_status = order_status
        self.evaluation_no = evaluation_no
        self.oi_list = []

    def compose(self,oi):#参数是订单明细对象
        self.oi_list.append(oi)  #将订单明细添加到订单中，一对多，关键点

    def display(self):
        for i in self.oi_list:
            print(i.oi_id)  #打印订单明细编号

class Order_item:
    def __init__(self,oi_id,s_serialno,price,amount,goods_id):
        self.oi_id = oi_id
        self.s_serialno = s_serialno
        self.price = price
        self.amount = amount
        self.goods_id = goods_id

    def compose(self,goods):  #参数是商品对象
        self.goods = goods  #一对一的关键点 拿self.goods指代商品对象

class Goods:
    def __init__(self,goods_id,goods_name,discription,price,stock):
        self.goods_id = goods_id
        self.goods_name = goods_name
        self.discription = discription
        self.price = price
        self.stock = stock

#新建2个订单对象
o1 = Order('001','202001020838','user001','beijing',5.00,'0','e001')
o2 = Order('002','202001020841','user001','beijing',5.00,'0','e002')
# 订单 信息: 订单编号, 流水号, 所属用户编号, 收货地址.邮费.订单状态(0:是
# 否发货, 1:是否收货, 2: 是否退货), 评价编号.

#新建1个用户
u1 = User('user001','jack','cn5036518','111',13501145281,'cn5036520@163.com',
          '北京朝阳','421102198310240495')
# 用户 信息: 用户编号, 昵称, 用户名, 密码, 电话, email, 家庭住址, 身份证号

u1.buy(o1)  #用户1下第1个订单
u1.buy(o2)  #用户1下第2个订单

u1.dispaly()  #打印用户下的订单的订单号
# 001
# 002
print('--------------------------1 1个用户对应多个订单 一对多')

#新建2个订单明细对象
oi1 = Order_item('oi001','20200104061441',9.9,2,'goodsid001')
oi2 = Order_item('oi002','20200104061541',10.9,3,'goodsid002')

o1.compose(oi1)  #一个订单由2个订单明细组成
o1.compose(oi2)

o1.display()  #打印一个订单下2个订单明细的订单明细id
# oi001
# oi002
print('--------------------------2 1个订单对应多个订单明细 一对多')

#新建1个商品对象
goods1 = Goods('goodsid001','青岛啤酒','好酒',36,100)

oi1.compose(goods1)  #必须要有，不能不写，建立一对一的关系，参数是商品对象   注意点
print(oi1.goods.goods_name) #通过oi1.goods指代商品对象（后面的.goods_name就是商品对象的商品名称）
#通过订单明细对象来打印与其一对一关系的商品对象的商品名称
#青岛啤酒
print('--------------------------3 1个订单明细对应1个商品  一对一')




