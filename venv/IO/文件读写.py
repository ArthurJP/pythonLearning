#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__arthur__ = "张俊鹏"

with open('E:/code/pythonLearning/venv/IO/reading.txt', 'r', encoding='utf-8', errors='ignore') as f:
    # print(f.read()) # 这样会一次性读完，但是可能导致内存溢出
    for line in f.readlines():
        print(line.strip())

# f = open("E:/code/pythonLearning/venv/IO/writing.txt",'w')
# f.write("writing test")
# f.close()


with open("E:/code/pythonLearning/venv/IO/writing.txt", 'w') as f:
    f.write("advanced writing test")

from io import StringIO

# StringIO顾名思义就是在内存中读写str
f = StringIO()
print(f.write('hello'))
print(f.write(" "))
print(f.write("world!"))
print(f.getvalue())

f = StringIO("Hello!\nHi!\nGoodbye!")
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
