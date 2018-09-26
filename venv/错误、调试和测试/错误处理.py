#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__arthur__ = "张俊鹏"

# 这种做法很蠢
# def foo():
#     r=some_function()
#     if r==(-1):
#         return (-1)
#     #TODO: something
#     return r
#
# def bar():
#     r=foo()
#     if r==(-1):
#         print("error")
#     else:
#         pass

try:
    print("try...")
    r = 10 / int("0")
    print("result:", r)
except ValueError as e:
    print("ValueError:",e)
except ZeroDivisionError as e:
    print("except:",e)
else:
    print('no error!')
finally:
    print("finally")
print("End")

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

# main()
# print('END')

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()



from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
try :
    main()
except Exception as e:
    logging(e)
finally:
    print('End')
