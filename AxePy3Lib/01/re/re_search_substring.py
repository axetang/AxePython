#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Searching a substring of the input.
"""

# end_pymotw_header
import re

text = 'This is some text -- with punctuation.'
pattern = re.compile(r'\b\w*is\w*\b')
print(type(pattern), pattern)
match = pattern.search(text, 0)
print(type(match), match)

print('Text:', text)
print()

pos = 0
while True:
    # pattern的search方法和re的search函数用法不同
    # 接受可选的start和end位置参数
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print('  {:>2d} : {:>2d} = "{}"'.format(
        s, e - 1, text[s:e]))
    # Move forward in text for the next search
    pos = e
