#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])
# 如果从开头取可以省略0
print(L[:3])
# 可以逆向截取
print(L[-2:])
# 最后一位为-1
print(L[-2:-1])

L = list(range(100))
print(L[10:20])
r = L[:10:2]
print(r)


# 去除空格
def trim(str):
    if str[:1] == ' ':
        return trim(str[1:])
    if str[-1:] == ' ':
        return trim(str[:-1])
    return str


if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key + ':', value)

# 如何判断一个对象是否为迭代对象：通过collections模块的Iterable类型判断
from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 2), (3, 3)]:
    print(x, y)


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 列表生成式
print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ' if m + n != 'AX'])

import os

print([d for d in os.listdir('./')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([x + '=' + y for x, y in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 生成器 generator ：用于解决列表生成器生成大量元素导致的内存浪费
# generator使用一边循环一边计算的机制
# 第一种方式：使用（）
g = (x * x for x in range(1, 11))
print(g)
for n in g:
    print(n)


# 第二种方式：使用yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(4))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


print(fib(4))
# 这种方式可以循环执行generator，但是获取不到返回值
for n in fib(4):
    print(n)
# 获取返回值的方式
g = fib(4)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 这里L[x+1]不会越界：range()不取上界
# x=len(L)-1-1
# x+1=len(L)-1刚好可以取到最大值而不越界
def triangles():
    L = [1]
    while (True):
        yield L
        M = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L = [1] + M + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


# 迭代器
from collections.abc import Iterable,Iterator
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance(([]),Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(1,11)),Iterable))
print(isinstance(100,Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print("Iterator")
print(isinstance((x for x in range(1,11)),Iterator))
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance(([]),Iterator))
print(isinstance('abc',Iterator))

# 将Iterable 变成Iterator使用iter()
print(isinstance(iter([]),Iterator))
print(isinstance(iter('abc'),Iterator))
# Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。


# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 只有tunple 是Iterator
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。