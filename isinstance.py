#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    pass


class Dog(Animal):
    pass


dog = Dog()
print(isinstance(dog, Dog) and isinstance(dog, Animal))

import types
print(isinstance('123', str))
print(isinstance(123, int))
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance([1, 2, 3, 4], (list, tuple)))  # 判断是否是两个类型中的一个
