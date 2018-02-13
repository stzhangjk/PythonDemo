#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器，边循环一遍生成元素

g = (x for x in range(0, 20))
print(g)
for i in g:
    print(i)


# 含有yield的函数变成generator
def fibonacci(n):
    s, a, b = 0, 0, 1
    while s < n:
        s = s + 1
        yield b
        a, b = b, a + b

print([i for i in fibonacci(5)])
