#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__arthur__ = "arthur"
# 这种变量是特殊变量，可以直接引用，但是有特殊用途

import sys
from numpy import *

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")


if __name__ == "__main__":
    test()


# 作用域
# python中不存在完全无法访问的private函数或者变量，
# 使用_xx,__xx命名的变量或者函数不应该被外部引用

def _private_1(name):
    return "hello %s" % name


def _private_2(name):
    return "Hi %s" % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



