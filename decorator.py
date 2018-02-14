#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器

from functools import wraps


def log(message):
    def interim(func):
        @wraps(func)
        def wapper(*args, **kw):
            print('%s %s' % (message, func.__name__))
            return func(*args,**kw)
        return wapper
    return interim


@log('call')
def f(n):
    return 25*n


print(f(4))



