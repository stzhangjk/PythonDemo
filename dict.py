#!/usr/bin/env python3
# -*- coding: utf-8 -*-

student = {
    'name': '小明',
    'age': 18,
    'skill': 'eat'
}

print(student)

print(student['age'])

# 判断key是否存在
print('name' in student)
print('gender' in student)

# get()
print(student.get('gender', 'male'))
print(student.get('gender'))

# pop()
print(student.pop('name'))
print(student)