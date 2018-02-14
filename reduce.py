#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# reduce

a = [1, 2, 3, 4, 5]


def add(a, b):
    return a + b


from functools import reduce
print(reduce(add, a))