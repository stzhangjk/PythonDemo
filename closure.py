#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 闭包


def f_sum(*numbers):
    def sum():
        s=0
        for i in numbers:
            s = s + i
        return s
    return sum


print(f_sum(1, 2, 3, 4)())


def f_square():
    f = []
    for i in range(1, 4):
        def square():
            return i*i
        f.append(square)
    return f


f1, f2, f3 = f_square()
print(f1(), f2(), f3()) # 9 9 9


def f_square2():
    for i in range(1, 4):
        def square():
            return i*i
        yield square


for square in f_square2():
    print(square())


def count():
    def f(j):
        def g():
            return j*j
        return g
    g = []
    for i in range(1, 4):
        g.append(f(i))
    return g


g1,g2,g3 = count()
print(g1(), g2(), g3())