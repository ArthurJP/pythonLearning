#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
classmate=['Michael', 'Bob', 'Tracy']
print(classmate)
print(len(classmate))
print(classmate[len(classmate)-1])
print(classmate.append("Adam"))
print(classmate)
print(classmate.insert(0,"Jack"))
print(classmate)
# 删除指定位置的元素，默认为-1
print(classmate.pop(1))
print(classmate)
classmate[1]="replaced"
print(classmate)



# tuple
t=(1,2,3)
print(t)

# 定义只有一个的tuple必须在后面添加一个逗号
t1=('ASS',)
print(t1)

# 可变的tuple,利用list实现
t2=('A','B',['C','D'])
t2[2][0]='X'
t2[2][1]='Y'
print(t2)