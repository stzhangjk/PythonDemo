#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代
list = [1, 2, 3, 4, 5, 6]
for l in list:
    print(l)

dict = {'username': 'admin', 'password': '123456'}
for k in dict.keys():
    print(k)
    print(dict[k])

str = "abcdefg"
for s in str:
    print(s)

# 判断是否可迭代
from collections import Iterable
print(isinstance("abc",Iterable))
print(isinstance([1, 2, 3, 4, 5, 6],Iterable))
print(isinstance(123,Iterable))

a = [(1, 2), (2, 3), (3, 4)]
for x, y in a:
    print(x, y)

for i, value in enumerate(list):
    print(i, value)