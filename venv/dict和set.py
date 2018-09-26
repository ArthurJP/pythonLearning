#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# dict   dictionary dict的key必须是不可变对象
d = {"A": 1, "B": 2, "C": 3}
print(d["B"])

d["B"] = 22
print(d["B"])

d["B"] = 88
print(d["B"])

print("D" in d)

print(d.get("D", -1))

# print(d.fromkeys())


# set
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)

s.add(4)
print(s)
# 重复添加没有效果
s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)


# 再议不可变对象

a=['c','a','b']
a.sort()
print(a)

a='abc'
b=a.replace('a','A')
print('a:',a)
print('b:',b)
