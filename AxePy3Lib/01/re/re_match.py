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

print('Text   :', text)
print('Pattern:', pattern)

# 如果模式必须出现在输入开头，那么使用match而不是search来锚定搜索即可
m = re.match(pattern, text)
print('Match  :', m)
# 如果不要求必须出现在开头，则使用search,search也只能搜索一次，要全部搜索，
# 建议使用finditer函数来构建iterable的对象进行遍历
s = re.search(pattern, text)
print('Search :', s)
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(pattern, s, e))
