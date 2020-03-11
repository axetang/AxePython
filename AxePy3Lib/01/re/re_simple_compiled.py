#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Simple pattern examples.
"""

# end_pymotw_header
import re

# Precompile the patterns
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
print(type(re.compile('this')))
text = 'Does this text match the pattern?'

# 目前支持的转换旗标有三种: '!s' 会对值调用 str()，'!r' 调用 repr() 而 '!a' 则调用 ascii()。
print('Text: {!r}\n'.format(text))
print('Number: {!s}'.format(10342.1))
print('Number: {!a}'.format('123唐'))


for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')
