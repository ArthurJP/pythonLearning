#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Hi %s,your score is %d" % ("joker", 24))

# d前面的数字表示输出占用多少位置，如果有‘0’表示不足位置用0填充
# 如果需要显示的数字大小超过控制位数，显示全部数字
print("%4d-%04d" % (322, 1))

print("%.2f" % (3.14159265))

print("Age: %s,Gender: %s" % (1, "Female"))

# 使用格式化输出后：需要输出‘%’必须使用“%%”，转义符\失效
print("Rate is : %.2f %%" % 3.666)

print("{0} 的成绩提高了 {1:.2f}%".format("Xiaomi",(85-72)/72*100))
