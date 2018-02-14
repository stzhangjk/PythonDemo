#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = [5, 6, -7, 3, -6, 7, 2, 0, -9, 4, 98, 2, 5]

print(sorted(a))
print(sorted(a, key=abs))
print(sorted(a, reverse=True))