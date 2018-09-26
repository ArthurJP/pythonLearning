#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str=input("input your age:")
age=int(str);
if age>=18:
    # print("your age is %d" % age)
    print("adult")
elif age>=12:
    print("teenager")
else:
    print("kid")