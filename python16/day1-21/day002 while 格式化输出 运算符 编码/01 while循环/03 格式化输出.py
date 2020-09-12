#!/usr/bin/env python
#-*- coding:utf-8 -*-


name = "alex"
age = 18
hobby ="斗地主"

print("我是%s,我今年%s岁了,我的爱好是%s" % (name,age,hobby))
#这里的%s是占位符  %既可以表示字符串,也可以表示数字  %d只能表示数字,而不能表示字符串

name="alex"
# print("我是%s,我已经学习python15%了" % (name))  #报错
# TypeError: not enough arguments for format string   这里的15%的百分号必须用15%% %前面需要加上%进行转义才行
print("我是%s,我已经学习python15%%了" % (name))
#我是alex,我已经学习python15%了
# 结论:当字符串中出现了%s占位符,此时百分号%前面需要加上%进行转义才行  15%应该写成15%%
# 学习方法:这个百分号该怎么写,就怎么写,如果在格式化输出中报错了,就在百分号%前面加上一个百分号%即可









