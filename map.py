#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map

a = [1, 2, 3, 4, 5]


def square(x):
    return x * x


print(list(map(square, a)))