#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum=0
for x in range(101):
    sum+=x
print(sum)


sum=0
n=99
while n>0:
    sum+=n;
    n-=2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("hello",name+"!")


n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1
print("END")


n=0
while n<10:
    if n%2!=0:
        print(n)
    n+=1