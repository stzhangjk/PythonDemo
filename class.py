#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print(self):
        print('name: %s, age: %s' % (self.__name, self.__age))


a = Student('Tom', 10)
b = Student('Jerry', 100)
a.print()
b.print()

print(a._Student__name)
