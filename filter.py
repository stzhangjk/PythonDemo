#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter()


def odd_number():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divide(n):
    return lambda x: x % n != 0


def prime():
    yield 2
    a = odd_number()
    while True:
        n = next(a)
        yield n
        a = filter(not_divide(n), a)


for n in prime():
    if n > 1000:
        break
    print(n)
