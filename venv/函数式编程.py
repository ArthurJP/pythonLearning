#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 传入函数
def add(x, y, f):
    return f(x) + f(y)


print(add(5, -6, abs))


# map/reduce
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8])
# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(r))

print(list(map(str, [1, 2, 3])))

from functools import reduce


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


def str2int(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        return 10 * x + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int("11010"))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("998"))


def normalize(name):
    return name[:1].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def str2num(s):
        return DIGITS[s]

    def fn(x, y):
        return x * 10 + y

    i = s.index('.')
    s = s[:i] + s[i + 1:]
    return reduce(fn, map(str2num, s)) / (10 ** (len(s) - i))
    # 这里s已经减去了'.'，所以小数部分位数不需要在减1


# print('123.456'.__len__())
# print('123.456'.index('.'))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# filter
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 全体素数的表示
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


def is_palindrome(n):
    k = str(n)
    return k == k[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# sorted
r = sorted([36, 5, -12, 9, -21], key=abs, reverse=True)
print(r)

r = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(r)  # 默认使用ASCII码进行排序

r = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(r)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_score)
print(L2)


# 函数作为返回值

# 常见的求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)


# 闭包 Closure

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs  # 返回list


#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs  # 这里返回的并不是内部的函数


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# def createCounter():
#     global i
#     i=0
#     def counter():
#         global i
#         i=i+1
#         return i
#     return counter


# def createCounter():
#     n=[0]
#     def counter():
#         n[0]=n[0]+1
#         return n[0]
#     return counter


def createCounter():
    def iter():
        n = 1
        while 1:
            yield n
            n += 1

    it = iter()

    def counter():
        return next(it)

    return counter  # 这里调用counter是为了将函数变成可重复调用的，并且会保存上一次的调用结果数据，对本次调用产生影响


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# 匿名函数
r = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

f = lambda x: x * x
print(f)


# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y


print(build(1, 10))  # 直接返回的匿名函数无法直接执行

f = build(1, 10)
print(f)
print(f())

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)

# 装饰器
import time


def now():
    print(time.asctime(time.localtime(time.time())))


f = now
f()

print(now.__name__)


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
# 称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)  # 最终要返回原函数

    return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
#
# 次标注的函数需要在标注之前
@log
def now():
    print(time.asctime(time.localtime(time.time())))


now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print(time.asctime(time.localtime(time.time())))


now()

now = log('final')(now)  # final wrapper():
print(now.__name__)
# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，
# 所以，一个完整的decorator的写法如下：
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # wrapper.__name__ = func.__name__
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log(text='execute')
def now():
    print(time.asctime(time.localtime(time.time())))


log('final')(now)()

print("练习 metric")


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end - start))
        return func(*args, **kw)

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

from inspect import isfunction


def logger(arg=''):
    if type(arg) == str or not arg:
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print(arg + "begin call")
                fw = fn(*args, **kw)
                print(arg + "end call")
                return fw

            return wrapper

        return decorator
    if isfunction(arg):
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print("begin call")
            fw = arg(*args, **kw)
            print("end call")
            return fw

        return wrapper


@logger('excute')
def a(name):
    return name


@logger
def b(name):
    return name


A = a('Test A')
print(A)
print()
B = b('Test B')
print(B)


# 偏函数
def int2(x, base=2):
    return int(x, base)


print(int2('1000000'))

import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))

max2 = functools.partial(max, 10) # 会把10作为*args的一部分自动加到左边
print(max2(5, 6, 7))


