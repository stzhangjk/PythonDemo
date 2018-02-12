#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fruit = ['apple', 'banana', 'orange']

print(fruit)

print(len(fruit))

print(fruit[0])
print(fruit[2])

# 最后一个元素
print(fruit[-1])
# 倒数第二个
print(fruit[-2])

# 追加元素
fruit.append('asdhaskjd')
print(fruit[-1])

# 把元素插入到指定的位置，比如索引号为1的位置
fruit.insert(1, 'insert')
print(fruit)

# 弹出末尾元素
print(fruit.pop())
print(fruit)

# 弹出指定位置
print(fruit.pop(1))
print(fruit)

fruit[1]='apple'
print(fruit)

arr = ['abc',12,True]
print(arr)

arrs = [
    456,
    ['abc', 213, True],
    'abc'
]
print(arrs)

# range函数生成整数数列
print(range(6))
print(list(range(7)))