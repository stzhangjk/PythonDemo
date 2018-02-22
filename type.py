#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A(object):
    pass


print(type(123))
print(type('str'))
print(type(A()))
print(type(abs))
print(type(None))
print(type(123) == type(234))
print(type('')==str)
print(type(123)==int)

import types

print(type(abs)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

