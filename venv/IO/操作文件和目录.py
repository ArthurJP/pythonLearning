#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__arthur__ = "张俊鹏"

import os

print(os.name)
# print(os.uname()) #该函数在windows上不提供

env = os.environ
print(env)

path = os.environ.get("PATH", "default")
print(path)

print(os.path.abspath('./'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/users/michael', 'testdir'))
# 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')

print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

# os.rename('test.txt','test.py')
# os.remove('test.py')

from shutil import copyfile

copyfile('reading.txt','copied.txt')


print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir("./") if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


