#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成器

print([x * x for x in range(1, 10)])
# 加条件
print([x * x for x in range(1, 10) if x % 2 == 0])
# 多变量
print([m + n + o for m in 'ABC' for n in 'XYZ' for o in 'PQR'])

import os
print([d for d in os.listdir('.')])

dict = {'name': 'Tom', 'age': 18, 'gender': 'male'}
print([k + '=' + str(v) for k, v in dict.items()])

list = ['Abc', 'Banana', 'Orange']
print([l.lower() for l in list])