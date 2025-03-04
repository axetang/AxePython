#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Matching vs. searching
"""

# end_pymotw_header
import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text       :', text)
print('Pattern    :', pattern)

m = re.search(pattern, text)
print(type(m), m)
print('Search     :', m)
# fullmatch要求整个字符串与模式匹配
s = re.fullmatch(pattern, text)
print('Full match :', s)

print(re.fullmatch(pattern, "is").span())
