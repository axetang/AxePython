#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import string

s = 'The quick brown fox   jumped    over the lazy dog.'

print(s)
# string.capwords()删除了多余的空格
print('string.capwords()', string.capwords(s))
print(string.capwords("This is my first Py3Lib codes."))

# capwords()相当于如下操作
l = s.split(' ')
print(l)
l = [w.title() for w in l if w]
print(l)
str = ' '.join(l)
print(str)
