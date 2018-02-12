#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = 0
while i < 10:
    print(i)
    i += 1

print('=============')

i = 0
while i < 10:
    print(i)
    i += 1
    break

print('=============')

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)