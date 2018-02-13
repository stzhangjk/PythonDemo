#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 迭代器

# 获得Iterator对象:
it = iter([1, 2, 3, 4, 5])


# 循环:
while True:
    try:
        # 获得下一个值:
        print(next(it))
    except StopIteration:
        # 遇到StopIteration就退出循环
        break