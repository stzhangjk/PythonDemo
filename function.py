#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数


def func(x):
    if x > 10:
        return 10
    else:
        return 1


def func2():
    if True:
        pass
    else:
        return


def func3():
    pass


def func4():
    return 1, 2


# 参数默认值
def func5(x, a=0):
    return a


def add(l=None):
    if l is None:
        l = []
    l.append('END')
    return l


def add2(l=[]):
    l.append('END')
    return l


# 可变参，组装为tuple
def variable(*numbers):
    print(numbers)


# 关键字参数，x组装为dict
def key(a, b, **x):
    print(a)
    print(x)
    print(b)


# 命名关键字参数，
def named(a, b, *, username, password):
    print(a)
    print(b)
    print(username)
    print(password)


def pos(a, b, *variable, username, password):
    print(a)
    print(b)
    print(variable)
    print(username)
    print(password)


def hanoi(n, a='A', b='B', c='C'):
    if n == 1:
        print('move', a, '->', c)
        return
    else:
        hanoi(n-1,a, c, b)
        print('move', a, '->', c)
        hanoi(n-1, b, a, c)


print('==========')
print(add())
print(add())
print('==========')
print(add2())
print(add2())
print('==========')
variable(1, 2, 3, 4, 5)
variable(*[1, 2, 3, 4, 5, 6])
print('==========')
key(1, 2, username='admin', password='123456')
print('==========')
named(1, 2, username='admin',password='123456')
print('==========')
pos(1, 2, 3, 4, username='admin', password='123456')
print('==========')
hanoi(5)