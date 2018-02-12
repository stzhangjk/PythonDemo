#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set 不重复、无序集合

print(set([1, 2, 3, 4]))
print(set([1, 1, 2, 2, 3, 4, 5, 5]))

s = set([1, 2, 3])

# add()
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(3)
print(s)


a = set([1, 2, 3])
b = set([4, 5, 6])
print(a & b)  # &交集
print(a | b)  # |并集
