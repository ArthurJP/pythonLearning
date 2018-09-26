#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(abs(-10))

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(123))
print(bool(1))
print(bool(''))

print(hex(1080))


# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x;
    else:
        return -x;


print(my_abs(199))


# print(my_abs("A"))


# pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    if not isinstance((a, b, c), int):
        raise TypeError("Bad Operand type")
    delta = b * b - 4 * a * c
    if (delta) > 0:
        print("此方程有双实根")
        x1 = (-b + math.sqrt(delta)) / a * 2
        x2 = (b + math.sqrt(delta)) / a * 2
        return x1, x2
    elif delta == 0:
        print("此方程有单实根")
        return -b / a * 2
    else:
        print("此方程没有根")
        return None


def power(x, n=2):
    s = 1
    while n > 0:
        s *= x
        n -= 1
    return s


print(power(5, 2))


def add_end(L=None):
    if L == None:
        L = []
    L.append('end')
    return L


print(add_end())
print(add_end())


# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


# 调用的时候，需要先组装出一个list或tuple
print(calc([1, 2, 3]))
print(calc((1, 2, 3)))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1, 2, 3, 4))

# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传入
num = [1, 2, 3, 4]
print(calc(*num))


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print("name:", name, "age:", age, "other:", kw)


person('Michael', 30)
person("Adam", 45, gender="M", job="Engineer")

# 可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(*extra)
print(extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person("Tom", 24, **extra)


# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person(name, age, *args, city="Taiyuan", job):
    print(name, age, args, city, job)


person('Jack', 24, job='Engineer')


# 组合参数
# 顺序：必选参数、默认参数、可变参数、命名关键字、关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 20, 'x': '#'}
f2(*args,**kw)


# 递归函数
def fact(n):
    if n==1:
        return 1;
    return n*fact(n-1)

print(fact(5))

# 尾递归 ：防止栈溢出
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)



# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')